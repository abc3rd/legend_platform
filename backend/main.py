from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import os

from routes.query import router as query_router
from routes.upload import router as upload_router
from routes.generate_image import router as image_router
from routes.websearch import router as websearch_router

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="legend_db",
    user="postgres",
    password="Legendary123!"  # Replace with your real password
)

class QueryRequest(BaseModel):
    query: str

@app.post("/api/search")
def search_leads(request: QueryRequest):
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT username, name, email, phone, bio
        FROM leads
        WHERE bio ILIKE %s OR category ILIKE %s
        LIMIT 100;
    """, (f"%{request.query}%", f"%{request.query}%"))

    rows = cursor.fetchall()
    result = [
        {"username": r[0], "name": r[1], "email": r[2], "phone": r[3], "bio": r[4]}
        for r in rows
    ]
    return result

# Register additional routers
app.include_router(query_router)
app.include_router(upload_router)
app.include_router(image_router)
app.include_router(websearch_router)
