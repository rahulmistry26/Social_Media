from fastapi import HTTPException,APIRouter,Depends, Security
from src.resource.user.model import UserModel
from src.functionality.user.user import create_user,login_user,forget_password,veritfy_otp,reset_password,delte_user,user_detials,update_user,security
from src.resource.user.schema import UserCreate,UserLogin,ResetPassword,ForgetPassword,VerifyOtp,User,UpdateUserSchema
from sqlalchemy.orm import Session
from database import get_db




user_router =APIRouter()

@user_router.post("/register/")
def user_register(user:UserCreate,db:Session= Depends(get_db)):
    try:
        register = create_user(user=user,db=db)
        return register
    except Exception as e:
        return HTTPException(status_code=500,detail=str(e)) 
    
@user_router.post("/login/")
def user_login(user:UserLogin,db:Session= Depends(get_db)):
    try:
        login = login_user(user=user,db=db)
        return login
    except Exception as e:
        return HTTPException(status_code=500,detail=str(e))
    
@user_router.get("/users/")
def get_all_users(db: Session = Depends(get_db)):
    try:
        users = db.query(UserModel).all()
        return users
    except Exception as e:
        return HTTPException(status_code=500,detail=Depends(str(e)))
    
@user_router.post("/forget-password/")
def for_pass(user:ForgetPassword,db:Session=Depends(get_db)):
    try:
        forgetpass = forget_password(user=user,db=db)
        return forgetpass
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@user_router.post("/reset-password/")
def rset_password(request:ResetPassword, db:Session = Depends(get_db)):
    try:
        resetpass = reset_password(request=request,db=db)
        return resetpass
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
# @user_router.post("/verify-otp/")
# def vfy_otp(request:VerifyOtp,db:Session=Depends(get_db)):
#     try:
#         verify =veritfy_otp(request=request)

#         return verify
#     except Exception as e:
#         raise HTTPException(status_code=500,detail=str(e))

    
@user_router.post("/verify-otp/")
def verify_otp_endpoint(request: VerifyOtp):
    return veritfy_otp(request)

@user_router.delete("/delete-user/{user_id}")
def del_user(user_id:int,db:Session=Depends(get_db),token :str = Security(security)):
    try:
        dels = delte_user(user_id=user_id,db=db,token=token)
        return dels
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
# @user_router.get("/user_get")
# def get_user(db:Session=Depends(get_db)):
#     try:
#         use = user_detials(db=db)
#         return use
#     except Exception as e:
#         raise HTTPException(status_code=404,detail="Not Found")

@user_router.put("/user-update")
def use_det(user:UpdateUserSchema,db:Session=Depends(get_db)):
    try:
        updt = update_user(user=user,db=db)
        return updt
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))