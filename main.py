from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from controlador import get_db
from models import User
from crud import get_user, get_all_users, create_user, update_user, delete_user

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD application"}

@app.get("/users/", response_model=List[UserResponse])
def read_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users

@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    return create_user(db, db_user)

@app.put("/users/{user_id}", response_model=UserResponse)
def update_existing_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    updated_user = update_user(db, user_id, db_user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}")
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
