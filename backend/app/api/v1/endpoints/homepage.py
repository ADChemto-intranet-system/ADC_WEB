"""
홈페이지 관련 API 엔드포인트
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.homepage import NewsCreate, NewsResponse, ContactCreate, ContactResponse
from app.models.homepage import News, Contact

router = APIRouter()


# 뉴스/공지사항 관련
@router.get("/news", response_model=List[NewsResponse])
async def get_news(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """뉴스/공지사항 목록 조회"""
    news = db.query(News).offset(skip).limit(limit).all()
    return news


@router.get("/news/{news_id}", response_model=NewsResponse)
async def get_news_detail(news_id: int, db: Session = Depends(get_db)):
    """뉴스/공지사항 상세 조회"""
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="뉴스를 찾을 수 없습니다."
        )
    return news


@router.post("/news", response_model=NewsResponse)
async def create_news(news: NewsCreate, db: Session = Depends(get_db)):
    """새 뉴스/공지사항 생성"""
    db_news = News(**news.dict())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news


# 고객 문의 관련
@router.post("/contact", response_model=ContactResponse)
async def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    """고객 문의 등록"""
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


@router.get("/contact", response_model=List[ContactResponse])
async def get_contacts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """고객 문의 목록 조회 (관리자용)"""
    contacts = db.query(Contact).offset(skip).limit(limit).all()
    return contacts
