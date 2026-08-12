from unittest.mock import patch

import requests

from app.email import send_confirmation_email, send_reset_email
from app.models import User


def test_send_reset_email_logs_link_when_no_api_key(app, user):
    with app.test_request_context():
        u = User.query.get(user)
        with patch("app.email.requests.post") as mock_post:
            send_reset_email(u)
        mock_post.assert_not_called()


def test_send_reset_email_posts_to_brevo_api(app, user):
    with app.test_request_context():
        app.config["BREVO_API_KEY"] = "fake-key"
        u = User.query.get(user)
        with patch("app.email.requests.post") as mock_post:
            mock_post.return_value.raise_for_status.return_value = None
            send_reset_email(u)

        assert mock_post.call_args.args[0] == "https://api.brevo.com/v3/smtp/email"
        assert mock_post.call_args.kwargs["headers"]["api-key"] == "fake-key"
        assert mock_post.call_args.kwargs["json"]["to"] == [{"email": u.email}]


def test_send_reset_email_swallows_request_errors(app, user):
    with app.test_request_context():
        app.config["BREVO_API_KEY"] = "fake-key"
        u = User.query.get(user)
        with patch("app.email.requests.post", side_effect=requests.ConnectionError("timed out")):
            send_reset_email(u)  # must not raise


def test_send_confirmation_email_logs_link_when_no_api_key(app, user):
    with app.test_request_context():
        u = User.query.get(user)
        with patch("app.email.requests.post") as mock_post:
            send_confirmation_email(u)
        mock_post.assert_not_called()


def test_send_confirmation_email_posts_to_brevo_api(app, user):
    with app.test_request_context():
        app.config["BREVO_API_KEY"] = "fake-key"
        u = User.query.get(user)
        with patch("app.email.requests.post") as mock_post:
            mock_post.return_value.raise_for_status.return_value = None
            send_confirmation_email(u)

        assert mock_post.call_args.args[0] == "https://api.brevo.com/v3/smtp/email"
        assert mock_post.call_args.kwargs["json"]["to"] == [{"email": u.email}]


def test_send_confirmation_email_swallows_request_errors(app, user):
    with app.test_request_context():
        app.config["BREVO_API_KEY"] = "fake-key"
        u = User.query.get(user)
        with patch("app.email.requests.post", side_effect=requests.ConnectionError("timed out")):
            send_confirmation_email(u)  # must not raise
