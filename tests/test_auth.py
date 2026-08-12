def test_home_redirects_to_public_discover_when_anonymous(client):
    response = client.get("/")
    assert response.status_code == 302
    assert response.headers["Location"] == "/decouvrir"


def test_register_then_login(client):
    response = client.post(
        "/auth/inscription",
        data={
            "username": "nouveau",
            "email": "nouveau@example.com",
            "password": "Test1234!",
            "confirm_password": "Test1234!",
            "study_level": "lycee",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200

    response = client.post(
        "/auth/connexion",
        data={"identifier": "nouveau", "password": "Test1234!"},
        follow_redirects=True,
    )
    assert response.status_code == 200

    response = client.get("/")
    assert response.status_code == 200


def test_login_wrong_password_stays_on_login_page(client, user):
    response = client.post(
        "/auth/connexion",
        data={"identifier": "tester", "password": "wrong-password"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert response.request.path == "/auth/connexion"


def test_register_logs_signup_event(app, client):
    client.post(
        "/auth/inscription",
        data={
            "username": "nouveau",
            "email": "nouveau@example.com",
            "password": "Test1234!",
            "confirm_password": "Test1234!",
            "study_level": "lycee",
        },
    )
    with app.app_context():
        from app.models import AccountEvent, User

        created = User.query.filter_by(username="nouveau").first()
        events = AccountEvent.query.filter_by(user_id=created.id).all()
        assert [e.event_type for e in events] == ["signup"]


def test_login_success_and_failure_are_logged(app, client, user):
    client.post("/auth/connexion", data={"identifier": "tester", "password": "wrong-password"})
    client.post("/auth/connexion", data={"identifier": "tester", "password": "Test1234!"})

    with app.app_context():
        from app.models import AccountEvent

        events = (
            AccountEvent.query.filter_by(user_id=user)
            .order_by(AccountEvent.id)
            .all()
        )
        assert [e.event_type for e in events] == ["login_failed", "login_success"]


def test_login_failure_for_unknown_identifier_is_not_logged(app, client):
    client.post("/auth/connexion", data={"identifier": "personne", "password": "wrong"})

    with app.app_context():
        from app.models import AccountEvent

        assert AccountEvent.query.count() == 0


def test_deleting_account_removes_its_events(app, client, user):
    client.post("/auth/connexion", data={"identifier": "tester", "password": "Test1234!"})
    with app.app_context():
        from app.models import AccountEvent

        assert AccountEvent.query.filter_by(user_id=user).count() >= 1

    client.post("/auth/supprimer-compte", data={"password": "Test1234!"})

    with app.app_context():
        from app.models import AccountEvent

        assert AccountEvent.query.filter_by(user_id=user).count() == 0


def test_profile_shows_recent_activity(client, user):
    client.post("/auth/connexion", data={"identifier": "tester", "password": "Test1234!"})
    response = client.get("/profil")
    assert response.status_code == 200
    assert "Activité récente".encode() in response.data


def test_new_account_is_not_email_confirmed_and_stays_usable(app, client):
    response = client.post(
        "/auth/inscription",
        data={
            "username": "nonconfirme",
            "email": "nonconfirme@example.com",
            "password": "Test1234!",
            "confirm_password": "Test1234!",
            "study_level": "lycee",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert "Confirme ton email".encode() in response.data

    with app.app_context():
        from app.models import User

        created = User.query.filter_by(username="nonconfirme").first()
        assert created.email_confirmed is False

    # Unconfirmed accounts are fully usable (non-blocking flow).
    response = client.get("/quiz")
    assert response.status_code == 200


def test_confirm_email_with_valid_token(app, client, user):
    with app.app_context():
        from app.models import User

        u = User.query.get(user)
        token = u.get_confirmation_token()

    response = client.get(f"/auth/confirmer/{token}", follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        from app.models import AccountEvent, User

        assert User.query.get(user).email_confirmed is True
        assert AccountEvent.query.filter_by(
            user_id=user, event_type="email_confirmed"
        ).count() == 1


def test_confirm_email_with_invalid_token(client):
    response = client.get("/auth/confirmer/not-a-real-token", follow_redirects=True)
    assert response.status_code == 200
    assert "invalide ou a expir".encode() in response.data


def test_resend_confirmation_requires_login(client):
    response = client.post("/auth/renvoyer-confirmation")
    assert response.status_code == 302
    assert "/auth/connexion" in response.headers["Location"]


def test_resend_confirmation_when_logged_in(client, user):
    client.post("/auth/connexion", data={"identifier": "tester", "password": "Test1234!"})
    response = client.post("/auth/renvoyer-confirmation", follow_redirects=True)
    assert response.status_code == 200
    assert "nouvel email de confirmation".encode() in response.data
