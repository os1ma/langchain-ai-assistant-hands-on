import uuid

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Room(BaseModel):
    id: str
    is_light_on: bool


rooms: list[Room] = []

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/rooms")
async def get_rooms():
    return rooms


@app.post("/rooms")
async def post_room():
    id = str(uuid.uuid4())
    room = Room(id=id, is_light_on=False)
    rooms.append(room)
    return room


@app.get("/rooms/{room_id}")
async def get_room(room_id: str):
    for room in rooms:
        if room.id == room_id:
            return room

    raise HTTPException(status_code=404, detail="Room not found")


@app.get("/rooms/{room_id}/poll")
async def poll_room(room_id: int):
    for room in rooms:
        if room.id == room_id:
            return room

    raise HTTPException(status_code=404, detail="Room not found")
