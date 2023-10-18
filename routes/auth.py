from fastapi import APIRouter
from fastapi.responses import JSONResponse

from auth.jwt_manager import create_token

from models.user import User

router = APIRouter(
    tags=['Auth']
)

@router.post('/login', response_model=dict())
def login(data: User) -> dict():
    # Emulates the existence of user in DB
    if data.email == "test@mail.com" and data.password =="test123":
        token: str = create_token(data.model_dump())
        return JSONResponse(content={"token": token})