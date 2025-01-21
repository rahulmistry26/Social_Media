from datetime import datetime
from pydantic import BaseModel

class UserCreate(BaseModel):
    email:str
    password:str
    first_name:str
    last_name:str
    created_at: datetime = datetime.utcnow()
    is_active:datetime =datetime.utcnow()
    is_verified:datetime=datetime.utcnow()
    is_deleted:datetime=datetime.utcnow


class UserLogin(BaseModel):
    email:str
    password:str

class User(BaseModel):
    email:str
    passoword:str
    first_name:str
    last_name:str

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class ForgetPassword(BaseModel):
    email :str

class ResetPassword(BaseModel):
    email:str
    new_password:str
    conform_password:str

class VerifyOtp(BaseModel):
    email:str
    otp:str

class UpdateUserSchema(BaseModel):
    id:int
    email:str
    first_name:str
    last_name:str
    password:str