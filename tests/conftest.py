# coding: utf-8
"""."""

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope="function")
def test_app():
    """."""
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="function")
def user_headers(test_app):
    """."""
    headers = {
        "Host": "http://localhost",
        "User-Agent": "insomnia/2023.5.8",
        "Content-Type": "application/json",
        "X-User-Id": "user_test",
    }
    return headers
