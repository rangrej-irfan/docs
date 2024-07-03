#!/bin/bash

# Variables
IMAGE="python:latest"
CONTAINER_NAME="discussion_leaderboard"
SRC_DIR=$(pwd)/src
PORT=8501

# Ensure the src directory exists
if [ ! -d "$SRC_DIR" ]; then
  echo "The src directory does not exist in the current directory. Please create it and add your Python code and properties file."
  exit 1
fi

# Build Docker command
DOCKER_CMD="docker run -d --name $CONTAINER_NAME -v $SRC_DIR:/app -w /app -p $PORT:8501 $IMAGE bash -c 'pip install streamlit matplotlib configparser && cd /app && streamlit run github_discussion_leaderboard.py'"

# Pull the latest Python image
echo "Pulling the latest Python image..."
docker pull $IMAGE

# Stop and remove the container if it is already running
echo "Stopping the existing Docker container..."
docker stop $CONTAINER_NAME 2>/dev/null
echo "Removing the existing Docker container..."
docker rm $CONTAINER_NAME 2>/dev/null

# Run the container
echo "Running the Docker container..."
eval $DOCKER_CMD

# Check if the container is running
if [ $(docker ps -q -f name=$CONTAINER_NAME) ]; then
  echo "The Docker container is running in the background."
  echo "You can access the application at http://localhost:$PORT"
else
  echo "Failed to start the Docker container."
  exit 1
fi
