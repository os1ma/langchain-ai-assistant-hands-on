import asyncio
import logging
from typing import Optional

from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class Room(BaseModel):
    id: str
    is_light_on: bool
    is_fan_on: bool


class RoomEventPair:
    def __init__(self, room_id: str) -> None:
        self.room = Room(id=room_id, is_light_on=False, is_fan_on=False)
        self.event = asyncio.Event()


class RoomDatabase:
    def __init__(self) -> None:
        # ルームIDをキーとしたルームの一覧
        self.roomEventPairs: dict[str, RoomEventPair] = {}

    def exist_room_id(self, room_id: str) -> bool:
        return room_id in self.roomEventPairs

    def get_rooms(self) -> list[Room]:
        rooms = []
        for roomService in self.roomEventPairs.values():
            rooms.append(roomService.room)
        return rooms

    def get_room(self, room_id: str) -> Room:
        return self.roomEventPairs[room_id].room

    def register(self, room_id: str) -> Room:
        roomService = RoomEventPair(room_id=room_id)
        # すでに存在する場合は上書きします
        self.roomEventPairs[room_id] = roomService
        return roomService.room

    def update_room(
        self, room_id: str, is_light_on: Optional[bool], is_fan_on: Optional[bool]
    ) -> Room:
        roomEventPair = self.roomEventPairs[room_id]

        room = roomEventPair.room
        if is_light_on is not None:
            room.is_light_on = is_light_on
        if is_fan_on is not None:
            room.is_fan_on = is_fan_on

        logger.info(
            "Room updated. id = %s, is_light_on = %s, is_fan_on = %s",
            room.id,
            room.is_light_on,
            room.is_fan_on,
        )

        event = roomEventPair.event
        event.set()
        event.clear()

        return room

    async def poll(self, room_id: str) -> Room:
        roomEventPair = self.roomEventPairs[room_id]
        room = roomEventPair.room
        event = roomEventPair.event

        try:
            await asyncio.wait_for(event.wait(), timeout=10)
        except asyncio.TimeoutError:
            logger.info("Room poll timeout. room_id = %s", room.id)
        return room
