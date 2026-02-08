from fastapi import Request
from fastapi.responses import JSONResponse
from config import logger

async def global_exception_handler(request: Request, e: Exception):
    logger.exception(f"Unhandled exception: {e}")
    
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message" : "Something went wrong"
        }
    )