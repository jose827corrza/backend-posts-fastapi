from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    # password: str

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

class UserCreate(UserBase):
    password: str