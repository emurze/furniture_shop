from starlette.testclient import TestClient

from tests.slow.e2e.api.conftest import make_publisher, make_post, post_data


def test_get_post(client: TestClient) -> None:
    make_publisher(client)
    make_post(client)

    response = client.get("/posts/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1} | post_data


def test_add_post(client: TestClient) -> None:
    make_publisher(client)
    response = make_post(client)

    assert response.status_code == 200
    assert response.json() == 1


def test_get_posts(client: TestClient) -> None:
    make_publisher(client)
    make_post(client)
    make_post(client)

    response = client.get("/posts/")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1} | post_data,
        {"id": 2} | post_data,
    ]
