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
                "password": "12345678",
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
                "password": "12345678",
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
                "attachment": "secure",
            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class AnswerSchema(BaseModel):
    jawaban_pertanyaan_1: conint(gt=0, lt=6)
    jawaban_pertanyaan_2: conint(gt=0, lt=6)
    jawaban_pertanyaan_3: conint(gt=0, lt=6)
    jawaban_pertanyaan_4: conint(gt=0, lt=6)
    jawaban_pertanyaan_5: conint(gt=0, lt=6)
    jawaban_pertanyaan_6: conint(gt=0, lt=6)
    jawaban_pertanyaan_7: conint(gt=0, lt=6)
    jawaban_pertanyaan_8: conint(gt=0, lt=6)
    jawaban_pertanyaan_9: conint(gt=0, lt=6)
    jawaban_pertanyaan_10: conint(gt=0, lt=6)
    jawaban_pertanyaan_11: conint(gt=0, lt=6)
    jawaban_pertanyaan_12: conint(gt=0, lt=6)
    jawaban_pertanyaan_13: conint(gt=0, lt=6)
    jawaban_pertanyaan_14: conint(gt=0, lt=6)
    jawaban_pertanyaan_15: conint(gt=0, lt=6)
    jawaban_pertanyaan_16: conint(gt=0, lt=6)
    jawaban_pertanyaan_17: conint(gt=0, lt=6)
    jawaban_pertanyaan_18: conint(gt=0, lt=6)
    jawaban_pertanyaan_19: conint(gt=0, lt=6)
    jawaban_pertanyaan_20: conint(gt=0, lt=6)
    jawaban_pertanyaan_21: conint(gt=0, lt=6)
    jawaban_pertanyaan_22: conint(gt=0, lt=6)


    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "jawaban_pertanyaan_1": 1,
                "jawaban_pertanyaan_2": 3,
                "jawaban_pertanyaan_3": 5,
                "jawaban_pertanyaan_4": 3,
                "jawaban_pertanyaan_5": 2,
                "jawaban_pertanyaan_6": 1,
                "jawaban_pertanyaan_7": 3,
                "jawaban_pertanyaan_8": 2,
                "jawaban_pertanyaan_9": 2,
                "jawaban_pertanyaan_10": 1,
                "jawaban_pertanyaan_11": 1,
                "jawaban_pertanyaan_12": 3,
                "jawaban_pertanyaan_13": 5,
                "jawaban_pertanyaan_14": 3,
                "jawaban_pertanyaan_15": 2,
                "jawaban_pertanyaan_16": 1,
                "jawaban_pertanyaan_17": 3,
                "jawaban_pertanyaan_18": 2,
                "jawaban_pertanyaan_19": 2,
                "jawaban_pertanyaan_20": 1,
                "jawaban_pertanyaan_21": 1,
                "jawaban_pertanyaan_22": 3

            }
        }
