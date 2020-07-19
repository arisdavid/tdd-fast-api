import logging

from fastapi import APIRouter

logging.basicConfig(level=logging.INFO)

router = APIRouter()


@router.get("/ping")
async def pong():
    return {"ping": "pong!"}
