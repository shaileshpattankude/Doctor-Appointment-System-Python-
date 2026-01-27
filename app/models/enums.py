from enum import Enum


class UserRole(str, Enum):
    PATIENT = "PATIENT"
    DOCTOR = "DOCTOR"
    ADMIN = "ADMIN"


class AppointmentStatus(str, Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"
    CANCELLED_BY_PATIENT = "CANCELLED_BY_PATIENT"
    CANCELLED_BY_ADMIN = "CANCELLED_BY_ADMIN"
    COMPLETED = "COMPLETED"
