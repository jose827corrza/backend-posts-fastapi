from pydantic import BaseModel
from typing import Tuple

class PostDto(BaseModel):
    title: str
    description: str
    date: str
    user_id: str
    categories: list[str]