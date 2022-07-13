from typing import Optional
from beanie import Document
from pydantic.fields import Field
from datetime import datetime


class Post(Document):
    image_url: str = Field(...)
    caption: Optional[str]
    timestamp: datetime = datetime.now()

    class Settings:
        name = 'posts'

    class Config:
        schema_extra = {
            'example': {
                'image_url': 'https://images.pexels.com/photos/3495870/pexels-photo-3495870.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
                'caption': ''
            }
        }
