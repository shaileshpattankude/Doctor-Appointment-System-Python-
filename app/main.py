from fastapi import FastAPI
from app.api.v1.health import router as health_router

app = FastAPI(title="Doctor Appointment Management System")

app.include_router(health_router)
