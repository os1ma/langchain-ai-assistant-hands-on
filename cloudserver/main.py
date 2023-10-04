import asyncio
import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class Room:
    def __init__(self, id: str, is_light_on: bool) -> None:
        self.id = id
        self.is_light_on = is_light_on
        self.event = asyncio.Event()

    def turn_light(self, on: bool) -> None:
        self.is_light_on = on
        self.event.set()
        self.event.clear()


rooms: list[Room] = []

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/rooms")
async def get_rooms():
    return rooms


class CreateRoomRequestBody(BaseModel):
    id: str


@app.post("/rooms")
async def create_room(body: CreateRoomRequestBody):
    room = Room(id=body.id, is_light_on=False)
    rooms.append(room)
    return room


@app.get("/rooms/{room_id}")
async def get_room(room_id: str):
    for room in rooms:
        if room.id == room_id:
            return room

    raise HTTPException(status_code=404, detail="Room not found")


class UpdateRoomRequestBody(BaseModel):
    is_light_on: bool


@app.post("/rooms/{room_id}/update")
async def update_room(room_id: str, body: UpdateRoomRequestBody):
    for room in rooms:
        if room.id == room_id:
            room.turn_light(body.is_light_on)
            logger.info(
                "Room updated. id = %s,  is_light_on = %s", room.id, room.is_light_on
            )
            return room

    raise HTTPException(status_code=404, detail="Room not found")


@app.get("/rooms/{room_id}/poll")
async def poll_room(room_id: str):
    for room in rooms:
        if room.id == room_id:
            try:
                await asyncio.wait_for(room.event.wait(), timeout=10)
            except asyncio.TimeoutError:
                logger.info("Timeout")
            return room

    raise HTTPException(status_code=404, detail="Room not found")
