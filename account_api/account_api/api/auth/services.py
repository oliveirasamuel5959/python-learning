from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from account_api.api.users.models import ClientModel
from account_api.api.users.schemas import ClientIn
from account_api.core.security import hash_password, verify_password

def authenticate_user(db: Session, form_data):
    """
    Authenticate a user based on email and password.
    Returns the user if authentication is successful, otherwise None.
    """
    user = db.query(ClientModel).filter(ClientModel.name == form_data.username).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    if not verify_password(form_data.password, user.hash_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return user

def create_user(db: Session, client_in: ClientIn):
    """
    Create a new user in the database with a hashed password.
    """

    user = db.query(ClientModel).filter(ClientModel.email == client_in.email).first()

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )

    hashed_password = hash_password(client_in.hash_password)

    client_out = ClientIn(
        hash_password=hashed_password,
        **client_in.model_dump(exclude={"hash_password"})
    )

    client = ClientModel(**client_out.model_dump())

    db.add(client)
    db.commit()
    db.refresh(client)

    return client

