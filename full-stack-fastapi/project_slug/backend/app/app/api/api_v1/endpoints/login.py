from datetime import timedelta

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.token import Token
from app.api.utils.db import get_db

router = APIRouter()


@router.post("/login/access-token", response_model=Token, tags=["login"])
def login_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """
    OAuth2 compatible token login , get an access token for future requests
    """

