from pydantic import BaseModel

from schemas.post import PostTable

class UserBase(BaseModel):
    email: str
    # password: str

    

class UserCreate(UserBase):
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "test@mail.com",
                    "password": "test123"
                }
            ]
        }
    }

class UserTable(UserBase):
    id: int
    registered_user_id: str
    posts: list[PostTable] = []

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "email": "test@mail.com",
                    "registered_user_id": "95be9709-585b-4b74-9345-a3f80091e719",
                    "posts": [
                        {
                            "title": "My first post",
                            "description": "Description of the first Post",
                            "category": "Iot",
                            "id": 1,
                            "date": "Fri Oct 20 17:21:32 2023",
                            "user_id": "95be9709-585b-4b74-9345-a3f80091e719",
                            "post_id": "be00325c-b2b6-4340-8b2e-5a70e2ea7b1a"
                        }
                    ]
                }
            ]
        }
    }