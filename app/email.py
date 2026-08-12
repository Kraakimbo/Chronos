import requests
from flask import current_app, render_template, url_for

BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"


def send_reset_email(user) -> None:
    token = user.get_reset_token()
    reset_url = url_for("auth.reset_token", token=token, _external=True)

    api_key = current_app.config.get("BREVO_API_KEY")
    if not api_key:
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
        response = requests.post(
            BREVO_API_URL,
            timeout=10,
            headers={
                "api-key": api_key,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            json={
                "sender": {"email": current_app.config["MAIL_DEFAULT_SENDER"]},
                "to": [{"email": user.email}],
                "subject": "Réinitialisation de ton mot de passe Chronos",
                "textContent": body,
            },
        )
        response.raise_for_status()
    except requests.RequestException:
        # A flaky email provider must not turn into a 500 for the user, and
        # the caller always shows the same "if an account exists..."
        # message regardless of outcome (no account enumeration) -- so it's
        # safe to swallow this and just log it for us to investigate.
        current_app.logger.exception(
            "Échec de l'envoi de l'email de réinitialisation à %s", user.email
        )
