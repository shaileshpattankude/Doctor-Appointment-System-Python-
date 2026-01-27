# from enum import Enum
from sqlalchemy import Boolean, Column, Integer, String, Enum
from app.db.base import Base
from app.models.enums import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(
        Enum(UserRole, name="user_role_enum"), default=UserRole.PATIENT, nullable=False
    )
    is_active = Column(Boolean, default=True)
