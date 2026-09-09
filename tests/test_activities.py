from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_github_skills_activity_is_available():
    response = client.get("/activities")

    assert response.status_code == 200
    assert "GitHub Skills" in response.json()


def test_github_skills_activity_signup_works():
    response = client.post(
        "/activities/GitHub%20Skills/signup?email=student@mergington.edu"
    )

    assert response.status_code == 200
    assert "student@mergington.edu" in client.get("/activities").json()["GitHub Skills"]["participants"]
