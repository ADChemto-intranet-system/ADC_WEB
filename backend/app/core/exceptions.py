"""
커스텀 예외 처리
"""

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

logger = logging.getLogger(__name__)


class ADChemtoException(Exception):
    """ADChemto 커스텀 예외"""
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


def setup_exception_handlers(app: FastAPI):
    """예외 처리기 설정"""
    
    @app.exception_handler(ADChemtoException)
    async def adchemto_exception_handler(request: Request, exc: ADChemtoException):
        """ADChemto 커스텀 예외 처리"""
        logger.error(f"ADChemto Exception: {exc.message}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": "ADChemto Error",
                "message": exc.message,
                "status_code": exc.status_code
            }
        )
    
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        """HTTP 예외 처리"""
        logger.error(f"HTTP Exception: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": "HTTP Error",
                "message": exc.detail,
                "status_code": exc.status_code
            }
        )
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """요청 검증 예외 처리"""
        logger.error(f"Validation Error: {exc.errors()}")
        return JSONResponse(
            status_code=422,
            content={
                "error": "Validation Error",
                "message": "입력 데이터가 올바르지 않습니다.",
                "details": exc.errors()
            }
        )
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """일반 예외 처리"""
        logger.error(f"Unexpected Error: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={
                "error": "Internal Server Error",
                "message": "서버 내부 오류가 발생했습니다.",
                "status_code": 500
            }
        )
