from database import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class PostModel(Base):
    __tablename__ ="posts"
    id = Column(Integer,primary_key=True)
    user_id =Column(Integer,ForeignKey('user.id'))
    user = relationship("UserModel")
    title = Column(String(500))
    caption = Column(String(500))
    
    image_url=Column(String(1000))
    created_at = Column(DateTime,default=datetime.utcnow())
    updated_at = Column(DateTime,default=datetime.utcnow())  
    is_deleted =Column(Boolean(),default=False)
   

class PostLike(Base):
    __tablename__ ="post_like"
    id = Column(Integer,primary_key=True)
    user_id =Column(Integer,ForeignKey('user.id'))
    user = relationship("UserModel")
    post_id =Column(Integer,ForeignKey('posts.id'))
    post = relationship("PostModel")
    created_at = Column(DateTime,default=datetime.utcnow())

