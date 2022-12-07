from sqlalchemy import Column, Integer, String
from database.db import Base
from pydantic import BaseModel, EmailStr, conint
from typing import Optional


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    nama = Column(String)
    password = Column(String)
    attachment = Column(String, default="")

    class Config:
        schema_extra = {
            "Contoh": {
                "email": "sample@mail.com",
                "nama": "Adit",
                "password": "135790",
            }
        }


class UserSchema(BaseModel):
    email: EmailStr
    nama: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "sample@mail.com",
                "nama": "Adit",
                "password": "135790",
            }
        }


class ShowUser(BaseModel):
    email: EmailStr
    nama: str
    attachment: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "sample@mail.com",
                "nama": "Adit",
                "attachment": "Anxious",
            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class AnswerSchema(BaseModel):
    jawaban_pertanyaan_1: conint(gt=0, lt=8)
    jawaban_pertanyaan_2: conint(gt=0, lt=8)
    jawaban_pertanyaan_3: conint(gt=0, lt=8)
    jawaban_pertanyaan_4: conint(gt=0, lt=8)
    jawaban_pertanyaan_5: conint(gt=0, lt=8)
    jawaban_pertanyaan_6: conint(gt=0, lt=8)
    jawaban_pertanyaan_7: conint(gt=0, lt=8)
    jawaban_pertanyaan_8: conint(gt=0, lt=8)
    jawaban_pertanyaan_9: conint(gt=0, lt=8)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "jawaban_pertanyaan_1": 1,
                "jawaban_pertanyaan_2": 3,
                "jawaban_pertanyaan_3": 5,
                "jawaban_pertanyaan_4": 7,
                "jawaban_pertanyaan_5": 6,
                "jawaban_pertanyaan_6": 4,
                "jawaban_pertanyaan_7": 5,
                "jawaban_pertanyaan_8": 2,
                "jawaban_pertanyaan_9": 4

            }
        }
