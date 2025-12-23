from fastapi import FastAPI

app = FastAPI(title="Doctor Appointment System")


@app.get("/health")
def health_check():
    return {"status": "ok"}
