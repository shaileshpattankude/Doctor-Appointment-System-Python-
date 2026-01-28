from fastapi import FastAPI
from app.api.v1.health import router as health_router
from app.auth.router import router as auth_router
from app.api.v1.admin import router as admin_router

app = FastAPI(title="Doctor Appointment Management System")

app.include_router(health_router)
app.include_router(auth_router, prefix="/api/v1")
app.include_router(admin_router, prefix="/api/v1")
