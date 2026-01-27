from fastapi import FastAPI
from app.api.v1.health import router as health_router
from app.auth.router import router as auth_router

app = FastAPI(title="Doctor Appointment Management System")

app.include_router(health_router)
app.include_router(auth_router, prefix="/api/v1")
