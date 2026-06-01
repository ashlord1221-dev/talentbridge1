import sys, os

# Add project root to path so app.py can be imported
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set DB and upload paths to /tmp (Vercel writable directory)
os.environ.setdefault("DB_PATH", "/tmp/talentbridge.db")
os.environ.setdefault("UPLOAD_FOLDER", "/tmp/uploads")
os.makedirs("/tmp/uploads", exist_ok=True)

# Import the Flask app — init_db() runs automatically on import
from app import app

# Vercel expects a variable named `app`
# This file is the serverless handler
