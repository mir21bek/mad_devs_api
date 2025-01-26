from datetime import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base
from sqlalchemy import DateTime, String, Integer



class Role(Base):
    __tablename__ = "t_roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True, nullable=False)

    users = relationship("Patient", back_populates="role")


class Diagnose(Base):
    __tablename__ = 't_diagnostic'
    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    patients = relationship("Patient", back_populates="diagnoses")


class Patient(Base):
    __tablename__ = 't_user_profile'
    id = Column(Integer, primary_key=True)
    username = Column(String(64))
    password = Column(String(256))
    date_of_birth = Column(String(64))
    created_at = Column(DateTime, default=datetime.now())

    role_id = Column(Integer, ForeignKey("t_roles.id"))
    role = relationship("Role", back_populates="users")

    diagnoses_id = Column(ForeignKey("t_diagnostic.id"))
    diagnoses = relationship("Diagnose", back_populates="patients")
