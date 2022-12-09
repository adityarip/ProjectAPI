from fastapi import FastAPI 
from database.db import engine
from models import userModels, questionModels
from routes.userRoutes import user_router
from routes.questionRoutes import question_router
from routes.lovlangRoutes import lovlang_router

app = FastAPI()
app.debug = True

userModels.Base.metadata.create_all(engine)
questionModels.Base.metadata.create_all(engine)

app.include_router(user_router, prefix="/users")
app.include_router(question_router, prefix="/questions")
app.include_router(lovlang_router, prefix="/love-language")

@app.get("/")
async def root():
    return {
        "Message": "Hello, World"
    }
