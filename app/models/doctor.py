from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    specialization = Column(String, nullable=False)
    experience_years = Column(Integer, nullable=False)

    user = relationship("User")
