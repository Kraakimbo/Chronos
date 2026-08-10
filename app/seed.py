from flask import current_app

from app import db


def seed_admin_account() -> None:
    """Create a bootstrap account from ADMIN_* env vars, if configured.

    Lets you log in without going through /auth/inscription (handy right
    after a fresh deploy where the DB is empty). No-op if the env vars
    aren't set, or if an account with that username/email already exists.
    """
    username = current_app.config.get("ADMIN_USERNAME")
    email = current_app.config.get("ADMIN_EMAIL")
    password = current_app.config.get("ADMIN_PASSWORD")

    if not (username and email and password):
        return

    from app.models import User

    email = email.strip().lower()
    existing = User.query.filter(
        (User.username == username) | (User.email == email)
    ).first()
    if existing:
        return

    admin = User(
        username=username,
        email=email,
        study_level=current_app.config.get("ADMIN_STUDY_LEVEL"),
    )
    admin.set_password(password)
    db.session.add(admin)
    db.session.commit()
    current_app.logger.info("Compte admin bootstrap créé : %s", username)
