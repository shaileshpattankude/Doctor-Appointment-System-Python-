from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.auth.service import authenticate_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    token = authenticate_user(db=db, email=payload.email, password=payload.password)

    return {"access_token": token}
