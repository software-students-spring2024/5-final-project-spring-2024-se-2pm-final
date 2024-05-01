"""
Tests for the app module
"""

import os
import pytest

os.environ["MONGO_DBNAME"] = "Cluster0"
os.environ["MONGO_URI"] = (
    "mongodb+srv://yl7408:David205@cluster0.griovdi.mongodb.net/?retryWrites=true&w=majority"
)

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


def test_home_route(test_client):
    """
    Test home page rendering
    """
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Quiz App Homepage" in response.data


def test_invalid_route(test_client):
    """
    Test handling of invalid routes
    """
    response = test_client.get("/invalid-route")
    assert response.status_code == 404


def test_template_rendering(test_client):
    """
    Test rendering of the template
    """
    response = test_client.get("/")
    assert b"Quiz App Homepage" in response.data


def test_create_route(test_client):
    """
    Test create route
    """
    response = test_client.get("/create")
    assert response.status_code == 200


def test_delete_route(test_client):
    """
    Test delete route
    """
    response = test_client.get("/delete")
    assert response.status_code == 200
    
def test_search_route(test_client):
    """
    Test delete route
    """
    response = test_client.get("/search")
    assert response.status_code == 200

def test_create_submit_search_delete_quiz(test_client):
    """
    Test create, submit, and delete quiz
    """
    # Create Quiz
    response = test_client.post(
        "/create",
        data={
            "title": "Test Quiz",
            "question1": "Question 1",
            "answer1": "Option 1",
            "options1": "Option 1, Option 2",
        },
    )
    assert response.status_code == 302  # Redirects to home route
     # Search Quiz
    response = test_client.post(
        "/search",
        data={
            "title": "Test",
        },
    )
    assert response.status_code == 200  # Redirects to search route
    
    # Get created quiz id
    created_quiz_id = db.quizzes.find_one({"title": "Test Quiz"})["_id"]

    # Submit Quiz
    response = test_client.post(
        f"/submit_quiz/{created_quiz_id}", data={"question1": "Option 1"}
    )
    assert response.status_code == 200
    assert b"Score:" in response.data

    # Delete Quiz
    response = test_client.post("/delete", data={"quiz_ids[]": [str(created_quiz_id)]})
    assert response.status_code == 302  # Redirects to delete route
