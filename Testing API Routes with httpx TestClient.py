
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_analyze_event():
    payload = {
        "description": "Artificial Intelligence Conference"
    }

    response = client.post("/analyze-event", json=payload)

    assert response.status_code == 200
    assert "themes" in response.json()


def test_fact_check():
    payload = {
        "query": "Artificial Intelligence"
    }

    response = client.post("/fact-check", json=payload)

    assert response.status_code == 200


def test_generate_conversation():
    payload = {
        "event_description": "AI Networking Event",
        "interests": ["Machine Learning", "Python"]
    }

    response = client.post(
        "/generate-conversation",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "themes" in data
    assert "suggestions" in data


def test_invalid_request_returns_422():
    response = client.post(
        "/analyze-event",
        json={}
    )

    assert response.status_code == 422