import json
import logging
import urllib.request
import sys

SERVER_URL_BASE = "http://localhost:8000"

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

room_id = sys.argv[1]
logger.info("Room id = %s", room_id)

req = urllib.request.Request(
    f"{SERVER_URL_BASE}/rooms/{room_id}/register",
    method="POST",
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(req) as res:
    logger.info("Room registered. id = %s", room_id)


while True:
    req = urllib.request.Request(f"{SERVER_URL_BASE}/rooms/{room_id}/poll")
    with urllib.request.urlopen(req) as res:
        res_body = res.read().decode("utf-8")
        room = json.loads(res_body)
        logger.info(
            "Room detail received. room.id = %s, room.is_light_on = %s",
            room["id"],
            room["is_light_on"],
        )
