from pydantic import BaseModel

class SuccessResponse(BaseModel):
    message: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "Your task was successfully performed"
                }
            ]
        }
    }

class TokenAccess(BaseModel):
    token: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAbWFpbC5jb20ifQ.O5jF3X8UFOqO35LjEC5BXMKmE3gN13RClc1gQgQzgEA"
                }
            ]
        }
    }