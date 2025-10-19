"""
애플리케이션 설정
"""

from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """애플리케이션 설정"""
    
    # 데이터베이스 설정
    DATABASE_URL: str = "postgresql://username:password@localhost:5432/adchemto_db"
    
    # 보안 설정
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # 서버 설정
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # 도메인 설정
    FRONTEND_URL: str = "http://localhost:3000"
    BACKEND_URL: str = "http://localhost:8000"
    
    # CORS 설정
    ALLOWED_HOSTS: List[str] = ["*"]
    
    # 프로젝트 설정
    PROJECT_NAME: str = "ADChemto API"
    VERSION: str = "1.0.0"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# 전역 설정 인스턴스
settings = Settings()
