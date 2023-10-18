from typing import Any, Coroutine, Optional
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette.requests import Request
from fastapi import HTTPException, status

from auth.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth)
        # Emulates the existance of the user in a  DB
        if data['email'] != "test@mail.com":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not Authorized")