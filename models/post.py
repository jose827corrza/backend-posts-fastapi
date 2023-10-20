from database.database import Base
from sqlalchemy import Column, Integer, String

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    post_id = Column(String)
    title = Column(String)
    description = Column(String)
    date = Column(String)
    user_id = Column(String)
    category = Column(String)
    date = Column(String)

    # Func to avoid the  field to field update into the controller function in routes
    def update( self, **kwargs ):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)