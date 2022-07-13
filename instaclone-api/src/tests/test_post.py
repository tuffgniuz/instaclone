from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_valid_id():
    response = client.get('/api/v1/posts/1')
    assert response.status_code == 200
