import datetime
from dataclasses import dataclass
from typing import List

from sqlalchemy import select
from jose import jwt, JWTError
from datetime import datetime as dt, timedelta

from app.exception import UserNotFoundException, UserNotCorrectPasswordException, TokenNotCorrect, TokenExpired, \
    RoleNotFoundException
from app.settings import Settings
from app.user.models import Patient
from app.user.schemas import PatientLoginSchema, PatientCreateSchema, DiagnoseSchema
from app.user.repository import PatientRepository


@dataclass
class PatientService:
    settings = Settings
    user_repository = PatientRepository


    async def create_user(self, username: str, password: str) -> PatientCreateSchema:
        user_data_create = PatientCreateSchema(username=username, password=password)
        user = await self.user_repository.create_user(user_data_create)
        access_token = self._generate_access_token(user_id=user.id)
        return PatientLoginSchema(user_id=user.id, access_token=access_token)


    async def user_login(self, username: str, password: str) -> PatientLoginSchema:
        user = await self.user_repository.get_user_by_username(username)
        self._validate_auth_user(user, password)
        access_token = self._generate_access_token(user_id=user.id)
        return PatientLoginSchema(user_id=user.id, access_token=access_token)

    async def get_diagnose_list(self, role_name) -> DiagnoseSchema:
        role = await self.user_repository.get_user_role(role_name)
        if not role_name:
            raise RoleNotFoundException
        diagnoses = await self.user_repository.get_diagnose_by_user_role(role_name)
        return DiagnoseSchema(user_role=role, user_diagnose=[diagnose.title for diagnose in diagnoses])



    @staticmethod
    def _validate_auth_user(user: Patient, password: str):
        if not user:
            raise UserNotFoundException
        if user.password != password:
            raise UserNotCorrectPasswordException


    def _generate_access_token(self, user_id: str):
        payload = {"user_id": user_id, "expire": (dt.now(tz=datetime.UTC) + timedelta(days=1)).timestamp()}
        encode_jwt = jwt.encode(payload, self.settings.JWT_SECRET_KEY, algorithm=self.settings.JWT_ENCODE_ALGORITHM)
        return encode_jwt


    def get_user_id_from_access_token(self, token: str) -> int:
        try:
            payload = jwt.decode(token, self.settings.JWT_SECRET_KEY, algorithms=[self.settings.JWT_ENCODE_ALGORITHM])
        except JWTError:
             raise TokenNotCorrect
        if payload['expire'] < dt.utcnow().timestamp():
            raise TokenExpired
        return payload['user_id']