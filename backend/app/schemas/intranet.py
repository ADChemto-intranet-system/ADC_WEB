"""
인트라넷 관련 스키마
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NoticeBase(BaseModel):
    """공지사항 기본 스키마"""
    title: str
    content: str
    is_important: bool = False


class NoticeCreate(NoticeBase):
    """공지사항 생성 스키마"""
    pass


class NoticeResponse(NoticeBase):
    """공지사항 응답 스키마"""
    id: int
    author_id: int
    is_published: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class DocumentBase(BaseModel):
    """문서 기본 스키마"""
    title: str
    description: Optional[str] = None
    file_path: str
    file_size: Optional[int] = None
    category: Optional[str] = None
    is_public: bool = False


class DocumentCreate(DocumentBase):
    """문서 생성 스키마"""
    pass


class DocumentResponse(DocumentBase):
    """문서 응답 스키마"""
    id: int
    uploader_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class ScheduleBase(BaseModel):
    """일정 기본 스키마"""
    title: str
    description: Optional[str] = None
    start_date: datetime
    end_date: Optional[datetime] = None
    location: Optional[str] = None
    is_all_day: bool = False


class ScheduleCreate(ScheduleBase):
    """일정 생성 스키마"""
    pass


class ScheduleResponse(ScheduleBase):
    """일정 응답 스키마"""
    id: int
    creator_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
