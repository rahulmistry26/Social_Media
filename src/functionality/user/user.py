from datetime import datetime
from fastapi.security import HTTPBearer
from src.resource.user.model import UserModel
from src.resource.user.schema import UserCreate,UserLogin,ForgetPassword,ResetPassword,VerifyOtp,UpdateUserSchema
from sqlalchemy.orm import Session
from src.utils.user.user import create_access_token,create_refresh_token,pwd_context,verify_password,otp_genrates,send_email,verify_token
from fastapi import HTTPException,Depends, Security
from database import get_db
from pydantic import validate_email

security = HTTPBearer()

otp_store={}

def create_user(user:UserCreate,db : Session = Depends (get_db)):

    try:
        # breakpoint()
        validate_email(user.email)
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))


    # db_user =db.query(UserModel).filter(UserModel.email==user.email).first()
    # if db_user:
    #     raise HTTPException(status_code=200,detail="Email already register")
    
    hash_password = pwd_context.hash(user.password)

    db_user= UserModel(email=user.email,
                       password=hash_password,
                       first_name=user.first_name,
                       last_name=user.last_name,
                       created_at=datetime.utcnow(),
                       updated_at=datetime.utcnow(),
                        is_active=True,)

    db.add(db_user)
    db.commit()
    # db.refresh(db_user)
    
    otp = otp_genrates()
    otp_store[user.email] = otp
    

    subejct = "This is Test mail server form Roy..!"
    body=f"Your OTP code is {otp} ...It will expire in 1 minutes."
    
    try:
        send_email(to_email=user.email,subject=subejct,body=body)
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Faild to send OTP email: {str(e)}")
    return {
    "status":"Success",
    "User_id":db_user.id,   
    "Created_at":db_user.created_at,
    "Email":"Your OTP send successfully --> check your email",
    "Messgae":"Please OTP verified !!"
    }

def login_user(user:UserLogin,db : Session =Depends(get_db)):
    
    db_user = db.query(UserModel).filter(UserModel.email==user.email).first()
    if  not db_user or not verify_password(user.password,db_user.password):
        raise HTTPException(status_code=400,detail="Incorrect deatlis...!")

    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})
    return {"access_token": access_token,
            "refresh_token": refresh_token,
             "token_type": "bearer","Message":"Login Successfully"}

  
def forget_password(user:ForgetPassword,db:Session=Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email==user.email).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="User email not found ")

    otp = otp_genrates()
    otp_store[user.email]=otp
   
    body = "Reset passowrd "
    subejct = f"OTP is deliverd on email Pelase verify {otp}...It will expire in 1 minutes"

    try:
        send_email(to_email=user.email,subject=subejct,body=body)
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Faild to send OTP email: {str(e)}")
    return {"Status":"Success",
            "Message":"OTP has been sent on your email..."}

def veritfy_otp(request:VerifyOtp):

    try:
        if request.email not in otp_store:
         raise HTTPException(status_code=404,detail="OTP is not valid Its Expires")
    
        # otp_data =otp_store[request.email]
        # stored_otp = otp_data["otp"]
        stored_otp = otp_store[request.email]
    
        if request.otp != stored_otp:
            raise HTTPException(status_code=400,detail="Inavlid OTP please try again...!!!")
        
        del otp_store[request.email]

        return{"Status":"Success",
            "message":"OTP veryfied successfully",
            "user":"User Successfully Register"}
    
    except Exception as e:
        raise e
    
    except Exception as e:
        print(f"Unexpeced error:  {e}")
        raise HTTPException(status_code=500,detail="An internal sever error occurred")

def reset_password(request :ResetPassword,db:Session = Depends(get_db)):
    db_user =db.query(UserModel).filter(UserModel.email == request.email).first()

    if not db_user:
        raise HTTPException(status_code=404,detail="User not found and name is mismathced")
    
    if request.new_password != request.conform_password:
        raise HTTPException(status_code=400,detail="New password and conform passwprd does not matched")
    
    hash_password = pwd_context.hash(request.new_password)
       
    db_user.password = hash_password
    db.commit()

    return{
        "Status":"Success",
        "Message":"Password reset successfully"
    }

def delte_user(user_id:int,db:Session=Depends(get_db),token :str = Security(security)):

    try:
      token_data = verify_token(token.credentials)
    except Exception :
        raise HTTPException(status_code=400,detail="Invalid or expire token")
      
    user  = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
          raise HTTPException(status_code=404,detail="User not found")
      
    db.delete(user)
    db.commit()
      
    return{"Status":"Success",
           "Message":"User deleted successfully",
           "user_id":user_id
           }
    

def user_detials(db:Session=Depends(get_db)):
    us =db.query(UserModel).all()
    if not us:
        raise HTTPException(status_code=404,detail="Not Found User")
    
    return{
        "Status":"Success",
        "Message":"User Found successfully",
        "Data":[
            {
                "user_id":us,
            }
        ]
    }

def update_user(user:UpdateUserSchema,db:Session=Depends(get_db)):  
    try:
        # breakpoint()
        db_user =db.query(UserModel).filter(UserModel.id==user.id).first()

        if not db_user:
            raise HTTPException(status_code=404,detail="User Not Found")
        
        db_user.email=user.email
        db_user.first_name=user.first_name
        db_user.last_name=user.last_name
        db_user.password=user.password
        db.commit()
        db.refresh(db_user)

        return{
            "Status":"Success",
            "Message":"User updated successfully",
            "Post_id":db_user.id,
            "Updated_first_name":db_user.first_name,
            "Updated_last_name":db_user.last_name,
            "Updated_email":db_user.email,
            "Updated_password":db_user.password,
            "Updated_at":db_user.updated_at

        }
    except Exception as e:
        raise HTTPException(status_code=500,detail="Not Updated")