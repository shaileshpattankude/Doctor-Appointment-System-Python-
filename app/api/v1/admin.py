from fastapi import APIRouter, Depends
from app.core.dependencies import require_roles
from app.models.enums import UserRole

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/dashboard")
def admin_dashboard(user=Depends(require_roles(UserRole.ADMIN))):
    return {"message": "Admin dashboard"}
