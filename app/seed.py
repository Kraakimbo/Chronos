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
            username=username,
            email=email,
            study_level=study_level,
            email_confirmed=True,
            is_admin=True,
        )
        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()
        current_app.logger.info(
            "Compte admin bootstrap créé : %s (%s)", username, email
        )


def seed_events() -> None:
    """Populate historical_events from app.data.EVENTS, once.

    A no-op once the table has any row: after the first deploy, the
    database (not app/data.py) is the source of truth, so admin edits
    made via /admin/evenements are never overwritten by a redeploy.
    """
    from app.data import EVENTS
    from app.models import HistoricalEvent

    if HistoricalEvent.query.first() is not None:
        return

    for slug, event in EVENTS.items():
        map_pos = event.get("map_pos")
        db.session.add(
            HistoricalEvent(
                slug=slug,
                title=event["title"],
                month=event["month"],
                day=event["day"],
                year=event["year"],
                date_label=event["date_label"],
                era=event["era"],
                era_key=event["era_key"],
                category=event["category"],
                location=event["location"],
                location_label=event.get("location_label"),
                map_pos_x=map_pos[0] if map_pos else None,
                map_pos_y=map_pos[1] if map_pos else None,
                summary=event["summary"],
                before=event["before"],
                during=event["during"],
                after=event["after"],
                narrative=event.get("narrative", []),
                why_it_matters=event["why_it_matters"],
                characters=event.get("characters", []),
                quiz_slug=event.get("quiz_slug"),
                approximate=bool(event.get("approximate")),
            )
        )
    db.session.commit()
    current_app.logger.info("%d événements historiques importés en base.", len(EVENTS))


def seed_event_level_content() -> None:
    """Populate event_level_content from app.level_content.CONTENT_BY_LEVEL, once.

    Same one-time-only rule as seed_events: a no-op once the table has any
    row, so admin edits (per event, per study level) survive redeploys.
    """
    from app.level_content import CONTENT_BY_LEVEL
    from app.models import EventLevelContent

    if EventLevelContent.query.first() is not None:
        return

    count = 0
    for slug, by_level in CONTENT_BY_LEVEL.items():
        for level, text in by_level.items():
            db.session.add(
                EventLevelContent(
                    event_slug=slug,
                    level=level,
                    summary=text["summary"],
                    before=text["before"],
                    during=text["during"],
                    after=text["after"],
                    narrative=text.get("narrative", []),
                    why_it_matters=text["why_it_matters"],
                )
            )
            count += 1
    db.session.commit()
    current_app.logger.info("%d textes par niveau d'étude importés en base.", count)


def seed_event_images() -> None:
    """Populate event_images from app.event_images.EVENT_IMAGES, once.

    Same one-time-only rule as seed_events: a no-op once the table has
    any row, so admin edits (per event, per image type) survive redeploys.
    """
    from app.event_images import EVENT_IMAGES
    from app.models import EventImage

    if EventImage.query.first() is not None:
        return

    count = 0
    for slug, images in EVENT_IMAGES.items():
        for image_type, image in images.items():
            db.session.add(
                EventImage(
                    event_slug=slug,
                    image_type=image_type,
                    url=image["url"],
                    subject=image.get("subject"),
                    credit=image.get("credit"),
                    licence=image.get("licence"),
                )
            )
            count += 1
    db.session.commit()
    current_app.logger.info("%d illustrations d'événements importées en base.", count)
