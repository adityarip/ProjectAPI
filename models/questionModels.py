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
                "pertanyaan": "I feel at ease in emotional relationships",
                "pilihan": "(Disagree) 1, 2, 3, 4, 5(Agree)"
            }
        }


class QuestionSchema(BaseModel):
    pertanyaan: str
    pilihan: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "pertanyaan": "I feel at ease in emotional relationships",
                "pilihan": "1 (Strongly Disagree), 2 (Disagree), 3 (Neutral), 4 (Agree), 5 (Strongly Agree)"
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
                "pertanyaan": "I feel at ease in emotional relationships",
                "pilihan": "1 (Strongly Disagree), 2 (Disagree), 3 (Neutral), 4 (Agree), 5 (Strongly Agree)"
            }
        }


class QuestionUpdate(BaseModel):
    pertanyaan: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "pertanyaan": "I feel at ease in emotional relationships",
            }
        }
