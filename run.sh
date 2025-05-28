#!/usr/bin/env bash
Blue='\033[0;34m' 
NC='\033[0m' # No Color (reset)

arg="$1"
set -e # exit on first error

GIT_ROOT=$(git rev-parse --show-toplevel)

ARCH_RAW=$(uname -m)
OS_RAW=$(uname -s)

# lowercase
ARCH="${ARCH_RAW,,}"
OS_NAME="${OS_RAW,,}" 

#rust compile target is named aarch64 not arm64
if [[ "$OS_NAME" == "linux" && "$ARCH" == "arm64" ]]; then
    TARGET_ARCH="aarch64"
else
    TARGET_ARCH="$ARCH"
fi

SYSTEM="$TARGET_ARCH-$OS_NAME"
DATABASE_URL=$(find "$GIT_ROOT" -name 'db.sqlite3' -print -quit)
# in the flask app the same default is specified if no env var is set >>  `app/__init__.py:42` 
DATABASE_URL_ENV=${DATABASE_URL:-"./instance/db.sqlite3"} 
ws_pid=""
flask_pid=""

cleanup() {
    if [[ -n "$flask_pid" ]]; then # 
        kill $flask_pid 2>/dev/null
        echo "Flask server stopped"
    fi
    if [[ -n "$ws_pid" ]]; then
        kill $ws_pid 2>/dev/null
        echo "Ws ws-server stopped"
    fi
    exit 0
}

trap cleanup SIGINT SIGTERM EXIT

if [[ "$arg" == "start" ]]; then
    if [[ -z "$DATABASE_URL" ]]; then
        echo "No Database named db.sqlite3 found please run  './run.sh reset'"
        exit 1
    fi
    echo "starting ws server"
    export DATABASE_URL="$DATABASE_URL_ENV"

    "$GIT_ROOT/ws-server/lfsc-$SYSTEM" &
    ws_pid=$!
    echo "Ws ws-server started (PID: $ws_pid)"

    flask run --debug &
    flask_pid=$! 
    echo "Flask server started (PID: $flask_pid)"

    echo -e "${BLUE}Servers running press CTRL+C to quit${NC}"
    wait
    exit 0
elif [[ "$arg" == "reset" ]]; then
    echo "resetting db starting ws server"
    mkdir -p ./instance
    flask drop-db
    flask init-db
    "$GIT_ROOT/ws-server/lfsc-$SYSTEM" &

    ws_pid=$!
    echo "Ws ws-server started (PID: $ws_pid)"

    flask run --debug &
    flask_pid=$!
    echo "Flask server started (PID: $flask_pid)"

    echo -e "${BLUE}Servers running press CTRL+C to quit${NC}"
    wait
    exit 0
fi

echo "command usage: ./run.sh start|reset"
exit 1
