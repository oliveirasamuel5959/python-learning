from jose import jwt, JWTError
from datetime import datetime, timedelta

SECRET_KEY = "REPLACE_THIS"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30

def create_token(data, expires_delta=None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    