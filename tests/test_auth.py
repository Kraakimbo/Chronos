def test_home_redirects_to_login_when_anonymous(client):
    response = client.get("/")
    assert response.status_code == 302
    assert "/auth/connexion" in response.headers["Location"]


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
