from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.room import Room, RoomDatabase

room_database = RoomDatabase()

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/rooms")
async def get_rooms() -> list[Room]:
    return room_database.get_rooms()


@app.get("/rooms/{room_id}")
async def get_room(room_id: str) -> Room:
    if not room_database.exist_room_id(room_id):
        raise HTTPException(status_code=404, detail="Room not found")

    return room_database.get_room(room_id)


@app.post("/rooms/{room_id}/register")
async def create_room(room_id: str) -> Room:
    return room_database.register(room_id)


class UpdateRoomRequestBody(BaseModel):
    is_light_on: Optional[bool] = None
    is_fan_on: Optional[bool] = None


@app.post("/rooms/{room_id}/update")
async def update_room(room_id: str, body: UpdateRoomRequestBody) -> Room:
    if not room_database.exist_room_id(room_id):
        raise HTTPException(status_code=404, detail="Room not found")

    return room_database.update_room(room_id, body.is_light_on, body.is_fan_on)


@app.get("/rooms/{room_id}/poll")
async def poll_room(room_id: str) -> Room:
    if not room_database.exist_room_id(room_id):
        raise HTTPException(status_code=404, detail="Room not found")

    return await room_database.poll(room_id)
