"""
인트라넷 관련 API 엔드포인트
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.intranet import (
    NoticeCreate, NoticeResponse,
    DocumentCreate, DocumentResponse,
    ScheduleCreate, ScheduleResponse
)
from app.models.intranet import Notice, Document, Schedule

router = APIRouter()


# 공지사항 관련
@router.get("/notices", response_model=List[NoticeResponse])
async def get_notices(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """사내 공지사항 목록 조회"""
    notices = db.query(Notice).offset(skip).limit(limit).all()
    return notices


@router.post("/notices", response_model=NoticeResponse)
async def create_notice(notice: NoticeCreate, db: Session = Depends(get_db)):
    """새 공지사항 생성"""
    db_notice = Notice(**notice.dict())
    db.add(db_notice)
    db.commit()
    db.refresh(db_notice)
    return db_notice


# 문서 관리 관련
@router.get("/documents", response_model=List[DocumentResponse])
async def get_documents(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """문서 목록 조회"""
    documents = db.query(Document).offset(skip).limit(limit).all()
    return documents


@router.post("/documents", response_model=DocumentResponse)
async def create_document(document: DocumentCreate, db: Session = Depends(get_db)):
    """새 문서 등록"""
    db_document = Document(**document.dict())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document


# 일정 관리 관련
@router.get("/schedules", response_model=List[ScheduleResponse])
async def get_schedules(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """일정 목록 조회"""
    schedules = db.query(Schedule).offset(skip).limit(limit).all()
    return schedules


@router.post("/schedules", response_model=ScheduleResponse)
async def create_schedule(schedule: ScheduleCreate, db: Session = Depends(get_db)):
    """새 일정 등록"""
    db_schedule = Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule
