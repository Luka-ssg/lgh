#!/bin/bash

# Start FastAPI backend
echo "Starting FastAPI Backend..."
poetry run fastapi dev /Users/lukamindek/Desktop/learning-github/learning_github/src/api/main.py &

# Store the FastAPI backend process ID
BACKEND_PID=$!

# Wait for FastAPI to start (optional, to ensure backend starts before frontend)
sleep 2

# Start Streamlit frontend
echo "Starting Streamlit Frontend..."
poetry run streamlit run learning_github/src/streamlit/main.py
# Store the Streamlit frontend process ID
FRONTEND_PID=$!

# Function to handle script termination
function shutdown {
    echo "Shutting down FastAPI Backend and Streamlit Frontend..."
    kill $BACKEND_PID
    kill $FRONTEND_PID
}

# Trap CTRL+C (SIGINT) and call the shutdown function
trap shutdown SIGINT

# Wait for the processes to finish (keep the script running)
wait $BACKEND_PID
wait $FRONTEND_PID
