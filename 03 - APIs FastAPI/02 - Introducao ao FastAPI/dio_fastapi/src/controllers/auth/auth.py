# from fastapi import APIRouter

# from schemas.auth import LoginIn
# from auth_handler import signJWT
# from views.auth import LoginOut

# router = APIRouter(prefix="/auth", tags=["auth"])

# @router.post("/login", response_model=LoginOut)
# async def login(data: LoginIn):
#     return signJWT(data.user_id)