from datetime import date, datetime, timezone

from flask import current_app
from flask_login import UserMixin
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer
from werkzeug.security import check_password_hash, generate_password_hash

from app import db

STUDY_LEVELS = ("enfant", "college", "lycee", "etudiant_adulte")
RESET_TOKEN_SALT = "password-reset"
EMAIL_CONFIRM_SALT = "email-confirmation"
EMAIL_CONFIRM_TOKEN_MAX_AGE = 60 * 60 * 24 * 3  # 3 days


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False, index=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    study_level = db.Column(db.String(32), nullable=True)
    avatar_id = db.Column(db.String(8), nullable=False, default="1")
    xp = db.Column(db.Integer, nullable=False, default=0)
    tokens = db.Column(db.Integer, nullable=False, default=0)
    streak_days = db.Column(db.Integer, nullable=False, default=0)
    last_quiz_date = db.Column(db.Date, nullable=True)
    email_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    events = db.relationship(
        "AccountEvent",
        backref="user",
        cascade="all, delete-orphan",
        order_by="AccountEvent.created_at.desc()",
    )

    def set_password(self, raw_password: str) -> None:
        self.password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password: str) -> bool:
        return check_password_hash(self.password_hash, raw_password)

    def _make_token(self, salt: str) -> str:
        serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        return serializer.dumps({"user_id": self.id}, salt=salt)

    @staticmethod
    def _verify_token(token: str, salt: str, expires_sec: int):
        serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        try:
            data = serializer.loads(token, salt=salt, max_age=expires_sec)
        except (BadSignature, SignatureExpired):
            return None
        return db.session.get(User, data.get("user_id"))

    def get_reset_token(self, expires_sec: int = 1800) -> str:
        return self._make_token(RESET_TOKEN_SALT)

    @staticmethod
    def verify_reset_token(token: str, expires_sec: int = 1800):
        return User._verify_token(token, RESET_TOKEN_SALT, expires_sec)

    def get_confirmation_token(self) -> str:
        return self._make_token(EMAIL_CONFIRM_SALT)

    @staticmethod
    def verify_confirmation_token(token: str, expires_sec: int = EMAIL_CONFIRM_TOKEN_MAX_AGE):
        return User._verify_token(token, EMAIL_CONFIRM_SALT, expires_sec)

    def record_quiz_win(self, xp_reward: int = 20, token_reward: int = 5) -> bool:
        """Grant the daily quiz reward once per calendar day.

        Returns whether this call actually granted XP/tokens, so callers can
        tell an already-claimed win from a fresh one instead of letting a
        replayed quiz farm unlimited XP.
        """
        today = date.today()
        if self.last_quiz_date == today:
            return False
        self.streak_days = (self.streak_days + 1) if self.last_quiz_date else 1
        self.last_quiz_date = today
        self.xp += xp_reward
        self.tokens += token_reward
        return True

    def __repr__(self):
        return f"<User {self.username}>"


ACCOUNT_EVENT_TYPES = (
    "signup",
    "login_success",
    "login_failed",
    "password_reset_requested",
    "password_reset_completed",
    "email_confirmed",
)

ACCOUNT_EVENT_LABELS = {
    "signup": "Création du compte",
    "login_success": "Connexion réussie",
    "login_failed": "Tentative de connexion échouée",
    "password_reset_requested": "Demande de réinitialisation du mot de passe",
    "password_reset_completed": "Mot de passe réinitialisé",
    "email_confirmed": "Email confirmé",
}


class AccountEvent(db.Model):
    __tablename__ = "account_events"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    event_type = db.Column(db.String(32), nullable=False)
    ip_address = db.Column(db.String(45), nullable=True)
    user_agent = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), index=True)

    @property
    def label(self) -> str:
        return ACCOUNT_EVENT_LABELS.get(self.event_type, self.event_type)

    def __repr__(self):
        return f"<AccountEvent {self.event_type} user={self.user_id}>"


