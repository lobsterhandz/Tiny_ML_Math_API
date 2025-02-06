#!/bin/bash

echo "🚀 Starting TinyML Flask API..."

# Activate virtual environment if exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run database migration script (if needed)
python scripts/init_db.py

# Start the Flask server
exec python app.py
