from app.auth.password import hash_password
from app.models.user import User
from app.models.enums import UserRole


def test_login_success(client, db_session):
    # from app.db.session import SessionLocal
    from app.models.user import User

    # db = SessionLocal()

    db_session.query(User).filter(User.email == "admin@test.com").delete()
    db_session.commit()

    user = User(
        email="admin@test.com",
        password_hash=hash_password("admin123"),
        role=UserRole.ADMIN,
        is_active=True,
    )
    db_session.add(user)
    db_session.commit()
    # db_session.close()

    response = client.post(
        "/api/v1/auth/login", json={"email": "admin@test.com", "password": "admin123"}
    )

    assert response.status_code == 200
    # data = response.json()
    assert "access_token" in response.json()


def test_login_invalid_password(client):
    response = client.post(
        "/api/v1/auth/login",
        json={"email": "admin@test.com", "password": "wrongpassword"},
    )

    assert response.status_code == 401


def test_protected_route_without_token(client):
    response = client.get("/api/v1/admin/dashboard")
    assert response.status_code == 401


def test_rbac_denied_for_patient(client, db_session):
    from app.db.session import SessionLocal
    from app.models.user import User

    # db = SessionLocal()

    db_session.query(User).filter(User.email == "patient@test.com").delete()
    db_session.commit()

    patient = User(
        email="patient@test.com",
        password_hash=hash_password("patient123"),
        role=UserRole.PATIENT,
        is_active=True,
    )
    db_session.add(patient)
    db_session.commit()
    # db_session.close()

    login = client.post(
        "/api/v1/auth/login",
        json={"email": "patient@test.com", "password": "patient123"},
    )

    assert login.status_code == 200
    token = login.json()["access_token"]

    response = client.get(
        "/api/v1/admin/dashboard", headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 403
