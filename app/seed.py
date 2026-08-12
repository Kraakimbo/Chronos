import os

from flask import current_app

from app import db

MAX_BOOTSTRAP_ACCOUNTS = 10


def _bootstrap_accounts():
    """Yield (username, email, password, study_level) from ADMIN_* env vars.

    The first account uses unsuffixed names (ADMIN_USERNAME, ADMIN_EMAIL,
    ADMIN_PASSWORD). Additional accounts use a numeric suffix starting at 2
    (ADMIN_USERNAME_2, ADMIN_EMAIL_2, ADMIN_PASSWORD_2, then _3, _4, ...).
    """
    username = current_app.config.get("ADMIN_USERNAME")
    email = current_app.config.get("ADMIN_EMAIL")
    password = current_app.config.get("ADMIN_PASSWORD")
    if username and email and password:
        yield username, email, password, current_app.config.get("ADMIN_STUDY_LEVEL")

    for n in range(2, MAX_BOOTSTRAP_ACCOUNTS + 1):
        username = os.environ.get(f"ADMIN_USERNAME_{n}")
        email = os.environ.get(f"ADMIN_EMAIL_{n}")
        password = os.environ.get(f"ADMIN_PASSWORD_{n}")
        if not (username or email or password):
            continue
        if not (username and email and password):
            current_app.logger.warning(
                "Compte admin bootstrap #%d incomplet (ADMIN_USERNAME_%d / "
                "ADMIN_EMAIL_%d / ADMIN_PASSWORD_%d) — ignoré.",
                n, n, n, n,
            )
            continue
        study_level = os.environ.get(f"ADMIN_STUDY_LEVEL_{n}", "etudiant_adulte")
        yield username, email, password, study_level


def seed_admin_account() -> None:
    """Create/sync bootstrap accounts from ADMIN_* env vars, if configured.

    Lets you log in without going through /auth/inscription (handy right
    after a fresh deploy where the DB is empty).

    - If a user with the exact same username AND email already exists,
      it's treated as this same bootstrap account: its password/study
      level are re-synced to the current env var values every startup,
      so changing ADMIN_PASSWORD in Render and restarting is enough —
      no need to delete the account first.
    - If a user matches on only one of username/email (a real, unrelated
      account happens to collide), it's left untouched and logged as a
      conflict instead of being overwritten.
    """
    from app.models import User

    for username, email, password, study_level in _bootstrap_accounts():
        email = email.strip().lower()

        exact_match = User.query.filter_by(username=username, email=email).first()
        if exact_match:
            exact_match.set_password(password)
            exact_match.study_level = study_level
            db.session.commit()
            current_app.logger.info(
                "Compte admin bootstrap '%s' resynchronisé (mot de passe à "
                "jour avec ADMIN_PASSWORD actuel).",
                username,
            )
            continue

        conflict = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()
        if conflict:
            field = "identifiant" if conflict.username == username else "email"
            current_app.logger.info(
                "Compte admin bootstrap '%s' ignoré : %s déjà utilisé par "
                "le compte existant '%s' (%s).",
                username, field, conflict.username, conflict.email,
            )
            continue

        admin = User(
            username=username, email=email, study_level=study_level, email_confirmed=True
        )
        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()
        current_app.logger.info(
            "Compte admin bootstrap créé : %s (%s)", username, email
        )
