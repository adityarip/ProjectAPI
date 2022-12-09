from pydantic import BaseModel, EmailStr

class ShowUserLove(BaseModel):
    nama: str
    physical_touch: int
    word_affirmation: int
    receiving_gift: int
    quality_time: int
    act_of_service: int
    attachment: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                    "email": "sample@mail.com",
                    "nama": "Adit",
                    "physical_touch": 20,
                    "word_affirmation": 20,
                    "receiving_gift": 20,
                    "quality_time": 20,
                    "act_of_service": 20,
                    "attachment": "secure"
            }
        }


class UserLoveRequest(BaseModel):
    username: EmailStr
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "sample@mail.com",
                "password": "12345678",
            }
        }

# class UserLove(BaseModel):
#     email: EmailStr
#     nama: str
#     physical_touch: int
#     word_affirmation: int
#     gift: int
#     quality_time: int
#     act_of_service: int

#     class Config:
#         orm_mode = True
#         schema_extra = {
#             "example": {
#                 "email": "sample@mail.com",
#                 "nama": "Adit",
#                 "physical_touch": 20,
#                 "word_affirmation": 20,
#                 "gift": 20,
#                 "quality_time": 20,
#                 "act_of_service": 20,
#             }
#         }