import os
import tempfile

import pytest

# Config reads these at first import, so they must be set before `app` (and
# transitively `config.Config`) is imported anywhere -- including by other
# test modules collected before this fixture file runs.
os.environ.setdefault("SECRET_KEY", "test-secret-key-not-for-production")
os.environ.setdefault(
    "DATABASE_URL", f"sqlite:///{os.path.join(tempfile.gettempdir(), 'chronos_test.db')}"
)
os.environ.setdefault("FLASK_ENV", "testing")

from app import create_app, db  # noqa: E402
from app.models import User  # noqa: E402


@pytest.fixture()
def app():
    flask_app = create_app()
    flask_app.config.update(TESTING=True, WTF_CSRF_ENABLED=False, RATELIMIT_ENABLED=False)
    with flask_app.app_context():
        db.drop_all()
        db.create_all()

        from app.seed import seed_event_level_content, seed_events

        seed_events()
        seed_event_level_content()

        yield flask_app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def user(app):
    with app.app_context():
        u = User(username="tester", email="tester@example.com", study_level="etudiant_adulte")
        u.set_password("Test1234!")
        db.session.add(u)
        db.session.commit()
        return u.id


@pytest.fixture()
def auth_client(client, user):
    with client.session_transaction() as sess:
        sess["_user_id"] = str(user)
        sess["_fresh"] = True
    return client
