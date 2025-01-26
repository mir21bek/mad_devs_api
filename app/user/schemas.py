from pydantic import BaseModel


class PatientCreateSchema(BaseModel):
    username: str
    password: str


class PatientLoginSchema(BaseModel):
    user_id: int
    access_token: str
