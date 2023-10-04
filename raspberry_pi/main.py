import json
import logging
import urllib.request

ROOM_ID = "myroom"
SERVER_URL_BASE = "http://localhost:8000"

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

req_body = json.dumps({"id": ROOM_ID}).encode("utf-8")
req = urllib.request.Request(
    f"{SERVER_URL_BASE}/rooms",
    method="POST",
    headers={"Content-Type": "application/json"},
    data=req_body,
)
with urllib.request.urlopen(req) as res:
    logger.info("Room created. id = %s", ROOM_ID)


while True:
    req = urllib.request.Request(f"{SERVER_URL_BASE}/rooms/{ROOM_ID}/poll")
    with urllib.request.urlopen(req) as res:
        res_body = res.read().decode("utf-8")
        room = json.loads(res_body)
        logger.info(
            "Room detail received. room.id = %s, room.is_light_on = %s",
            room["id"],
            room["is_light_on"],
        )
