from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    post_id = Column(String)
    title = Column(String)
    description = Column(String)
    date = Column(String)
    category = Column(String)
    date = Column(String)

    user_id = Column(String, ForeignKey("users.registered_user_id"))

    user = relationship("User", back_populates="posts")


    # Func to avoid the  field to field update into the controller function in routes
    def update( self, **kwargs ):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)