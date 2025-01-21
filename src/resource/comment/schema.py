from datetime import datetime
from pydantic import BaseModel


class CommentSchema(BaseModel):
    post_id:int
    user_id:int
    text:str
    created_at:datetime=datetime.utcnow()


class CommentLikeOrDislike(BaseModel):
    comment_id:int
    post_id:int
    user_id:int

