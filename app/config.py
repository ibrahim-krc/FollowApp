import os
from dotenv import load_dotenv

load_dotenv()


INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")


CHECK_USERNAME = "isim"
SCRAPE_COUNT = 50
DURATION = 500


SETTINGS_PATH = "session.json"
SUCCESSFUL_REQUESTS_FILE = "basarili_istekler.txt"
NAMES_FILE = "isimler.txt"
