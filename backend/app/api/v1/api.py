"""
API v1 라우터 통합
"""

from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, homepage, intranet

api_router = APIRouter()

# 인증 관련 라우터
api_router.include_router(auth.router, prefix="/auth", tags=["인증"])

# 사용자 관련 라우터
api_router.include_router(users.router, prefix="/users", tags=["사용자"])

# 홈페이지 관련 라우터
api_router.include_router(homepage.router, prefix="/homepage", tags=["홈페이지"])

# 인트라넷 관련 라우터
api_router.include_router(intranet.router, prefix="/intranet", tags=["인트라넷"])
