"""
사용자 관련 스키마
"""

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    """사용자 기본 스키마"""
    email: EmailStr
    full_name: str
    department: Optional[str] = None
    position: Optional[str] = None


class UserCreate(UserBase):
    """사용자 생성 스키마"""
    password: str


class UserResponse(UserBase):
    """사용자 응답 스키마"""
    id: int
    is_active: bool
    is_admin: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
