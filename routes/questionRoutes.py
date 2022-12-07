from database.db import get_db
from fastapi import APIRouter, Depends
from models.questionModels import QuestionSchema, QuestionUpdate, QuestionShow
from models.userModels import UserSchema
from sqlalchemy.orm import Session
from typing import List
from auth.authenticate import authenticate


from controllers import questionControllers

question_router = APIRouter(
    tags=["Question"],
)


@question_router.post("/create")
def create_a_new_question(request: QuestionSchema, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return questionControllers.create_quesiton(request, db, user)


@question_router.get("/", response_model=List[QuestionShow])
def get_all_existing_questions(db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return questionControllers.get_questions(db)


@question_router.get("/{id}", response_model=QuestionShow)
def get_an_existing_question(id: int, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return questionControllers.get_question(id, db)


@question_router.put("/update/{id}")
def update_an_existing_question(id: int, request: QuestionUpdate, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return questionControllers.update_question(id, request, db, user)


@question_router.delete("/delete/{id}")
def delete_an_existing_question(id: int, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return questionControllers.delete_question(id, db, user)