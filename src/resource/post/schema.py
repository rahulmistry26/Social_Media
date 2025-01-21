from datetime import datetime
from pydantic import BaseModel


class Post(BaseModel):
    user_id:int  
    title:str
    caption:str
    # image_url:str
    created_at : datetime = datetime.utcnow()

# class DeletePost(BaseModel):
#     post_id:int

class UpdatePost(BaseModel):
    post_id:int
    title:str
    caption:str
    updated_at : datetime=datetime.utcnow() 

class GetPost(BaseModel):
    post_id:int
    user_id:int  
    title:str
    caption:str

class PostLikeSchema(BaseModel):
    post_id:int
    user_id:int

