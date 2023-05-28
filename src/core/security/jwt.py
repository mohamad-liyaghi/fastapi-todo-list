from datetime import datetime, timedelta
from jose import jwt
from dotenv import load_dotenv
from core.config import config

load_dotenv()

SECRET_KEY = config.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class JWTHandler:
    
    @staticmethod
    async def create_access_token(data: dict):
        to_encode = data.copy()
        
        expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
