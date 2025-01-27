from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from app.dependecy import get_patient_repository
from app.user.handlers import router as user_router
from app.user.repository import PatientRepository


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user_router)

@app.get("/ping/app")
async def ping_app():
    return {"result": "App is working"}

@app.get("/ping/db")
async def ping_db(patient_repository: PatientRepository = Depends(get_patient_repository)):
    await patient_repository.ping_db()
