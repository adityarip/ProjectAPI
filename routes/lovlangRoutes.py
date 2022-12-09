from database.db import get_db
from fastapi import APIRouter, Depends
from models.lovlangModels import *
# from models.userModels import ShowUser
from sqlalchemy.orm import Session
from typing import List
from auth.authenticate import authenticate
from pydantic import EmailStr, HttpUrl

from controllers import lovlangControllers

lovlang_router = APIRouter(
    tags=["Love Language"],
)

@lovlang_router.put("/users")
def get_user_list(request: UserLoveRequest, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return lovlangControllers.get_love_attachment(request, db, user)