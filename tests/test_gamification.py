from datetime import date, timedelta

from app import db
from app.data import QUIZ_QUESTIONS
from app.level_content import resolve_quiz
from app.models import User


def test_record_quiz_win_grants_reward_once_per_day(app):
    with app.app_context():
        u = User(username="farmer", email="farmer@example.com", study_level="etudiant_adulte")
        u.set_password("Test1234!")
        db.session.add(u)
        db.session.commit()

        assert u.record_quiz_win() is True
        assert u.xp == 20
        assert u.tokens == 5
        assert u.streak_days == 1

        # Replaying the quiz the same day must not grant XP/tokens again.
        assert u.record_quiz_win() is False
        assert u.record_quiz_win() is False
        assert u.xp == 20
        assert u.tokens == 5
        assert u.streak_days == 1

        # A genuinely new day grants the reward again and extends the streak.
        u.last_quiz_date = date.today() - timedelta(days=1)
        assert u.record_quiz_win() is True
        assert u.xp == 40
        assert u.tokens == 10
        assert u.streak_days == 2


def test_quiz_replay_same_day_does_not_grant_xp_via_route(app, auth_client, user):
    slug = next(iter(QUIZ_QUESTIONS))
    # The "tester" fixture user is "etudiant_adulte" -- resolve the same
    # level-specific variant the route itself will validate against.
    correct_index = resolve_quiz(QUIZ_QUESTIONS[slug], "etudiant_adulte")["correct_index"]

    first = auth_client.post(
        "/quiz", data={"question_slug": slug, "answer_index": str(correct_index)}
    )
    assert b"+20 XP" in first.data

    second = auth_client.post(
        "/quiz", data={"question_slug": slug, "answer_index": str(correct_index)}
    )
    assert b"+20 XP" not in second.data
    assert "d\xe9j\xe0 r\xe9cup\xe9r\xe9".encode() in second.data

    with app.app_context():
        u = db.session.get(User, user)
        assert u.xp == 20
        assert u.tokens == 5
