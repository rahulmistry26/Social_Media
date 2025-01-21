
from database import Base   
from sqlalchemy import Column, DateTime, Integer, String,Boolean
from sqlalchemy.orm import relationship
from datetime import datetime


class UserModel(Base):
    __tablename__ = "user"
    id =Column(Integer,primary_key=True)
    first_name=Column(String(500))
    last_name=Column(String(500))
    email=Column(String(500))
    password=Column(String(500))
    # phone_number=Column(Integer)
    follow_count =Column(Integer)
    created_at=Column(DateTime,default=datetime.utcnow())
    updated_at=Column(DateTime,default=datetime.utcnow())
    is_active =Column(Boolean, default=True)
    is_verified=Column(Boolean,default=False)
    is_deleted=Column(Boolean,default=False)
    # relationship = relationship('Realtionship',back_populates='user')

