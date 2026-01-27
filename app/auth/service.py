from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.auth.password import verify_password
from app.auth.jwt import create_access_token


def authenticate_user(db: Session, email: str, password: str) -> str:
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, str(user.password_hash)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password"
        )

    if user.is_active is False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User is inactive"
        )

    return create_access_token({"sub": str(user.id), "role": user.role.value})
