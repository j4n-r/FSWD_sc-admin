#!/usr/bin/env bash
BLUE='\033[0;34m' 
NC='\033[0m' # No Color (reset)

arg="$1"
set -e # exit on first error

GIT_ROOT=$(git rev-parse --show-toplevel)

ARCH=$(uname -m)
OS=$(uname -s)

SYSTEM=""

if [[ "$OS" == "Darwin" && "$ARCH" == "arm64" ]]; then
    SYSTEM="aarch64-darwin"  #rust compile target is named aarch64-apple-darwin not arm64-...
elif [[ "$OS" == "Linux" && "$ARCH" == "x86_64" ]]; then
    SYSTEM="x86_64-linux"
else
    echo "Only aarch64-Darwin and x86_64-Linux is supported you have: $ARCH-$OS"
    exit 1
fi

DATABASE_URL=$(find "$GIT_ROOT" -name 'db.sqlite3' -print -quit)
# in the flask app the same default is specified if no env var is set >>  `app/__init__.py:42`
DATABASE_URL_ENV=${DATABASE_URL:-"./instance/db.sqlite3"} 
export DATABASE_URL="$DATABASE_URL_ENV"
ws_pid=""
flask_pid=""

cleanup() {
    if [[ -n "$flask_pid" ]]; then 
        kill $flask_pid 2>/dev/null
        echo "Flask server stopped"
    fi
    if [[ -n "$ws_pid" ]]; then
        kill $ws_pid 2>/dev/null
        echo "Ws ws-server stopped"
    fi
    exit 0
}

activate_venv() {
    if [[ ! -d "$GIT_ROOT/venv" ]]; then
        echo "Please initialize python venv as $GIT_ROOT/venv directory"
        echo "run:"
        echo "python -m venv venv/"
        echo "pip install -r requirements.txt"
    else
        source "$GIT_ROOT/venv"
    fi
}

start_servers() {
    "$GIT_ROOT/ws-server/lfsc-$SYSTEM" &

    ws_pid=$!
    echo "Ws ws-server started (PID: $ws_pid)"

    flask run --debug &
    flask_pid=$!
    echo "Flask server started (PID: $flask_pid)"

    echo -e "${BLUE}Servers started press CTRL+C to quit${NC}"
    wait
    exit 0
}

trap cleanup SIGINT SIGTERM EXIT

if [[ "$arg" == "start" ]]; then
    if [[ -z "$DATABASE_URL" ]]; then
        echo "No Database named db.sqlite3 found please run  './run.sh reset'"
        exit 1
    fi
    start_servers

elif [[ "$arg" == "reset" ]]; then
    echo "resetting db starting ws server"
    mkdir -p ./instance
    flask drop-db
    flask init-db
    start_servers
fi

echo "command usage: ./run.sh start|reset"
exit 1
