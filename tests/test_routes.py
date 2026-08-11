import pytest

from app.data import EVENTS
from app.event_images import EVENT_IMAGES


def test_home(auth_client):
    response = auth_client.get("/")
    assert response.status_code == 200


def test_explorer_default_view(auth_client):
    response = auth_client.get("/explorer")
    assert response.status_code == 200


def test_explorer_map_view(auth_client):
    response = auth_client.get("/explorer?view=carte")
    assert response.status_code == 200


def test_explorer_search(auth_client):
    response = auth_client.get("/explorer?q=bastille")
    assert response.status_code == 200
    assert "Bastille".encode() in response.data or "bastille".encode() in response.data.lower()


def test_explorer_search_no_results(auth_client):
    response = auth_client.get("/explorer?q=zzzznonexistent")
    assert response.status_code == 200


@pytest.mark.parametrize("slug", list(EVENTS.keys()))
def test_event_detail_renders(auth_client, slug):
    response = auth_client.get(f"/evenement/{slug}")
    assert response.status_code == 200


def test_event_detail_unknown_slug_404s(auth_client):
    response = auth_client.get("/evenement/does-not-exist")
    assert response.status_code == 404


@pytest.mark.parametrize(
    "slug,image_type",
    [
        (slug, image_type)
        for slug, images in EVENT_IMAGES.items()
        for image_type in images
    ],
)
def test_event_image_detail_renders(auth_client, slug, image_type):
    response = auth_client.get(f"/evenement/{slug}/image/{image_type}")
    assert response.status_code == 200
    assert response.data.count(b"<img") >= 1


def test_event_image_detail_unknown_type_404s(auth_client):
    slug = next(iter(EVENT_IMAGES))
    response = auth_client.get(f"/evenement/{slug}/image/not-a-real-type")
    assert response.status_code == 404


def test_event_image_detail_unknown_slug_404s(auth_client):
    response = auth_client.get("/evenement/does-not-exist/image/photo")
    assert response.status_code == 404


def test_quiz_page(auth_client):
    response = auth_client.get("/quiz")
    assert response.status_code == 200
