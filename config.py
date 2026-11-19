import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise RuntimeError(
            "SECRET_KEY is not set. Copy .env.example to .env and set a random SECRET_KEY."
        )

    def _normalized_database_uri() -> str:
        """Force the psycopg2 dialect regardless of the URL scheme given.

        requirements.txt installs psycopg2-binary, not psycopg (v3). Some
        providers (Supabase included) hand out connection strings using
        "postgres://" (Heroku-style, deprecated by SQLAlchemy) or
        "postgresql+psycopg://" (the v3 dialect) -- either one makes
        SQLAlchemy try to import a driver that isn't installed here
        ("ModuleNotFoundError: No module named 'psycopg'"), so normalize
        to "postgresql+psycopg2://" no matter what scheme was configured.
        """
        url = os.environ.get("DATABASE_URL")
        if not url:
            return f"sqlite:///{os.path.join(basedir, 'instance', 'chronos.db')}"
        if url.startswith("postgres://"):
            url = "postgresql://" + url[len("postgres://") :]
        if url.startswith("postgresql://"):
            url = "postgresql+psycopg2://" + url[len("postgresql://") :]
        elif url.startswith("postgresql+psycopg://"):
            url = "postgresql+psycopg2://" + url[len("postgresql+psycopg://") :]
        return url

    SQLALCHEMY_DATABASE_URI = _normalized_database_uri()
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
