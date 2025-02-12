from fastapi import APIRouter, Depends
from app.services.patient_service import get_patient_service, PatientService
from app.schemas.patient import PatientCreateSchema, PatientLoginSchema, DiagnoseSchema

router = APIRouter()

@router.post("/register", response_model=PatientLoginSchema)
async def register_user(
    username: str,
    password: str,
    patient_service: PatientService = Depends(get_patient_service),
):
    return await patient_service.create_user(username, password)


@router.post("/login", response_model=PatientLoginSchema)
async def login_user(
    username: str,
    password: str,
    patient_service: PatientService = Depends(get_patient_service),
):
    return await patient_service.user_login(username, password)


@router.get("/diagnoses", response_model=DiagnoseSchema)
async def get_diagnoses(
    role_name: str,
    patient_service: PatientService = Depends(get_patient_service),
):
    return await patient_service.get_diagnose_list(role_name)
