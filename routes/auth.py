from fastapi import APIRouter
from fastapi.responses import JSONResponse

from auth.jwt_manager import create_token
from schemas.user import UserCreate
from schemas.utils import TokenAccess
from services.user import UserService
from database.database import SessionLocal

router = APIRouter(
    tags=['Auth']
)

@router.post('/login', response_model=TokenAccess)
def login(data: UserCreate):
    db = SessionLocal()
    token = UserService(db).get_user_credentials(data.email, data.password)
    return JSONResponse(content={"token": token})
    # if UserService(db).get_user_credentials(data.email, data.password):
    #     token: str = create_token({"email":data.email})
    #     return JSONResponse(content={"token": token})
