#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

readonly ROOM_ID="myroom"
readonly SERVER_HOST=${SERVER_HOST:-localhost}
readonly SERVER_PORT=${SERVER_PORT:-80}
readonly BASIC_AUTH_USERNAME=${BASIC_AUTH_USERNAME:-testuser}
readonly BASIC_AUTH_PASSWORD=${BASIC_AUTH_PASSWORD:-testpassword}

readonly ON_OFF="$1"

REQUEST_BODY=$(cat << EOT
{
  "is_light_on": ${ON_OFF}
}
EOT
)

# update is_light_on
curl -f -u ${BASIC_AUTH_USERNAME}:${BASIC_AUTH_PASSWORD} \
  -X POST \
  -H 'Content-Type: application/json' \
  http://${SERVER_HOST}:${SERVER_PORT}/rooms/${ROOM_ID}/update \
  -d "${REQUEST_BODY}"
echo
