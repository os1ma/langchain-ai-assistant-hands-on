import secrets
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

from app.room import Room, RoomDatabase

room_database = RoomDatabase()

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}


security = HTTPBasic()


def basic_auth(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"testuser"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"testpassword"
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return


room_router = APIRouter(prefix="/rooms", dependencies=[Depends(basic_auth)])


@room_router.get("")
async def get_rooms() -> list[Room]:
    return room_database.get_rooms()


@room_router.get("/{room_id}")
async def get_room(room_id: str) -> Room:
    if not room_database.exist_room_id(room_id):
        raise HTTPException(status_code=404, detail="Room not found")

    return room_database.get_room(room_id)


@room_router.post("/{room_id}/register")
async def create_room(room_id: str) -> Room:
    return room_database.register(room_id)


class UpdateRoomRequestBody(BaseModel):
    is_light_on: Optional[bool] = None
    is_fan_on: Optional[bool] = None


@room_router.post("/{room_id}/update")
async def update_room(room_id: str, body: UpdateRoomRequestBody) -> Room:
    if not room_database.exist_room_id(room_id):
        raise HTTPException(status_code=404, detail="Room not found")

    return room_database.update_room(room_id, body.is_light_on, body.is_fan_on)


@room_router.get("/{room_id}/poll")
async def poll_room(room_id: str) -> Room:
    if not room_database.exist_room_id(room_id):
        raise HTTPException(status_code=404, detail="Room not found")

    return await room_database.poll(room_id)


app.include_router(room_router)
