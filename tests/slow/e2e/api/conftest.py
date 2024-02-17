from httpx import Response
from starlette.testclient import TestClient

publisher_data = {
    "name": "Publisher 1",
    "city": "Lersk",
}
post_data = {
    "title": "Post 1",
    "content": "",
    "publisher_id": 1,
    "draft": False,
}


def make_publisher(client: TestClient) -> Response:
    response = client.post("/publishers/", json=publisher_data)
    return response


def make_post(client: TestClient) -> Response:
    response = client.post("/posts/", json=post_data)
    return response
