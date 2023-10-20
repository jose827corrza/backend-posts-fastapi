import uuid
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import List

from fastapi.responses import JSONResponse
from middlewares.jwt_bearer import JWTBearer

from schemas.post import Post


from database.database import SessionLocal
from models.post import Post as PostModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix='/tweets/v2',
    tags=['Posts']
)

@router.get('/posts', response_model=List[Post])
def get_all_posts():
    db = SessionLocal()
    return db.query(PostModel).all()

@router.get('/posts/{post_id}', 
            response_model=Post)
def get_post(post_id: str) -> Post:
    db = SessionLocal()
    result = db.query(PostModel).filter(PostModel.post_id == post_id).first()
    if result == None:
        raise HTTPException(404, "Post not found")
    else:
        return result

        
@router.get('/posts_by_category', response_model=Post)
def get_posts_by_category(category: str):
    db = SessionLocal()
    return db.query(PostModel).filter(PostModel.category == category).all()



@router.post('/posts', 
             response_model=Post, 
             dependencies=[Depends(JWTBearer())]
             )
def create_post(post: Post):
    db = SessionLocal()
    # new_post = PostModel(**post.dict()) # Easy mode, passing directly
    new_post = PostModel(
        title = post.title,
        description = post.description,
        post_id = str(uuid.uuid4()),
        user_id = post.user_id,
        date = post.date,
        category = post.category
    )
    db.add(new_post)
    db.commit()
    return JSONResponse(content={"message": "Post Created"})

@router.put('/posts/{post_id}', tags=['Posts'])
def update_post(post_id: str, post: Post):
    db = SessionLocal()
    result = db.query(PostModel).filter(PostModel.post_id == post_id).first()
    if not result:
        raise HTTPException(404, "Post not found")
    else:
        result.title = post.title
        result.description = post.description
        result.category = post.category
        db.commit()
    

@router.delete('/posts/{post_id}', response_model=dict)
def delete_post(post_id: str) -> dict:
    db = SessionLocal()
    result = db.query(PostModel).filter(PostModel.post_id == post_id).first()
    if not result:
        raise HTTPException(404, "Post not found")
    else:
        db.delete(result)
        return JSONResponse(status_code=200, content={"message": "The post was deleted", "data": result})