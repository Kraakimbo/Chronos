from app import limiter


def test_login_is_rate_limited(app):
    app.config["RATELIMIT_ENABLED"] = True
    with app.app_context():
        limiter.reset()
    client = app.test_client()

    for _ in range(10):
        response = client.post(
            "/auth/connexion", data={"identifier": "nobody", "password": "wrong"}
        )
        assert response.status_code == 200

    blocked = client.post(
        "/auth/connexion", data={"identifier": "nobody", "password": "wrong"}
    )
    assert blocked.status_code == 429


def test_login_rate_limit_does_not_affect_other_ips(app):
    app.config["RATELIMIT_ENABLED"] = True
    with app.app_context():
        limiter.reset()
    client = app.test_client()

    for _ in range(10):
        client.post(
            "/auth/connexion",
            data={"identifier": "nobody", "password": "wrong"},
            environ_overrides={"REMOTE_ADDR": "1.1.1.1"},
        )

    response = client.post(
        "/auth/connexion",
        data={"identifier": "nobody", "password": "wrong"},
        environ_overrides={"REMOTE_ADDR": "2.2.2.2"},
    )
    assert response.status_code == 200


def test_login_get_is_never_rate_limited(app):
    app.config["RATELIMIT_ENABLED"] = True
    with app.app_context():
        limiter.reset()
    client = app.test_client()

    for _ in range(15):
        response = client.get("/auth/connexion")
        assert response.status_code == 200
