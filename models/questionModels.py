from sqlalchemy import Column, Integer, String
from database.db import Base
from pydantic import BaseModel


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    pertanyaan = Column(String)
    pilihan = Column(String)

    class Config:
        schema_extra = {
            "example": {
                "pertanyaan": "Provided me with sufficient food and housing, and medical care when needed",
                "pilihan": "(Very rarely) 1, 2, 3, 4, 5, 6, 7 (Very frequently)"
            }
        }


class QuestionSchema(BaseModel):
    pertanyaan: str
    pilihan: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "pertanyaan": "Provided me with sufficient food and housing, and medical care when needed",
                "pilihan": "(Very rarely) 1, 2, 3, 4, 5, 6, 7 (Very frequently)"
            }
        }


class QuestionShow(BaseModel):
    id: int
    pertanyaan: str
    pilihan: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "int": 1,
                "pertanyaan": "Provided me with sufficient food and housing, and medical care when needed",
                "pilihan": "(Very rarely) 1, 2, 3, 4, 5, 6, 7 (Very frequently)"
            }
        }


class QuestionUpdate(BaseModel):
    pertanyaan: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "pertanyaan": "Provided me with sufficient food and housing, and medical care when needed",
            }
        }
