from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException
import uuid

from models.post import Post as PostModel
from schemas.post import Post

class PostService():
    def __init__(self, db: sessionmaker) -> None:
        self.db = db

    def get_posts(self) -> list[Post]:
        return self.db.query(PostModel).all()
    
    def get_post_by_post_id(self, post_id: str) -> Post | None:
        result = self.db.query(PostModel).filter(PostModel.post_id == post_id).first()
        if result == None:
            raise HTTPException(404, "Post not found")
        else:
            return result

    def get_posts_by_category(self, category: str):  
        return self.db.query(PostModel).filter(PostModel.category == category.capitalize()).all()

    def create_post(self, post: Post):
        try:
            new_post = PostModel(
            title = post.title.capitalize(),
            description = post.description,
            post_id = str(uuid.uuid4()),
            user_id = post.user_id,
            date = post.date,
            category = post.category.capitalize()
            )
            self.db.add(new_post)
            self.db.commit()
            return
        except Exception as e:
            raise HTTPException(500, "Internal server error")
        
    def update_post(self, post_id: str, post: Post):
        try:
            result = self.get_post_by_post_id(post_id)
            if not result:
                raise HTTPException(404, "Post not found")
            else:
                result.title = post.title
                result.description = post.description
                result.category = post.category
                self.db.commit()
                return
        except Exception:
            raise HTTPException(400, "Bad request")
        
    def delete_post(self, post_id: str):
        result = self.get_post_by_post_id(post_id)
        self.db.delete(result)
        self.db.commit()
        return