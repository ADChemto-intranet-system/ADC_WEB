"""
인증 관련 스키마
"""

from pydantic import BaseModel, EmailStr
from typing import Optional


class Token(BaseModel):
    """토큰 응답 스키마"""
    access_token: str
    token_type: str
    expires_in: int


class TokenData(BaseModel):
    """토큰 데이터 스키마"""
    email: Optional[str] = None


class UserLogin(BaseModel):
    """사용자 로그인 스키마"""
    email: EmailStr
    password: str
