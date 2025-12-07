#!/bin/bash

# Budget Buddy - Run Script

echo "Starting Budget Buddy..."
echo "========================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the application
echo "Starting Flask application..."
echo "Access the app at: http://127.0.0.1:5000"
python app.py
