from fastapi import Header, HTTPException
from fastapi.responses import JSONResponse
from config import settings


def verify_api_key(api_key: str = Header(...)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized request")
    return True
