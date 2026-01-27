from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base
from app.models.enums import AppointmentStatus


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    scheduled_at = Column(DateTime, nullable=False)
    status = Column(String, default=AppointmentStatus.SCHEDULED, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    patient = relationship("User", foreign_keys=[patient_id])
    doctor = relationship("Doctor")
