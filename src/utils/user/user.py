from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random,smtplib
from fastapi import HTTPException
from jose import JWTError
import jwt
from passlib.context import CryptContext
from passlib.hash import bcrypt
SECRET_KEY = "social_app_insta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_MINUTES = 60


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def otp_genrates():
    return str(random.randint(10000,99999))

def send_email(to_email,subject , body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "rahul321.rejoice@gmail.com"
    sender_password = "whha bzpx ixgo zymu"

    try:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))


        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.starttls()
            server.login(sender_email,sender_password)
            server.sendmail(sender_email, to_email, message.as_string())
            message = f"Subject: {subject}\n\n{body}"
    except Exception as e:
        raise Exception(f"Error sending email: {str(e)}")



def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(pain_password,hashed_password): 
    return pwd_context.verify(pain_password,hashed_password)
    
# def create_access_token(data :dict):
#     to_encode =data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# def create_refresh_token(data :dict,expiry_delta:str):
#     exprie = datetime.utcnow() +(expiry_delta or timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES))
#     to_encode.update({"exp": exprie})
#     to_encode = data.copy()
#     return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
def create_refresh_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token:str):
    security_token = "social_app_insta"
    algorithm = ["HS256"]
    try :
        payload = jwt.decode(token,security_token,algorithms=algorithm)
        return payload
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid or expire token")











