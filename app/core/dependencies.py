from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.auth.jwt import decode_access_token
from app.models.user import User
from app.models.enums import UserRole

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token"
        )

    user = db.get(User, int(payload["sub"]))

    if user is None or user.is_active is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or inactive",
        )

    return user


def require_roles(*allowed_roles: UserRole):
    def checker(user=Depends(get_current_user)):
        if user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Access denied"
            )
        return user

    return checker
