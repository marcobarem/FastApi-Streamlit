from models import User, SessionLocal
from crud import get_user, get_all_users, create_user, update_user, delete_user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
