from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from app import crud
from app import schemas
from app.api import deps
from app.core.auth import (
    authenticate,
    create_access_token,
)
from app.models.user import User

router = APIRouter()

@router.post("/login")
def login(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = authenticate(email=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    return {
        "access_token": create_access_token(sub=user.id),
        "token_type": "bearer"
    }


@router.get("/me", response_model=schemas.User)
def read_user_me(current_user: User = Depends(deps.get_current_user)) -> User:
    user = current_user
    return user

@router.post("/signup", response_model=schemas.User, status_code=201)
def create_user_signup(
    *,
    user_in: schemas.user.UserCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    user = db.query(User).filter(User.email == user_in.email).first()
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system",
        )
    user = crud.user.create(db=db, obj_in=user_in)
    return user