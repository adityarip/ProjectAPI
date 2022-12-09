from sqlalchemy.orm import Session
from models.lovlangModels import ShowUserLove, UserLoveRequest
from models.userModels import User
from fastapi import HTTPException, status
import requests

callback_url = "https://lovelangapi.politeground-4e0e77af.eastus.azurecontainerapps.io/"
# callback_url = "https://apiadit.calmpond-d268450b.eastus.azurecontainerapps.io/"

def get_love_attachment(request: UserLoveRequest, db: Session, user: str):
    # signup = requests.post(callback_url + "users/signup", json= {
    #     "email": request.username,
    #     "nama": "Adit",
    #     "password": request.password,
    # })
    db_user = db.query(User).filter(User.email == user).first()
 
    res = requests.post(callback_url +"users/signin", data= {
        "username": request.username, 
        "password": request.password,})
    
    session = requests.Session()
    out = session.get(callback_url + "users/", 
        headers={"Authorization": "Bearer " + res.json().get("access_token")})
    
    for row in out.json():
        if row.get("email") == request.username:
            userOut = ShowUserLove(
                nama= db_user.nama, 
                physical_touch= row.get("physical_touch"),
                word_affirmation= row.get("word_affirmation"),
                receiving_gift= row.get("gift"),
                quality_time= row.get("quality_time"),
                act_of_service= row.get("act_of_service"),
                attachment= db_user.attachment),
            return userOut