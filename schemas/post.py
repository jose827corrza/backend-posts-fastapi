from pydantic import BaseModel, Field
from typing import Optional

class Post(BaseModel):
    id: Optional[int] = None
    post_id: Optional[str] = None
    title: str = Field(max_length=60)
    description: str = Field(max_length=100, min_length=5)
    date: str
    user_id: str
    category: str
    # categories: list[str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "My first Post",
                    "description": "Description of the first Post",
                    "date": "2023-10-15",
                    "user_id": "aaa-bbb-ccc-ddd",
                    "category": "IoT"
                    # "categories": [
                    #     "Math",
                    #     "Physics"
                    # ]
                }
            ]
        }
    }

class PostIn(BaseModel):
    title: str
    description: str
    date: str
    user_id: str
    categories: list[str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "My first Post",
                    "description": "Description of the first Post",
                    "date": "2023-10-15",
                    "user_id": "aaa-bbb-ccc-ddd",
                    "categories": [
                        "Math",
                        "Physics"
                    ]
                }
            ]
        }
    }

class PostOut(BaseModel):
    id: Optional[int] = None
    post_id: Optional[str] = None
    title: str
    description: str
    date: str
    user_id: str
    categories: list[str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "My first Post",
                    "description": "Description of the first Post",
                    "date": "2023-10-15",
                    "user_id": "aaa-bbb-ccc-ddd",
                    "categories": [
                        "Math",
                        "Physics"
                    ]
                }
            ]
        }
    }