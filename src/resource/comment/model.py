from database import Base
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class CommentModel(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id',ondelete='cascade'))
    post = relationship("PostModel")
    user_id = Column(Integer,ForeignKey("user.id",ondelete='cascade'))
    user = relationship("UserModel")
    text = Column(String,index=True)
    # likes = Column(Integer)
    # dislikes = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow())


class CommentLike(Base):
    __tablename__ = "comment_likes"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer,ForeignKey("posts.id",ondelete='cascade'))
    post = relationship("PostModel")
    user_id = Column(Integer,ForeignKey("user.id",ondelete='cascade'))
    user = relationship("UserModel")
    comment_id = Column(Integer, ForeignKey("comments.id",ondelete='cascade'))
    comment = relationship("CommentModel")
    created_at = Column(DateTime, default=datetime.utcnow)
    # comment = relationship("Comments", back_populates="likes")
