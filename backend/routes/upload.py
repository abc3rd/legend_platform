# routes/upload.py

from fastapi import APIRouter, UploadFile, File
import os
from pathlib import Path
from datetime import datetime

router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_DIR = Path("static/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/")
async def upload_files(files: list[UploadFile] = File(...)):
    results = []
    for file in files:
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        filename = f\"{timestamp}_{file.filename.replace(' ', '_')}\"
        filepath = UPLOAD_DIR / filename

        with open(filepath, \"wb\") as buffer:
            buffer.write(await file.read())

        results.append({\"filename\": filename, \"saved_to\": str(filepath)})

    return {
        \"status\": \"success\",
        \"files_uploaded\": results
    }
