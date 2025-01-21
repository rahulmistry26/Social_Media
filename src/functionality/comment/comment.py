from database import get_db 
from datetime import datetime
from sqlalchemy.orm import Session
from src.resource.user.model import UserModel
from src.resource.post.model import PostModel
from fastapi import Depends, HTTPException
from src.resource.comment.model import CommentModel,CommentLike
from src.resource.comment.schema  import CommentSchema,CommentLikeOrDislike

def create_comment(comments:CommentSchema,db:Session=Depends(get_db)):

    db_comments = CommentModel(
        user_id= comments.user_id,
        post_id= comments.post_id,
        text = comments.text
    )
    db.add(db_comments)
    db.commit()
    db.refresh(db_comments)


    return{
        "Status":"Success",
        "Message":"Comment Created Successfully",
        "id":db_comments.id,
        "user_id":db_comments.user_id,
        "post_id":db_comments.post_id,
        "created_at":db_comments.created_at
        
    }

def delete_comment(comment_id:CommentSchema,db:Session=Depends(get_db)):

    db_comment = db.query(CommentModel).filter(CommentModel.id==comment_id).first()

    if not db_comment:
        raise HTTPException(status_code=404,detail="Comment not found")
    
    db.delete(db_comment)
    db.commit()
    return{
        "Staus":"Success",
        "Message":"Comment deleted successfully",
        "Deleted_Comment_id":comment_id
    }

def read_all_comment(db:Session=Depends(get_db)):
    comments = db.query(CommentModel).all()
    if not comments:
        raise HTTPException(status_code=404,detail="No comment found")

    return{
        "Status":"Success",
        "Message":"Comment Found Successfully",
        "Data":[{
            "comment_id":CommentModel.id,
            "text":CommentModel.text,
            "created_at":CommentModel.created_at
        } for CommentModel in comments
        ]
    }
# def like_or_dislkie_comments(comment_id:int,like:CommentLikeOrDislike,db:Session=Depends(get_db)):
    

#      comments = db.query(CommentModel).filter(CommentModel.id==comment_id).first()
#      if not comments:
#          raise HTTPException(status_code=404,detail="Comment Not Found")
     
#     #  if reaction.action == "like":
#     #      comments.likes +=1

#     #  elif reaction.action == "dislike":
#     #      comments.dislikes +=1
    
#      exesting_like = db.query(CommentLikeOrDislike).filter(
#         CommentLikeOrDislike.comment_id == comment_id,
#         CommentLikeOrDislike.user_id == like.user_id
#      ).first()

#     #  else :
#     #      raise HTTPException(status_code=400,detail="Invalid  action.Use 'like' or 'dislike'.")

#      if  exesting_like:
#         raise HTTPException(status_code=400,detail="Comment alredy liked") 

#      db_like = CommentLikeOrDislike(**like.dict())
#      db.add(db_like)
#      db.commit()
#      db.refresh(db_like)
#      return {
#          "Status":"Success",
#          "Message":f"Comment  successfully.", 
#         #  "comment": comments
#          }


def create_like(like:CommentLikeOrDislike,db:Session=Depends(get_db)):
   
   user = db.query(UserModel).filter(UserModel.id == like.user_id).first()

   if not user :
       raise HTTPException(status_code=404,detail="User not found")
   
   if like.post_id:
       post  = db.query(PostModel).filter(PostModel.id == like.post_id).first()
       if not post:
           raise HTTPException(status_code=404,detail="Post not found")
    
   if like.comment_id:
       comment =db.query(CommentModel).filter(CommentModel.id == like.comment_id).first()
       if not comment:
           raise HTTPException(status_code=404,detail="Comment not found")
       
   db_like = CommentLike(
        post_id=like.post_id,
        comment_id=like.comment_id,
        user_id=like.user_id,
        created_at =datetime.utcnow()

    )
   db.add(db_like)
   db.commit()
   db.refresh(db_like)

   return{
       "Status":"Success",
       "Message":"Like created Successfully",
       "data":{
           "like_id":db_like.id,
           "user_id":db_like.user_id,
           "comment_id":db_like.comment_id,
           "post_id":db_like.post_id
       }
   }

