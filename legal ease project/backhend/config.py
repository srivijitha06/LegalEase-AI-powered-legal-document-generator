import os

from dotenv import load_dotenv

load_dotenv()

APP_NAME = "LegalEase"
APP_VERSION = "1.0.0"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash",
)

FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "http://localhost:8501",
)

MAX_TEXT_LENGTH = 30000