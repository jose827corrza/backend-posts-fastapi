from jwt import encode, decode
import os

# from main import jwt_key

def create_token(data: dict) -> str:
    jwt_key: str = os.getenv('JWT_SECRET_KEY')
    token: str = encode(payload=data, key=jwt_key, algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    key: str = os.getenv('JWT_SECRET_KEY')
    data: dict = decode(token, key=key, algorithms=['HS256'])
    return data