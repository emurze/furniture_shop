from starlette.testclient import TestClient

from tests.slow.e2e.api import conftest as utils


def test_get_publisher(client: TestClient) -> None:
    utils.make_publisher(client)

    response = client.get("/publishers/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1} | utils.publisher_data


def test_add_publisher(client: TestClient) -> None:
    response = utils.make_publisher(client)
    assert response.status_code == 200
    assert response.json() == 1


def test_get_publishers(client: TestClient) -> None:
    utils.make_publisher(client)
    utils.make_publisher(client)

    response = client.get("/publishers/")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1} | utils.publisher_data,
        {"id": 2} | utils.publisher_data,
    ]
