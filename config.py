import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise RuntimeError(
            "SECRET_KEY is not set. Copy .env.example to .env and set a random SECRET_KEY."
        )

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or (
        f"sqlite:///{os.path.join(basedir, 'instance', 'chronos.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = os.environ.get("FLASK_ENV") == "production"

    # Password-reset emails are sent through Brevo's HTTPS API rather than
    # SMTP: Render blocks outbound SMTP ports (25/465/587) on its web
    # services, so raw smtplib connections time out there. When
    # BREVO_API_KEY is unset (e.g. local dev), the reset link is logged
    # instead of emailed.
    BREVO_API_KEY = os.environ.get("BREVO_API_KEY")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER", "no-reply@chronos.app")

    # Optional bootstrap account, auto-created at startup so you can log in
    # without going through /auth/inscription. Set all three to enable it.
    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME")
    ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
    ADMIN_STUDY_LEVEL = os.environ.get("ADMIN_STUDY_LEVEL", "etudiant_adulte")
