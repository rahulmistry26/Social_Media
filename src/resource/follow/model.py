from sqlalchemy import Column, DateTime, ForeignKey, Integer
from database import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class FollowModel(Base):
    __tablename__ = "followers"
    id = Column(Integer,primary_key=True)
    
    user_id = Column(Integer,ForeignKey("user.id"))

    # user = relationship("UserModel") 
    follower_id = Column(Integer,ForeignKey("user.id"))
    # user = relationship("UserModel")
    created_at = Column(DateTime, default=datetime.utcnow())

    # follower =relationship("user", foreign_keys=[follower_id] ,back_populates="following")
    # followed =relationship("user",foreign_keys=[followed_id],back_populates="followers")







