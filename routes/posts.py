import uuid
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import List
from fastapi.responses import JSONResponse


from middlewares.jwt_bearer import JWTBearer
from schemas.post import Post
from database.database import SessionLocal
from models.post import Post as PostModel
from services.post import PostService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix='/tweets/v2',
    tags=['Posts']
)

@router.get('/posts', response_model=List[Post])
def get_all_posts():
    db = SessionLocal()
    return PostService(db).get_posts()

@router.get('/posts/{post_id}', 
            response_model=Post)
def get_post(post_id: str) -> Post:
    db = SessionLocal()
    result = PostService(db).get_post_by_post_id(post_id)
    return result
    

        
@router.get('/posts_by_category')
def get_posts_by_category(category: str):
    db = SessionLocal()
    return PostService(db).get_posts_by_category(category)
    # return db.query(PostModel).filter(PostModel.category == category).all()



@router.post('/posts', 
             response_model=Post, 
             dependencies=[Depends(JWTBearer())]
             )
def create_post(post: Post):
    db = SessionLocal()
    # new_post = PostModel(**post.dict()) # Easy mode, passing directly
    PostService(db).create_post(post)

    return JSONResponse(content={"message": "Post Created"})

@router.put('/posts/{post_id}', tags=['Posts'])
def update_post(post_id: str, post: Post):
    db = SessionLocal()
    PostService(db).update_post(post_id, post)
    return JSONResponse(content={"message": "Post updated"})
    

@router.delete('/posts/{post_id}', response_model=dict)
def delete_post(post_id: str) -> dict:
    db = SessionLocal()
    PostService(db).delete_post(post_id)
    return JSONResponse(status_code=200, content={"message": "The post was deleted", "post_id": post_id})
    