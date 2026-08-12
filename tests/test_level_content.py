import pytest
from markupsafe import escape

from app import db
from app.level_content import CONTENT_BY_LEVEL, QUIZ_BY_LEVEL
from app.models import User

PILOT_SLUGS = list(CONTENT_BY_LEVEL.keys())
LEVELS = ["enfant", "college", "lycee", "etudiant_adulte"]


def _login_as(client, app, level):
    with app.app_context():
        username = f"tester-{level}"
        u = User.query.filter_by(username=username).first()
        if u is None:
            u = User(username=username, email=f"{username}@example.com", study_level=level)
            u.set_password("Test1234!")
            db.session.add(u)
            db.session.commit()
        user_id = u.id
    with client.session_transaction() as sess:
        sess["_user_id"] = str(user_id)
        sess["_fresh"] = True
    return client


@pytest.mark.parametrize("slug", PILOT_SLUGS)
@pytest.mark.parametrize("level", LEVELS)
def test_event_detail_uses_level_specific_narrative(app, client, slug, level):
    _login_as(client, app, level)
    response = client.get(f"/evenement/{slug}")
    assert response.status_code == 200
    expected = str(escape(CONTENT_BY_LEVEL[slug][level]["summary"]))
    assert expected.encode() in response.data


def test_different_levels_get_different_text(app, client):
    slug = PILOT_SLUGS[0]
    summaries = set()
    for level in LEVELS:
        _login_as(client, app, level)
        client.get(f"/evenement/{slug}")
        summaries.add(CONTENT_BY_LEVEL[slug][level]["summary"])
    assert len(summaries) == len(LEVELS)


@pytest.mark.parametrize("level", LEVELS)
def test_quiz_answer_validated_against_the_shown_level_variant(app, client, level):
    _login_as(client, app, level)
    quiz_slug = next(iter(QUIZ_BY_LEVEL))
    correct_index = QUIZ_BY_LEVEL[quiz_slug][level]["correct_index"]

    response = client.post(
        "/quiz",
        data={"question_slug": quiz_slug, "answer_index": str(correct_index)},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert "Bonne réponse".encode() in response.data


def test_all_events_covered_by_level_content():
    from app.data import EVENTS

    assert set(EVENTS.keys()) <= set(CONTENT_BY_LEVEL.keys())


def test_resolve_event_content_falls_back_for_unknown_event(app):
    from app.level_content import resolve_event_content

    fake_event = {"slug": "not-a-real-event", "summary": "original"}
    with app.app_context():
        resolved = resolve_event_content(fake_event, "enfant")
    assert resolved == fake_event
