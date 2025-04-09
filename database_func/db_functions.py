import models.models as models
from database import SessionLocal, engine
from utils.hashing import verify_password

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def authenticate_user(username: str, password: str, db):
    user = db.query(models.Users)\
        .filter(models.Users.username == username)\
        .first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user