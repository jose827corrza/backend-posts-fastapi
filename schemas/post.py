from pydantic import BaseModel




# Basic
class PostBase(BaseModel):
    title: str
    description: str
    category: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "My first Post",
                    "description": "Description of the first Post",
                    "category ": "IoT"
                }
            ]
        }
    }

# Used when creating
class PostCreate(PostBase):
    user_id: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "My first Post",
                    "description": "Description of the first Post",
                    "user_id": "95be9709-585b-4b74-9345-a3f80091e719",
                    "category": "IoT"
                }
            ]
        }
    }  

# Used when show DB data
class PostTable(PostBase):
    id: int
    date: str
    user_id: str
    post_id: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "My first Post",
                    "description": "Description of the first Post",
                    "user_id": "95be9709-585b-4b74-9345-a3f80091e719",
                    "category": "IoT",
                    "post_id": "be00325c-b2b6-4340-8b2e-5a70e2ea7b1a",
                    "date": "Friday 2023 10 20 18:00"
                }
            ]
        }
    }