from starlette.testclient import TestClient


def test_publishers(client: TestClient) -> None:
    response = client.get("/publishers/")
    assert response.status_code == 200
    # assert response.json()
