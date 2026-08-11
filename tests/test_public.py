from markupsafe import escape

from app.data import EVENTS


def test_discover_accessible_without_login(client):
    response = client.get("/decouvrir")
    assert response.status_code == 200
    assert "Se connecter".encode() in response.data


def test_discover_lists_all_events(client):
    response = client.get("/decouvrir")
    assert response.status_code == 200
    for slug in list(EVENTS)[:5]:
        assert str(escape(EVENTS[slug]["title"])).encode() in response.data


def test_discover_event_accessible_without_login(client):
    response = client.get("/decouvrir/prise-de-la-bastille")
    assert response.status_code == 200
    assert "La prise de la Bastille".encode() in response.data
    assert "Cr\xe9er un compte".encode() in response.data


def test_discover_event_has_no_quiz_or_xp_widgets(client):
    response = client.get("/decouvrir/prise-de-la-bastille")
    assert b"Quiz Quotidien" not in response.data
    assert b"XP" not in response.data


def test_discover_event_unknown_slug_404s(client):
    response = client.get("/decouvrir/does-not-exist")
    assert response.status_code == 404


def test_discover_event_has_structured_data(client):
    response = client.get("/decouvrir/prise-de-la-bastille")
    assert b'"@type": "Event"' in response.data


def test_sitemap_lists_every_event(client):
    response = client.get("/sitemap.xml")
    assert response.status_code == 200
    assert response.content_type.startswith("application/xml")
    for slug in EVENTS:
        assert f"/decouvrir/{slug}<".encode() in response.data


def test_robots_txt_allows_discover(client):
    response = client.get("/robots.txt")
    assert response.status_code == 200
    assert b"Allow: /decouvrir" in response.data
    assert b"Sitemap:" in response.data
