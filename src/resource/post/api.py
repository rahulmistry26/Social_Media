from fastapi import HTTPException,APIRouter,Depends,UploadFile,File
from src.resource.post.model import PostModel
from src.resource.post.schema import Post,GetPost,UpdatePost,PostLikeSchema
from sqlalchemy.orm import Session
from database import get_db
from src.functionality.post.posts import create_post,read_all_post,delete_post,update_post,post_like

user_post= APIRouter()

@user_post.post("/post")
def user1_post(post:Post=Depends(),file:UploadFile= File(...),db:Session=Depends(get_db)):
    response = create_post(post,db,file)
    return response 

@user_post.get("/get_post_all")
def get_post(db:Session=Depends(get_db)):
    try:

        posts=read_all_post(db=db)
        return posts
    except Exception as e:
        raise HTTPException(status_code=404,detail="Not found")
    

# @user_post.get("/get_by_id")
# def get_post_by_id(request:GetPost,db:Session=Depends(get_db)):
#     response = post_by_id (request,db)
#     return response 

@user_post.delete("/post-delete/{post_id}/")
def del_post(post_id:int,db:Session=Depends(get_db)):
    try:
        dels = delete_post(post_id=post_id,db=db)
        return dels
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
@user_post.patch("/post-update")
def up_post(post:UpdatePost,db:Session=Depends(get_db)):
    try:
        updt = update_post(post=post,db=db)
        return updt
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
@user_post.post("/post-like/")
def likedis_coment(like:PostLikeSchema,db:Session=Depends(get_db)):
   try:
      likedis= post_like(like=like,db=db)
      return  likedis
   except Exception as e:
      raise HTTPException(status_code=500,detail=str(e))
