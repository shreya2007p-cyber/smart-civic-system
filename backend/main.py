from security import hash_password
from fastapi import FastAPI
from schemas.user import UserRegister
from database import engine, Base, SessionLocal
from model.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Smart Civic System API is running!"
    }


@app.post("/auth/register")
def register_user(user: UserRegister):

    db = SessionLocal()

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return {
        "message": "User registration successful",
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }