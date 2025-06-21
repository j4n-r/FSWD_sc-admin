FROM python:3.11-slim

RUN apt-get update && apt-get clean

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt && \
    mkdir instance

COPY . /app

EXPOSE 5000 8080

# Make ws-server executable
RUN chmod +x /app/ws-server/core-x86_64-linux

# Set environment variables that the ws-server might need
ENV FLASK_APP=app
ENV DATABASE_URL="/app/instance/db.sqlite3"

# Initialize DB and start servers
CMD flask init-db && \
    echo "Starting WebSocket server..." && \
    ./ws-server/core-x86_64-linux & \
    echo "Starting Flask server..." && \
    flask run --host=0.0.0.0
