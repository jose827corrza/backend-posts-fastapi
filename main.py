from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import List
import uuid

# Project
import db
from dtos.post import PostDto
from models.post import Post
from models.user import User
from models.jwt import JWTBearer
from auth.jwt_manager import create_token


# Load the .env
load_dotenv()
test = db.data

app = FastAPI(
    title= 'Tweets FastAPI',
    description='API that emulates the func of X',
    version='0.0.1',
    contact={
        "name": "joseDev",
        "url": 'https://github.com/jose827corrza',
        "email": 'jose.corrzadeveloper@gmail.com'
    }
)


@app.get('/',tags=['Home'])
def hello():
    return 'Hello Tweets!'

@app.get('/posts',tags=['Posts'], response_model=List[Post])
def get_posts() -> List[Post]:
    return test

@app.get('/posts/{id}',tags=["Posts"])
def get_post(id: str) -> Post:
    posts = test
    for post in posts:
        if post['post_id'] == id:
            return post
        else:
            raise HTTPException(404, "Post not found")
        
@app.get('/posts/', response_model=Post, tags=['Posts'])
def get_posts_by_category(category: str):
    posts = []
    for post in test:
        categories =  post['categories']
        for cat in categories:
            if cat == category:
                posts.append(post)
    return posts

@app.post('/posts', response_model=Post, tags=['Posts'], dependencies=[Depends(JWTBearer)])
def create_post(post: Post):
    # test.append({
    #     "id": 4,
    #     "post_id": str(uuid.uuid4()),
    #     "title": post['title'],
    #     "description": post['description'],
    #     "date": post['date'],
    #     "user_id": post['user_id'],
    #     "categories": post['categories'],
    # })
    # post['post_id'] = str(uuid.uuid4())
    post.post_id = str(uuid.uuid4())
    print(post)
    test.append(post)
    return post

@app.put('/posts/{post_id}', tags=['Posts'])
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

@app.delete('/posts/{post_id}', response_model=dict)
def delete_post(post_id: str) -> dict:
    for item in test:
        if item['post_id'] == post_id:
            test.remove(item)
            return JSONResponse(content={"message": "post deleted"})
        
@app.post('/login', tags=['Auth'])
def login(data: User):
    # Emulates the existence of user in DB
    if data.email == "test@mail.com" and data.password =="test123":
        token: str = create_token(data.model_dump())
        return token