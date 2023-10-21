from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import uuid

from auth.jwt_manager import create_token
from schemas.user import UserCreate, UserTable
from models.user import User as UserModel
from utils.hashing import hash_password, check_password

class UserService():
    def __init__(self, db: sessionmaker) -> None:
        self.db = db

    def create_user(self, user: UserCreate):
        try:
            hashed_password = hash_password(user.password)
            new_user = UserModel(
            email = user.email,
            password = hashed_password.decode(),
            registered_user_id = str(uuid.uuid4())
            )
            self.db.add(new_user)
            self.db.commit()
            return
        except Exception as e:
            raise HTTPException(400, f"Internal server error: {e}")
        


    def get_user_info(self, user_id: str) -> UserTable:
        result = self.db.query(UserModel).filter(UserModel.registered_user_id == user_id).first()
        if result == None:
                raise HTTPException(404, "Post not found")
        else:
            return result
        
    
    def get_user_credentials(self, email: str, password: str):
        result =  self.db.query(UserModel).filter(UserModel.email == email).first()
        if result == None:
            raise HTTPException(404, "Check your credentials")
        else:
            if check_password(password, result.password):
                token: str = create_token({"email":result.email})
                return token
            else:
                raise HTTPException(401, "Check your credentials")