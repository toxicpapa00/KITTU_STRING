from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","28284695"))
API_HASH = getenv("API_HASH","2fedf2c683513b853cba01854a15d12b")

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID","8299512910"))

MONGO_DB_URI = getenv("mongodb+srv://Toxicbots:TOXIC0000@cluster0.u5sllsx.mongodb.net/?appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN","KITTUU_UPDATES")
