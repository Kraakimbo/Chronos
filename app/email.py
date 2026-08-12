import smtplib

from flask import current_app, render_template, url_for
from flask_mail import Message

from app import mail


def send_reset_email(user) -> None:
    token = user.get_reset_token()
    reset_url = url_for("auth.reset_token", token=token, _external=True)

    if not current_app.config.get("MAIL_SERVER"):
        # No SMTP configured (e.g. local dev): log the link instead of
        # failing, so the reset flow stays testable without real email.
        current_app.logger.info(
            "MAIL_SERVER non configuré — lien de réinitialisation pour %s : %s",
            user.email,
            reset_url,
        )
        return

    msg = Message(
        "Réinitialisation de ton mot de passe Chronos",
        sender=current_app.config["MAIL_DEFAULT_SENDER"],
        recipients=[user.email],
    )
    msg.body = render_template("email/reset_password.txt", user=user, reset_url=reset_url)
    try:
        mail.send(msg)
    except (smtplib.SMTPException, OSError, TimeoutError):
        # A flaky SMTP provider must not turn into a 500 for the user, and
        # the caller always shows the same "if an account exists..."
        # message regardless of outcome (no account enumeration) -- so it's
        # safe to swallow this and just log it for us to investigate.
        current_app.logger.exception(
            "Échec de l'envoi de l'email de réinitialisation à %s", user.email
        )
