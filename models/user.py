from database.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True)
    email = Column(String)
    password = Column(String)
    registered_user_id = Column(String, unique=True)

    posts = relationship("Post",back_populates="user")
