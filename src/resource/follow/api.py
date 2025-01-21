from fastapi import HTTPException,APIRouter,Depends
from src.functionality.follow.follow import create_follow,remove_follow,get_follower_count
from src.resource.follow.schema import FollowRequest,UnfollowUser
from sqlalchemy.orm import Session
from database import get_db

user_follow =APIRouter()

@user_follow.post("/create-follow")
def use_follows(follows:FollowRequest,db:Session=Depends(get_db)):
    try:
        fl =create_follow(follows=follows,db=db)
        return fl
    except Exception as e:
        return HTTPException(status_code=500,detail=str(e))

@user_follow.delete("/remove-follow")
def re_follow(unfollow:UnfollowUser,db:Session=Depends(get_db)):
    try:
        re = remove_follow(unfollow=unfollow,db=db)
        return re
    except Exception as e:
        return HTTPException(status_code=500,detail=str(e))
    
@user_follow.get("/follow-count")
def follow_ct(unfollow:UnfollowUser,db:Session=Depends(get_db)):
    try:
        fc =get_follower_count(unfollow=unfollow,db=db)
        return fc
    except Exception as e:
        return HTTPException(status_code=500,detail=str(e))