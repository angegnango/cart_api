# coding: utf-8
"""Web server module."""

from fastapi import FastAPI, Request, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.external_dependencies.cart_storage import get_storage
from app.use_cases.cart import add_item_to_cart
from app.entities.product import ProductLine
from datadome_module.main import check_http_traffic
import os

session_key = os.environ.get("SESSION_KEY", "session_access_key")


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


@app.post("/cart", status_code=status.HTTP_201_CREATED)
@check_http_traffic
async def add_item(request: Request, product_line: ProductLine):
    """."""
    if not request.allow_traffic:  # type: ignore
        raise HTTPException(403, detail="Bot detected")

    cart_storage = get_storage(request.headers.get("X-User-Id"))
    cart_details = add_item_to_cart(product_line.model_dump(), cart_storage)
    return {"data": {"cart_details": cart_details}}


app.add_middleware(SessionMiddleware, secret_key=session_key)
