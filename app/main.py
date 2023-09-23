# coding: utf-8
"""Web server module."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.config import get_configs

settings = get_configs()
session_key = settings.get("sessions-keys", "session_secret_key")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def homepage():
    return {"message": "Welcome to Cart API"}


app.add_middleware(SessionMiddleware, secret_key=session_key)
