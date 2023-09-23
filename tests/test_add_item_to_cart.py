# coding: utf-8
"""Test server module."""

from fastapi import status
import responses
import copy


@responses.activate
def test_add_item_in_cart(test_app, user_headers):
    """Should success and return 201 for code status."""
    responses.add(
        method=responses.POST,
        url="http://localhost:8000/check_incomming_http_traffic",
        json={"status": "Granted"},
        status=201,
    )

    product = {
        "item": {"reference": "ref-1", "name": "Tshirt Vintage", "price": 15.5},
        "quantity": 2,
    }
    response = test_app.post(
        "/cart",
        headers=user_headers,
        json=product,
    )
    assert response.status_code == status.HTTP_201_CREATED


@responses.activate
def test_add_item_in_cart_from_suspect_http_signal(test_app, user_headers):
    """Should failed and return 403 for code status."""
    responses.add(
        method=responses.POST,
        url="http://localhost:8000/check_incomming_http_traffic",
        json={"status": "Denied"},
        status=403,
    )

    headers = copy.deepcopy(user_headers)
    headers["User-Agent"] = "Googlebot"
    product = {
        "item": {"reference": "ref-1", "name": "Tshirt Vintage", "price": 15.5},
        "quantity": 2,
    }

    response = test_app.post(
        "/cart",
        headers=headers,
        json=product,
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json() == {"detail": "Bot detected"}
