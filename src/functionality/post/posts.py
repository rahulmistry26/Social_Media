from datetime import  datetime
import os
from random import randint
import uuid
from src.resource.post.model import PostModel ,PostLike
from src.resource.user.model import UserModel
from src.resource.post.schema import Post,GetPost,UpdatePost,PostLikeSchema
from sqlalchemy.orm import Session
from database import get_db
from fastapi import File, HTTPException,Depends,UploadFile

IMAGEDIR = "image/"
def  create_post(post:Post,db: Session=Depends(get_db), file: UploadFile=File(...)):
    try:
        # breakpoint()
        post=PostModel(
            user_id= post.user_id,
            title =post.title,
            caption=post.caption,
            image_url=file.filename,
            created_at=datetime.utcnow(),
           
            
        )
        file_extension = file.filename.split('.')[-1]
        file.filename = f"{uuid.uuid4()}.{file_extension}"
        
        file_path = f"{IMAGEDIR}/{file.filename}"
        contents = file.file.read()
        with open(file_path, "wb") as f:
            f.write(contents)
    except:
        raise HTTPException(status_code=400,detail="Invalid post details")
    
    
    db.add(post)
    db.commit()
    db.refresh(post)
    return{
        "messsage":"post created successfully"
    }


# def post_by_id(get_user,db:Session=Depends(get_db)):
#     try:
#         # breakpoint()
#         file =os.listdir(IMAGEDIR)

#         rd_indenx= randint(0,len(file)-1)
#         path=os.path.join(IMAGEDIR,file[rd_indenx])

#         post_id =get_user.post_id
#         post_data=db.query(PostModel).filter(PostModel.id==post_id).first()
#         if not post_data:
#             raise HTTPException(status_code=404,detail=f"Psot id {post_id} not found")
        
#         return{
#             "Succes":True,
#             "Message":"Post Found Successfully",
#             "Post_id":post_data.id,
#             "Title":post_data.title,
#             "Caption":post_data.caption,
#             "Created_at":post_data.created_at,
#             "File_path":path

#         }

#     except Exception as e:
#         raise HTTPException(status_code=500,detail="An unexpected error occurred while fetching the user’s post")
        

def read_all_post(db:Session=Depends(get_db)):
    posts = db.query(PostModel).all()
    if not posts:
        raise HTTPException(status_code=404,detail="No posts found")

    return{
    "Status":"Success",
    "Message":"Posts found successfully",
    "Data":[
        {
            "post_id":post.id,
            "title":post.title,
            "caption":post.caption,
            "created_at":post.created_at
            } for post in posts
    
    ]
} 
def delete_post(post_id :Post,db:Session=Depends(get_db)):
    # breakpoint()
    db_post= db.query(PostModel).filter(PostModel.id==post_id).first()

    if not db_post:
        raise HTTPException(status_code=404,detail="Post not found")
    
    db.delete(db_post)
    db.commit()
    return{
        "Status":"Success",
        "Message":"Post deleted successfully",
        "Deleted_post_id":post_id
    }
        
def update_post(post:UpdatePost,db:Session=Depends(get_db)):
    # breakpoint()
    db_post= db.query(PostModel).filter(PostModel.id==post.post_id).first()

    if not db_post:
        raise HTTPException(status_code=404,detail="Post not found")

    db_post.title =post.title
    db_post.caption = post.caption
    db.commit()
    db.refresh(db_post)
        
    return{
        "Status":"Success",
        "Message":"Post updated successfully",
        "Post_id":db_post.id,
        "Updated_title":db_post.title,
        "Updated_caption":db_post.caption,
        "Updated_at":db_post.updated_at

    }

def post_like(like:PostLikeSchema,db:Session=Depends(get_db)):

   user = db.query(UserModel).filter(UserModel.id == like.user_id).first()

   if not user :
       raise HTTPException(status_code=404,detail="User not found")
   
   if like.post_id:
       post  = db.query(PostModel).filter(PostModel.id == like.post_id).first()
       if not post:
           raise HTTPException(status_code=404,detail="Post not found")

   db_like = PostLike(
        post_id=like.post_id,
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
           "post_id":db_like.post_id
       }
   }