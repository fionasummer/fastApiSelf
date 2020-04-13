from fastapi import APIRouter
from fastapi import FastAPI, File
from pydantic import BaseModel

router = APIRouter()


class Down(BaseModel):
    filekey: str
    host: str
    port: str


@router.post('/download', response_model=Down)
async def download(file: bytes = File(...)):
    return {"file_size": len(file)}
