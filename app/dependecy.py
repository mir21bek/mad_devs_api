from app.settings import Settings
from app.user.repository import PatientRepository

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.database.accsessor import get_db_session
from app.user.service import PatientService


async def get_patient_repository(db_session: AsyncSession = Depends(get_db_session)) -> PatientRepository:
    return PatientRepository(db_session=db_session)

async def get_patient_service(settings: Settings = Depends(Settings),
                              user_repository: PatientRepository = Depends(get_patient_repository)
                              ) -> PatientService:
    return PatientService(settings=settings, user_repository=user_repository)