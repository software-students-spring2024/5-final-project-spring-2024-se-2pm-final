"""
Tests for the app module
"""

import pytest
from app import app, db


@pytest.fixture(name="test_client")
def fixure_test_client():
    """
    Create a test client for the app
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_mongodb_connection():
    """
    Test MongoDB connection
    """
    assert db.client is not None


def test_home_page(test_client):
    """
    Test home page rendering
    """
    response = test_client.get("/")
    assert response.status_code == 200
    # assert b"Quiz App Homepage" in response.data


def test_invalid_route(test_client):
    """
    Test handling of invalid routes
    """
    response = test_client.get("/invalid-route")
    assert response.status_code == 404


# def test_template_rendering(test_client):
#     """
#     Test rendering of the template
#     """
#     response = test_client.get("/")
#     assert b"Quiz App Homepage" in response.data
