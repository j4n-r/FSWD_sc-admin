#!/usr/bin/env bash
BLUE='\033[0;34m' 
NC='\033[0m' # No Color (reset)

arg="$1"
venv="$2" # only option is novenv 
set -e # exit on first error

GIT_ROOT=$(git rev-parse --show-toplevel)

ARCH=$(uname -m)
OS=$(uname -s)

SYSTEM=""

if [[ "$OS" == "Darwin" && "$ARCH" == "arm64" ]]; then
    SYSTEM="aarch64-darwin"  #rust compile target is named aarch64-apple-darwin not arm64-...
elif [[ "$OS" == "Darwin" && "$ARCH" == "x86_64" ]]; then
    SYSTEM="x86_64-darwin"
elif [[ "$OS" == "Linux" && "$ARCH" == "x86_64" ]]; then
    SYSTEM="x86_64-linux"
else
    echo "Only aarch64-Darwin, x86_64-darwin and x86_64-Linux is supported you have: $ARCH-$OS"
    exit 1
fi

DATABASE_URL=$(find "$GIT_ROOT" -name 'db.sqlite3' -print -quit)
# in the flask app the same default is specified if no env var is set >>  `app/__init__.py:42`
DATABASE_URL_ENV=${DATABASE_URL:-"./instance/db.sqlite3"} 
export DATABASE_URL="$DATABASE_URL_ENV"
ws_pid=""
flask_pid=""


# Improved cleanup function
cleanup() {
    echo "Shutting down servers..."
    
    # Function to kill a process with timeout
    kill_with_timeout() {
        local pid=$1
        local name=$2
        local timeout=5
        
        if [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null; then
            echo "Stopping $name (PID: $pid)..."
            kill "$pid" 2>/dev/null || true
            
            # Wait for graceful shutdown
            local count=0
            while kill -0 "$pid" 2>/dev/null && [[ $count -lt $timeout ]]; do
                sleep 1
                ((count++))
            done
            
            # Force kill if still running
            if kill -0 "$pid" 2>/dev/null; then
                echo "Force killing $name..."
                kill -9 "$pid" 2>/dev/null || true
                sleep 1
            fi
            
            if ! kill -0 "$pid" 2>/dev/null; then
                echo "$name stopped"
            else
                echo "Warning: $name may still be running"
            fi
        fi
    }
    
    kill_with_timeout "$flask_pid" "Flask server"
    kill_with_timeout "$ws_pid" "Ws ws-server"
    
    exit 0
}

activate_venv() {
    if [[ ! -d "$GIT_ROOT/venv" ]]; then
        echo "Please initialize python venv as $GIT_ROOT/venv directory"
        echo "run:"
        echo "python -m venv venv/"
        echo "source $GIT_ROOT/venv/bin/activate"
        echo "pip install -r requirements.txt"
        exit 1
    else
        source "$GIT_ROOT/venv/bin/activate"
    fi
}

start_servers() {
    "$GIT_ROOT/ws-server/core-$SYSTEM" &
    ws_pid=$!
    echo "Ws ws-server started (PID: $ws_pid)"

    flask run --debug &
    flask_pid=$!
    echo "Flask server started (PID: $flask_pid)"

    echo -e "${BLUE}Servers started press CTRL+C to quit${NC}"
    
    # Wait for both processes
    while kill -0 "$ws_pid" 2>/dev/null && kill -0 "$flask_pid" 2>/dev/null; do
        sleep 1
    done
    
    exit 0
}

# Set trap for cleanup
trap cleanup SIGINT SIGTERM EXIT

if [[ "$venv" != "novenv" ]]; then
    activate_venv
fi

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
echo "use ./run.sh start|reset novenv if venv is not used for dependencies"
exit 1
