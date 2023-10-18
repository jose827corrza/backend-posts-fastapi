from jwt import encode, decode
import os

def create_token(data: dict) -> str:
    key: str = os.getenv('JWT_SECRET_KEY')
    print(key)
    token: str = encode(payload=data, key=key, algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    key: str = os.getenv('JWT_SECRET_KEY')
    data: dict = decode(token, key=key, algorithms=['HS256'])
    return data