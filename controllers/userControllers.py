from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from models.userModels import User, UserSchema, AnswerSchema
from fastapi import HTTPException, status
from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token
from pydantic import EmailStr


def sign_up(request: UserSchema, db: Session):
    user = db.query(User).filter(User.email == request.email).first()

    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email sudah digunakan."
        )

    if len(request.password) < 8:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Password setidaknya memiliki 8 karakter."
        )

    hashed_password = HashPassword().create_hash(request.password)
    new_user = User(email=request.email, nama=request.nama,
                    password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "Pesan": "Akun berhasil dibuat."
    }


def sign_in(request, db: Session):
    user = db.query(User).filter(User.email == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Akun dengan email tersebut tidak ditemukan."
        )

    if not HashPassword().verify_hash(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Gagal, silahkan periksa email/password Anda kembali!")

    access_token = create_access_token(user.email)

    return {"access_token": access_token, "token_type": "bearer"}


def get_all_user(db: Session):
    return db.query(User).all()


def get_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User dengan id tersebut tidak ditemukan."
        )

    return user


def analysis_attachment_style(request: AnswerSchema, db: Session, user: str):
    update_user = db.query(User).filter(User.email == user)

    kumpulan_jawaban = [request.jawaban_pertanyaan_1, request.jawaban_pertanyaan_2, request.jawaban_pertanyaan_3, request.jawaban_pertanyaan_4,
                        request.jawaban_pertanyaan_5, request.jawaban_pertanyaan_6, request.jawaban_pertanyaan_7, request.jawaban_pertanyaan_8, 
                        request.jawaban_pertanyaan_9, request.jawaban_pertanyaan_10, request.jawaban_pertanyaan_11, request.jawaban_pertanyaan_12, 
                        request.jawaban_pertanyaan_13, request.jawaban_pertanyaan_14, request.jawaban_pertanyaan_15, request.jawaban_pertanyaan_16, 
                        request.jawaban_pertanyaan_17, request.jawaban_pertanyaan_18, request.jawaban_pertanyaan_19, request.jawaban_pertanyaan_20, 
                        request.jawaban_pertanyaan_21, request.jawaban_pertanyaan_22]

    secure = 0
    fearful = 0
    preoccupied = 0
    dismissing = 0
    for i in range(len(kumpulan_jawaban)):
        if i in [0, 8, 11, 12, 15, 19]:
            secure += kumpulan_jawaban[i]
        elif i in [2, 6]:
            secure += 6 - kumpulan_jawaban[i]
        elif i in [1, 3, 17, 20]:
            fearful += kumpulan_jawaban[i]
        elif i in [5, 7, 9, 18, 21]:
            preoccupied += kumpulan_jawaban[i]
        elif i == 16:
            preoccupied += 6 - kumpulan_jawaban[i]
        elif i in [4, 10, 13, 16]:
            dismissing += kumpulan_jawaban[i]
    secure /= 8
    fearful /= 4
    preoccupied /= 6
    dismissing /= 4

    result = [secure, fearful, preoccupied, dismissing]
    max = result[0]
    idx = 0
    for i in range(len(result)):
        if result[i] > max:
            max = result[i]
            idx = i
    
    if idx == 0:
        attachment = "secure"
    elif idx == 1:
        attachment = "fearful"
    elif idx == 2:
        attachment = "preoccupied"
    else:
        attachment = "dismissing"
    
    update_user.update({'attachment': attachment})
    
    db.commit()

    return {"attachment": attachment}
