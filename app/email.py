import requests
from flask import current_app, render_template, url_for

BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"


def _send_via_brevo(to_email: str, subject: str, body: str) -> None:
    """POST to Brevo's HTTPS API. Never raises -- see callers for why."""
    response = requests.post(
        BREVO_API_URL,
        timeout=10,
        headers={
            "api-key": current_app.config["BREVO_API_KEY"],
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        json={
            "sender": {"email": current_app.config["MAIL_DEFAULT_SENDER"]},
            "to": [{"email": to_email}],
            "subject": subject,
            "textContent": body,
        },
    )
    response.raise_for_status()


def send_reset_email(user) -> None:
    token = user.get_reset_token()
    reset_url = url_for("auth.reset_token", token=token, _external=True)

    if not current_app.config.get("BREVO_API_KEY"):
        # No API key configured (e.g. local dev): log the link instead of
        # failing, so the reset flow stays testable without real email.
        current_app.logger.info(
            "BREVO_API_KEY non configuré — lien de réinitialisation pour %s : %s",
            user.email,
            reset_url,
        )
        return

    body = render_template("email/reset_password.txt", user=user, reset_url=reset_url)
    try:
        _send_via_brevo(user.email, "Réinitialisation de ton mot de passe Chronos", body)
    except requests.RequestException:
        # A flaky email provider must not turn into a 500 for the user, and
        # the caller always shows the same "if an account exists..."
        # message regardless of outcome (no account enumeration) -- so it's
        # safe to swallow this and just log it for us to investigate.
        current_app.logger.exception(
            "Échec de l'envoi de l'email de réinitialisation à %s", user.email
        )


def send_confirmation_email(user) -> None:
    token = user.get_confirmation_token()
    confirm_url = url_for("auth.confirm_email", token=token, _external=True)

    if not current_app.config.get("BREVO_API_KEY"):
        current_app.logger.info(
            "BREVO_API_KEY non configuré — lien de confirmation pour %s : %s",
            user.email,
            confirm_url,
        )
        return

    body = render_template("email/confirm_email.txt", user=user, confirm_url=confirm_url)
    try:
        _send_via_brevo(user.email, "Confirme ton email Chronos", body)
    except requests.RequestException:
        # Non-blocking signup flow (see auth.register): a failed send here
        # must not prevent the account from being usable, just get logged.
        current_app.logger.exception(
            "Échec de l'envoi de l'email de confirmation à %s", user.email
        )
