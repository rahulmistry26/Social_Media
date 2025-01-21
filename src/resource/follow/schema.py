from datetime import datetime
from pydantic import BaseModel

class FollowRequest(BaseModel):
    user_id: int
    follower_id: int
    

class UnfollowUser(BaseModel):
    user_id: int
    follower_id: int