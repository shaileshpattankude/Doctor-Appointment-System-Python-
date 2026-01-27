from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.core.config import settings

ALGORITHM = "HS256"


def create_access_token(data: dict) -> str:
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None
