#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

ROOM_ID="testroom"
SERVER_HOST="localhost"
SERVER_PORT="8000"

# GET /
curl -f http://${SERVER_HOST}:${SERVER_PORT}
echo

# GET /rooms
curl -f http://${SERVER_HOST}:${SERVER_PORT}/rooms
echo

# POST /rooms/{room_id}/register
curl -f -X POST \
  -H 'Content-Type: application/json' \
  http://${SERVER_HOST}:${SERVER_PORT}/rooms/${ROOM_ID}/register
echo

# GET /rooms
curl -f http://${SERVER_HOST}:${SERVER_PORT}/rooms
echo

# POST /rooms/{room_id}/update
# update is_light_on
curl -f -X POST \
  -H 'Content-Type: application/json' \
  http://${SERVER_HOST}:${SERVER_PORT}/rooms/${ROOM_ID}/update \
  -d '{"is_light_on": true}'
echo

# POST /rooms/{room_id}/update
# update is_fan_on
curl -f -X POST \
  -H 'Content-Type: application/json' \
  http://${SERVER_HOST}:${SERVER_PORT}/rooms/${ROOM_ID}/update \
  -d '{"is_fan_on": true}'
echo

# GET /rooms/{room_id}
curl -f http://${SERVER_HOST}:${SERVER_PORT}/rooms/${ROOM_ID}
echo

# GET /rooms/{room_id}/poll
curl -f http://${SERVER_HOST}:${SERVER_PORT}/rooms/${ROOM_ID}/poll
echo
