"""
FastAPI Backend Application
Containerized Web App with PostgreSQL
"""

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncpg


# ── Configuration ──────────────────────────────────────────────
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

pool: asyncpg.Pool = None


# ── Models ─────────────────────────────────────────────────────
class StudentCreate(BaseModel):
    name: str
    email: str
    course: str


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    course: str


# ── Lifespan (startup / shutdown) ─────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    global pool
    # Startup: create connection pool and auto-create table
    pool = await asyncpg.create_pool(DATABASE_URL, min_size=2, max_size=10)
    async with pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL UNIQUE,
                course VARCHAR(100) NOT NULL
            );
        """)
    yield
    # Shutdown: close pool
    await pool.close()


# ── App ────────────────────────────────────────────────────────
app = FastAPI(
    title="Student Management API",
    description="A containerized FastAPI application with PostgreSQL",
    version="1.0.0",
    lifespan=lifespan,
)


# ── Endpoints ──────────────────────────────────────────────────
@app.get("/health")
async def healthcheck():
    """Health check endpoint to verify API and DB connectivity."""
    try:
        async with pool.acquire() as conn:
            await conn.fetchval("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Unhealthy: {str(e)}")


@app.post("/students", response_model=StudentResponse, status_code=201)
async def create_student(student: StudentCreate):
    """POST endpoint — Insert a new student record."""
    try:
        async with pool.acquire() as conn:
            row = await conn.fetchrow(
                """
                INSERT INTO students (name, email, course)
                VALUES ($1, $2, $3)
                RETURNING id, name, email, course
                """,
                student.name,
                student.email,
                student.course,
            )
        return dict(row)
    except asyncpg.UniqueViolationError:
        raise HTTPException(status_code=409, detail="Email already exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/students", response_model=list[StudentResponse])
async def get_students():
    """GET endpoint — Fetch all student records."""
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT id, name, email, course FROM students ORDER BY id")
    return [dict(r) for r in rows]


@app.get("/")
async def root():
    return {
        "message": "Student Management API",
        "docs": "/docs",
        "health": "/health",
    }
