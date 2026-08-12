from app import db
from app.models import EventImage, EventLevelContent, HistoricalEvent, User

SLUG = "prise-de-la-bastille"


def _make_admin(app):
    with app.app_context():
        u = User(username="admintester", email="admintester@example.com", is_admin=True)
        u.set_password("Test1234!")
        db.session.add(u)
        db.session.commit()
        return u.id


def test_admin_routes_require_login(client):
    response = client.get("/admin/evenements")
    assert response.status_code == 302
    assert "/auth/connexion" in response.headers["Location"]


def test_admin_routes_404_for_non_admin(client, user):
    client.post("/auth/connexion", data={"identifier": "tester", "password": "Test1234!"})
    response = client.get("/admin/evenements")
    assert response.status_code == 404


def test_admin_events_list_shows_events(app, client):
    _make_admin(app)
    client.post("/auth/connexion", data={"identifier": "admintester", "password": "Test1234!"})
    response = client.get("/admin/evenements")
    assert response.status_code == 200
    assert "La prise de la Bastille".encode() in response.data


def test_admin_can_edit_event_text(app, client):
    _make_admin(app)
    client.post("/auth/connexion", data={"identifier": "admintester", "password": "Test1234!"})

    with app.app_context():
        event = db.session.get(HistoricalEvent, SLUG)
        form_data = {
            "title": event.title,
            "day": event.day, "month": event.month, "year": event.year,
            "date_label": event.date_label,
            "era": event.era, "era_key": event.era_key, "category": event.category,
            "location": event.location, "location_label": event.location_label or "",
            "quiz_slug": event.quiz_slug or "",
            "summary": "Résumé corrigé sans tiret cadratin.",
            "before": event.before, "during": event.during, "after": event.after,
            "narrative": "\n\n".join(event.narrative),
            "why_it_matters": event.why_it_matters,
            "characters": "\n".join(
                f"{c['name']} | {c['role']} | {c['emoji']} | {c['bg']}" for c in event.characters
            ),
        }

    response = client.post(f"/admin/evenements/{SLUG}/modifier", data=form_data, follow_redirects=True)
    assert response.status_code == 200
    assert "a été mis à jour".encode() in response.data

    with app.app_context():
        assert db.session.get(HistoricalEvent, SLUG).summary == "Résumé corrigé sans tiret cadratin."

    # Public preview reflects the edit immediately (no per-level override there).
    public_response = client.get(f"/decouvrir/{SLUG}")
    assert "Résumé corrigé sans tiret cadratin.".encode() in public_response.data


def test_admin_can_edit_level_specific_text(app, client):
    _make_admin(app)
    client.post("/auth/connexion", data={"identifier": "admintester", "password": "Test1234!"})

    with app.app_context():
        row = EventLevelContent.query.filter_by(event_slug=SLUG, level="etudiant_adulte").first()
        form_data = {
            "summary": "Résumé niveau adulte corrigé.",
            "before": row.before, "during": row.during, "after": row.after,
            "narrative": "\n\n".join(row.narrative),
            "why_it_matters": row.why_it_matters,
        }

    response = client.post(
        f"/admin/evenements/{SLUG}/niveau/etudiant_adulte", data=form_data, follow_redirects=True
    )
    assert response.status_code == 200
    assert "mis à jour".encode() in response.data

    with app.app_context():
        row = EventLevelContent.query.filter_by(event_slug=SLUG, level="etudiant_adulte").first()
        assert row.summary == "Résumé niveau adulte corrigé."


def test_admin_edit_unknown_slug_404s(app, client):
    _make_admin(app)
    client.post("/auth/connexion", data={"identifier": "admintester", "password": "Test1234!"})
    response = client.get("/admin/evenements/does-not-exist/modifier")
    assert response.status_code == 404


def test_admin_edit_unknown_level_404s(app, client):
    _make_admin(app)
    client.post("/auth/connexion", data={"identifier": "admintester", "password": "Test1234!"})
    response = client.get(f"/admin/evenements/{SLUG}/niveau/pas-un-niveau")
    assert response.status_code == 404


def _empty_images_form(csrf=None):
    data = {}
    if csrf is not None:
        data["csrf_token"] = csrf
    for image_type in ("photo", "tableau", "portrait"):
        for field in ("url", "subject", "credit", "licence"):
            data[f"{image_type}_{field}"] = ""
    return data


def test_admin_can_edit_illustration(app, client):
    _make_admin(app)
    client.post("/auth/connexion", data={"identifier": "admintester", "password": "Test1234!"})

    with app.app_context():
        row = EventImage.query.filter_by(event_slug=SLUG, image_type="tableau").first()
        form_data = _empty_images_form()
        form_data["tableau_url"] = row.url
        form_data["tableau_subject"] = "Légende corrigée"
        form_data["tableau_credit"] = row.credit or ""
        form_data["tableau_licence"] = row.licence or ""

    response = client.post(
        f"/admin/evenements/{SLUG}/illustrations", data=form_data, follow_redirects=True
    )
    assert response.status_code == 200
    assert "mises à jour".encode() in response.data

    with app.app_context():
        row = EventImage.query.filter_by(event_slug=SLUG, image_type="tableau").first()
        assert row.subject == "Légende corrigée"

    event_response = client.get(f"/evenement/{SLUG}")
    assert "Légende corrigée".encode() in event_response.data


def test_admin_clearing_illustration_url_removes_it(app, client):
    _make_admin(app)
    client.post("/auth/connexion", data={"identifier": "admintester", "password": "Test1234!"})

    response = client.post(
        f"/admin/evenements/{SLUG}/illustrations", data=_empty_images_form(), follow_redirects=True
    )
    assert response.status_code == 200

    with app.app_context():
        assert EventImage.query.filter_by(event_slug=SLUG).count() == 0

    event_response = client.get(f"/evenement/{SLUG}")
    assert "Galerie d'archives".encode() not in event_response.data


def test_admin_illustrations_unknown_slug_404s(app, client):
    _make_admin(app)
    client.post("/auth/connexion", data={"identifier": "admintester", "password": "Test1234!"})
    response = client.get("/admin/evenements/does-not-exist/illustrations")
    assert response.status_code == 404
