from fastapi import FastAPI 
from database.db import engine
from models import userModels, questionModels
from routes.userRoutes import user_router
from routes.questionRoutes import question_router

app = FastAPI()
app.debug = True

userModels.Base.metadata.create_all(engine)
questionModels.Base.metadata.create_all(engine)

app.include_router(user_router, prefix="/users")
app.include_router(question_router, prefix="/questions")

@app.get("/")
async def root():
    return {
        "Message": "Hello, World"
    }

"""
from fastapi import FastAPI
from database.db import engine
import uvicorn
from models import userModels, questionModels
from routes.userRoutes import user_router
from routes.questionRoutes import question_router

app = FastAPI()
app.debug  = True

userModels.Base.metadata.create_all(engine)
questionModels.Base.metadata.create_all(engine)

app.include_router(user_router, prefix="/users")
app.include_router(question_router, prefix="/questions")


@app.get('/')
def index():
    return {"Message" : "Welcome!"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
"""