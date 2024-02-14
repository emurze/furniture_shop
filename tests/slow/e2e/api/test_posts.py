from starlette.testclient import TestClient


def test_posts(client: TestClient) -> None:
    response = client.get("/posts/")
    assert response.status_code == 200
    # assert response.json()