class HistoricalEvent(db.Model):
    """A "on this day" calendar entry -- editable from /admin/evenements.

    Seeded once from app.data.EVENTS (see app.seed.seed_events) when this
    table is empty; never overwritten after that, so admin edits persist
    across deploys. app.events converts rows to plain dicts shaped exactly
    like the old EVENTS[slug] entries, so the rest of the app (search,
    templates, level_content overrides) didn't need to change.
    """

    __tablename__ = "historical_events"

    slug = db.Column(db.String(64), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    date_label = db.Column(db.String(64), nullable=False)
    era = db.Column(db.String(64), nullable=False)
    era_key = db.Column(db.String(32), nullable=False)
    category = db.Column(db.String(32), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    location_label = db.Column(db.String(255), nullable=True)
    map_pos_x = db.Column(db.Float, nullable=True)
    map_pos_y = db.Column(db.Float, nullable=True)
    summary = db.Column(db.Text, nullable=False)
    before = db.Column(db.Text, nullable=False)
    during = db.Column(db.Text, nullable=False)
    after = db.Column(db.Text, nullable=False)
    narrative = db.Column(db.JSON, nullable=False, default=list)
    why_it_matters = db.Column(db.Text, nullable=False)
    characters = db.Column(db.JSON, nullable=False, default=list)
    quiz_slug = db.Column(db.String(64), nullable=True)
    approximate = db.Column(db.Boolean, nullable=False, default=False)
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    def to_dict(self) -> dict:
        return {
            "slug": self.slug,
            "title": self.title,
            "month": self.month,
            "day": self.day,
            "year": self.year,
            "date_label": self.date_label,
            "era": self.era,
            "era_key": self.era_key,
            "category": self.category,
            "location": self.location,
            "location_label": self.location_label,
            "map_pos": (
                (self.map_pos_x, self.map_pos_y) if self.map_pos_x is not None else None
            ),
            "summary": self.summary,
            "before": self.before,
            "during": self.during,
            "after": self.after,
            "narrative": self.narrative or [],
            "why_it_matters": self.why_it_matters,
            "characters": self.characters or [],
            "quiz_slug": self.quiz_slug,
            "approximate": self.approximate,
        }

    def __repr__(self):
        return f"<HistoricalEvent {self.slug}>"


class EventLevelContent(db.Model):
    """Study-level-specific rewrite of one event's narrative text.

    Seeded once from app.level_content.CONTENT_BY_LEVEL (see
    app.seed.seed_event_level_content); editable per event per level from
    /admin/evenements/<slug>/niveau/<level>. Same field shape as the
    relevant subset of HistoricalEvent -- app.level_content.resolve_event_content
    merges a row's fields onto the base event dict when present.
    """

    __tablename__ = "event_level_content"
    __table_args__ = (db.UniqueConstraint("event_slug", "level", name="uq_event_level"),)

    id = db.Column(db.Integer, primary_key=True)
    event_slug = db.Column(
        db.String(64), db.ForeignKey("historical_events.slug"), nullable=False, index=True
    )
    level = db.Column(db.String(32), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    before = db.Column(db.Text, nullable=False)
    during = db.Column(db.Text, nullable=False)
    after = db.Column(db.Text, nullable=False)
    narrative = db.Column(db.JSON, nullable=False, default=list)
    why_it_matters = db.Column(db.Text, nullable=False)
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    def to_overrides(self) -> dict:
        return {
            "summary": self.summary,
            "before": self.before,
            "during": self.during,
            "after": self.after,
            "narrative": self.narrative or [],
            "why_it_matters": self.why_it_matters,
        }

    def __repr__(self):
        return f"<EventLevelContent {self.event_slug}/{self.level}>"


EVENT_IMAGE_TYPES = ("photo", "tableau", "portrait")


class EventImage(db.Model):
    """One archive image (photo/tableau/portrait) for an event's gallery.

    Seeded once from app.event_images.EVENT_IMAGES (see
    app.seed.seed_event_images); editable from
    /admin/evenements/<slug>/illustrations. app.event_images.event_images_for()
    converts rows back into the {image_type: {...}} dict shape templates
    already expect, so nothing downstream needed to change.
    """

    __tablename__ = "event_images"
    __table_args__ = (db.UniqueConstraint("event_slug", "image_type", name="uq_event_image_type"),)

    id = db.Column(db.Integer, primary_key=True)
    event_slug = db.Column(
        db.String(64), db.ForeignKey("historical_events.slug"), nullable=False, index=True
    )
    image_type = db.Column(db.String(16), nullable=False)
    url = db.Column(db.String(1024), nullable=False)
    subject = db.Column(db.String(255), nullable=True)
    description = db.Column(
        db.Text,
        nullable=True,
        doc="Per-image blurb shown on the gallery card/detail page; falls "
        "back to the generic per-type IMAGE_TYPE_INFO blurb when unset.",
    )
    credit = db.Column(db.String(255), nullable=True)
    licence = db.Column(db.String(255), nullable=True)
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    def to_dict(self) -> dict:
        return {
            "url": self.url,
            "subject": self.subject,
            "description": self.description,
            "credit": self.credit,
            "licence": self.licence,
        }

    def __repr__(self):
        return f"<EventImage {self.event_slug}/{self.image_type}>"
