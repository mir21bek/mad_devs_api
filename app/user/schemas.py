from typing import List

from pydantic import BaseModel


class PatientCreateSchema(BaseModel):
    username: str
    password: str


class PatientLoginSchema(BaseModel):
    user_id: int
    access_token: str


class DiagnoseSchema(BaseModel):
    user_role: str
    user_diagnose: List[str]
