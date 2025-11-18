from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from account_api.api.auth.services import authenticate_user, create_user
from account_api.core.database import get_session
from account_api.api.auth.schemas import LoginIn
from account_api.api.users.models import ClientModel
from account_api.core.security import create_access_token

router = APIRouter()

@router.post("/login")
def login(request: LoginIn, db: Session = Depends(get_session)):
    """
    Login route for obtaining an access token after verifying credentials.
    """
    user = authenticate_user(db, request.email, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Generate an access token
    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
  
@router.post("/signup")
def signup(request: LoginIn, db: Session = Depends(get_session)):
    """
    Sign-up route for creating a new user and storing their credentials securely.
    """
    user = db.query(ClientModel).filter(ClientModel.email == request.email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # Create the new user
    new_user = create_user(db, request.email, request.password)
    
    # Generate access token for the new user
    access_token = create_access_token({"sub": new_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
  
  