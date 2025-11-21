from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from account_api.api.auth.services import authenticate_user, create_user
from account_api.api.users.schemas import ClientIn
from account_api.core.database import get_session
from account_api.api.auth.schemas import Token
from account_api.core.security import create_access_token, create_refresh_token
from account_api.core.configs.logger_handler import logger

router = APIRouter()

@router.post("/signup", summary="User Sign-Up", status_code=status.HTTP_201_CREATED)
async def signup(request: ClientIn, db: Session = Depends(get_session)):
    logger.info(f"Creating user with email: {request.email}")
    user = create_user(db, request)
    return {"msg": "User created successfully"}


@router.post(
    "/login", 
    summary="User Login", 
    status_code=status.HTTP_200_OK, 
    response_model=Token
)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)):
    user = authenticate_user(db, form_data)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user.email),
        "refresh_token": create_refresh_token(user.email),
        "token_type": "bearer"
    }
