import uuid
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from fastapi.responses import JSONResponse
from models.jwt import JWTBearer

from models.post import Post, PostIn, PostOut
import db

test = db.data

router = APIRouter(
    prefix='/posts/v2',
    tags=['Posts']
)

@router.get('/', response_model=List[Post])
def get_posts() -> List[Post]:
    return test

@router.get('/posts/{id}')
def get_post(id: str) -> Post:
    posts = test
    for post in posts:
        if post['post_id'] == id:
            return post
        else:
            raise HTTPException(404, "Post not found")
        
@router.get('/', response_model=Post)
def get_posts_by_category(category: str):
    posts = []
    for post in test:
        categories =  post['categories']
        for cat in categories:
            if cat == category:
                posts.append(post)
    return posts


@router.post('/posts', response_model=Post, dependencies=[Depends(JWTBearer)])
def create_post(post: Post):
    post.post_id = str(uuid.uuid4())
    print(post)
    test.append(post)
    return post

@router.put('/posts/{post_id}', tags=['Posts'])
def update_post(post_id: str, post: Post):

    for postItem in test:
        print(postItem)
        if postItem['post_id'] == post_id:
            postItem['title'] = post.title
            postItem['description'] = post.description
            postItem['date'] = post.date
            postItem['categories'] = post.categories
            return postItem
    if post:
        raise HTTPException(404, "Post not found")
    

@router.delete('/posts/{post_id}', response_model=dict)
def delete_post(post_id: str) -> dict:
    for item in test:
        if item['post_id'] == post_id:
            test.remove(item)
            return JSONResponse(content={"message": "post deleted"})