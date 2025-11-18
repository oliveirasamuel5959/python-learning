from sqlalchemy.orm import Session
from account_api.api.users.models import ClientModel
from account_api.core.security import hash_password, verify_password

def authenticate_user(db: Session, email: str, password: str):
    """
    Authenticate a user based on email and password.
    Returns the user if authentication is successful, otherwise None.
    """
    user = db.query(ClientModel).filter(ClientModel.email == email).first()
    if user and verify_password(password, ClientModel.hash_password):
        return user
    return None

def create_user(db: Session, email: str, password: str):
    """
    Create a new user in the database with a hashed password.
    """
    hashed_password = hash_password(password)
    new_user = ClientModel(email=email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user