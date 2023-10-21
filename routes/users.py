from fastapi import APIRouter
from fastapi.responses import JSONResponse

from schemas.user import UserCreate, UserTable
from database.database import SessionLocal
from schemas.utils import SuccessResponse
from services.user import UserService

router = APIRouter(
    prefix='/users/v1',
    tags=['Users'],
)

@router.post(
    path='/user',
    response_model=SuccessResponse
)
def create_user(user: UserCreate) -> SuccessResponse:
    db = SessionLocal()
    UserService(db).create_user(user)
    return JSONResponse(content={"message": "User Created"})

@router.get(
    path='/users/{user_id}',
    response_model=UserTable,
    description="Thid method will return all the posts that the users has already posted"
)
def get_user_info(user_id: str) -> UserTable | None:
    db = SessionLocal()
    result = UserService(db).get_user_info(user_id)
    return result