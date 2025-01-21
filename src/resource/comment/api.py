from fastapi import HTTPException,APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from src.resource.comment.schema import CommentSchema,CommentLikeOrDislike

from src.functionality.comment.comment import create_comment,delete_comment,read_all_comment,create_like


user_comment = APIRouter()


@user_comment.post("/create-comment/")
def cre_coment(comment:CommentSchema,db:Session=Depends(get_db)):
   try:
      cte = create_comment(comments=comment,db=db)
      return cte
   except Exception as e:
      raise HTTPException(status_code=400,detail=str(e)) 
   

@user_comment.get("/get_comment_all")
def get_comment(db:Session=Depends(get_db)):
   try:
      comments = read_all_comment(db=db)
      return comments
   except Exception as e:
      raise HTTPException(status_code=500,Depends="Not found")

@user_comment.delete("/comment-delete/{comment_id}/")
def delt_coment(comment_id:int,db:Session=Depends(get_db)):
   try:
      dels = delete_comment(comment_id=comment_id,db=db)
      return dels
   except Exception as e:
      raise HTTPException(status_code=500,detail=str(e))
   
@user_comment.post("/commnet-like/")
def likedis_coment(like:CommentLikeOrDislike,db:Session=Depends(get_db)):
   try:
      likedis= create_like(like=like,db=db)
      return  likedis
   except Exception as e:
      raise HTTPException(status_code=500,detail=str(e))
