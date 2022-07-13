import motor.motor_asyncio

from beanie import init_beanie

from src.config.config import DB_URL
from src.models.post import Post

client = motor.motor_asyncio.AsyncIOMotorClient(
    DB_URL,
    uuidRepresentation='standard'
)
db = client['instaclone']
