from dataclasses import dataclass

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.settings import Settings
from app.user.models import Patient
from app.user.schemas import PatientCreateSchema


@dataclass
class PatientRepository:
    db_session = AsyncSession
    settings = Settings

    async def create_user(self, user_data: PatientCreateSchema) -> Patient:
        query = insert(Patient).values(**user_data.dict(exclude_none=True)).returning(Patient.id)
        async with self.db_session as session:
            user_id = (await session.execute(query)).scalar()
            await session.commit()
            await session.flush()
            return await self.get_user_id(user_id)

    async def get_user_id(self, user_id) -> Patient | None:
        query = select(Patient).where(Patient.id == user_id)
        async with self.db_session as session:
            return (await session.execute(query)).scalar_one_or_none()

    async def get_user_by_username(self, username) -> Patient:
        query = select(Patient).where(Patient.username == username)
        async with self.db_session as session:
            return {await session.execute(query).scalar_one_or_none()}

    async def get_user_by_role(self, role) -> Patient:
        query = select(Patient).where(Patient.role == role)
        async with self.db_sessiona as session:
            return (await session.execute(query)).scalar()
