from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import List
from fastapi.responses import JSONResponse


from middlewares.jwt_bearer import JWTBearer
from schemas.post import PostTable, PostCreate
from database.database import SessionLocal
from schemas.utils import SuccessResponse
from services.post import PostService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix='/tweets/v2',
    tags=['Posts v2']
)

@router.get(
        path='/posts', 
        response_model=List[PostTable]
        )
def get_all_posts():
    db = SessionLocal()
    return PostService(db).get_posts()

@router.get(
        path='/posts/{post_id}', 
        response_model=PostTable)
def get_post(post_id: str):
    db = SessionLocal()
    result = PostService(db).get_post_by_post_id(post_id)
    return result
    

        
@router.get(
        path='/posts_by_category',
        response_model=List[PostTable]
        )
def get_posts_by_category(category: str):
    db = SessionLocal()
    return PostService(db).get_posts_by_category(category)
    # return db.query(PostModel).filter(PostModel.category == category).all()



@router.post(
        path='/posts', 
        response_model=SuccessResponse, 
        dependencies=[Depends(JWTBearer())]
             )
def create_post(post: PostCreate):
    db = SessionLocal()
    # new_post = PostModel(**post.dict()) # Easy mode, passing directly
    PostService(db).create_post(post)
    return JSONResponse(content={"message": "Post Created"})

@router.put(
        path='/posts/{post_id}',
        response_model=SuccessResponse,
        deprecated=True
        )
def update_post(post_id: str, post: PostCreate):
    db = SessionLocal()
    PostService(db).update_post(post_id, post)
    return JSONResponse(content={"message": "Post updated"})
    

@router.delete(
        path='/posts/{post_id}', 
        response_model=SuccessResponse
        )
def delete_post(post_id: str) -> dict:
    db = SessionLocal()
    PostService(db).delete_post(post_id)
    return JSONResponse(status_code=200, content={"message": "The post was deleted", "post_id": post_id})
    