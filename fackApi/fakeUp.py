from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
router = APIRouter()


class Up(BaseModel):
    file: bytes = File(...)
    size: int
    filename: str


@router.post('/upload')
async def upload(file: UploadFile = File(...)):
    return {"status_code": 0, "filename": file.filename}
