"""
홈페이지 관련 스키마
"""

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class NewsBase(BaseModel):
    """뉴스 기본 스키마"""
    title: str
    content: str
    author: str


class NewsCreate(NewsBase):
    """뉴스 생성 스키마"""
    pass


class NewsResponse(NewsBase):
    """뉴스 응답 스키마"""
    id: int
    is_published: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class ContactBase(BaseModel):
    """문의 기본 스키마"""
    name: str
    email: EmailStr
    company: Optional[str] = None
    phone: Optional[str] = None
    subject: str
    message: str


class ContactCreate(ContactBase):
    """문의 생성 스키마"""
    pass


class ContactResponse(ContactBase):
    """문의 응답 스키마"""
    id: int
    is_processed: bool
    created_at: datetime
    processed_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
