from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check the response content
    assert response.text == '"Welcome to my awesome API!"'
