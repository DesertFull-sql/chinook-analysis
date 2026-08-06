from pathlib import Path

DB_URI = "postgresql+psycopg2://postgres:1221@localhost:5432/chinook"
IMAGES_DIR = Path(__file__).resolve().parent.parent / 'images'