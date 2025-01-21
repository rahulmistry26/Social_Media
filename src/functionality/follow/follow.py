from database import get_db
from datetime import datetime
from sqlalchemy.orm import Session
from src.resource.follow.model import FollowModel
from src.resource.user.model import UserModel
from src.resource.follow.schema import FollowRequest,UnfollowUser
from fastapi import Depends ,HTTPException


def create_follow(follows:FollowRequest,db:Session=Depends(get_db)):
    try:
        # breakpoint()

        user_db =db.query(UserModel).filter(UserModel.id==follows.user_id).first()
        if not user_db:
            raise HTTPException(status_code=404,detail="User not found")
        
        unfollow_db =db.query(UserModel).filter(UserModel.id==follows.follower_id).first()
        if not unfollow_db:
            raise HTTPException(status_code=404,detail="User not found")
        db_follow = FollowModel(user_id=follows.user_id,
                                follower_id=follows.follower_id,
                                created_at=datetime.utcnow())
        db.add(db_follow)
        
        user_db.follow_count=(user_db.follow_count or 0) +1
        db.commit()
        db.refresh(db_follow)

        
        return{
            "Success":True,
            "Message":"User followed"
        }
    except :
        raise HTTPException(status_code=500,detail="not inserted")

def remove_follow(unfollow:UnfollowUser,db:Session=Depends(get_db)):
    try:
        # breakpoint()
        user_db =db.query(UserModel).filter(UserModel.id==unfollow.user_id).first()
        if not user_db:
            raise HTTPException(status_code=404,detail="User not found")
        
        unfollow_db =db.query(UserModel).filter(UserModel.id==unfollow.follower_id).first()
        if not unfollow_db:
            raise HTTPException(status_code=404,detail="User not found")
    
        db.delete(unfollow_db)
        db.commit()

        user_db.follow_count=(user_db.follow_count or 0) -1
        db.commit()
        # db.refresh()

        db.refresh(unfollow_db)
       
        return{
            "Success":True,
            "Message":"User Unfollow"
        }
    except Exception as e:
        raise HTTPException(status_code=500,detail="not removed follower")
    
def get_follower_count(user_id: int, db: Session = Depends(get_db)):
    try:
        follower_count = db.query(FollowModel).filter(
            FollowModel.followed_id == user_id
        ).count()
        
        return {
            "success": True,
            "user_id": follower_count.user_id,
            "follower_count": follower_count
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error getting follower count")

def get_following_count(user_id: int, db: Session = Depends(get_db)):
    try:
        following_count = db.query(FollowModel).filter(
            FollowModel.follower_id == user_id
        ).count()
        
        return {
            "success": True,
            "user_id": user_id,
            "following_count": following_count
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error getting following count")
