#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

readonly ROOM_ID="testroom"
readonly SERVER_HOST=${SERVER_HOST:-localhost}
readonly SERVER_PORT=${SERVER_PORT:-80}
readonly BASIC_AUTH_USERNAME=${BASIC_AUTH_USERNAME:-testuser}
readonly BASIC_AUTH_PASSWORD=${BASIC_AUTH_PASSWORD:-testpassword}

# GET /
curl -f http://${SERVER_HOST}:${SERVER_PORT}
echo

# GET /rooms
curl -f -u ${BASIC_AUTH_USERNAME}:${BASIC_AUTH_PASSWORD} \
  http://${SERVER_HOST}:${SERVER_PORT}/rooms
echo

# POST /rooms/{room_id}/register
curl -f -u ${BASIC_AUTH_USERNAME}:${BASIC_AUTH_PASSWORD} \
  -X POST \
  -H 'Content-Type: application/json' \
  http://${SERVER_HOST}:${SERVER_PORT}/rooms/${ROOM_ID}/register
echo

# GET /rooms
curl -f -u ${BASIC_AUTH_USERNAME}:${BASIC_AUTH_PASSWORD} \
  http://${SERVER_HOST}:${SERVER_PORT}/rooms
echo

# POST /rooms/{room_id}/update
# update is_light_on
curl -f -u ${BASIC_AUTH_USERNAME}:${BASIC_AUTH_PASSWORD} \
  -X POST \
  -H 'Content-Type: application/json' \
  http://${SERVER_HOST}:${SERVER_PORT}/rooms/${ROOM_ID}/update \
  -d '{"is_light_on": true}'
echo

# POST /rooms/{room_id}/update
# update is_fan_on
curl -f -u ${BASIC_AUTH_USERNAME}:${BASIC_AUTH_PASSWORD} \
  -X POST \
  -H 'Content-Type: application/json' \
  http://${SERVER_HOST}:${SERVER_PORT}/rooms/${ROOM_ID}/update \
  -d '{"is_fan_on": true}'
echo

# GET /rooms/{room_id}
curl -f -u ${BASIC_AUTH_USERNAME}:${BASIC_AUTH_PASSWORD} \
  http://${SERVER_HOST}:${SERVER_PORT}/rooms/${ROOM_ID}
echo

# GET /rooms/{room_id}/poll
curl -f -u ${BASIC_AUTH_USERNAME}:${BASIC_AUTH_PASSWORD} \
  http://${SERVER_HOST}:${SERVER_PORT}/rooms/${ROOM_ID}/poll
echo

echo "All tests passed!"
