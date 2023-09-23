# coding: utf-8
"""Test server module."""

from fastapi import status


def test_server_run_without_error(test_app):
    """Should success and return 200 for code status."""
    response = test_app.get("/")
    assert response.status_code == status.HTTP_200_OK
