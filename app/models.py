from datetime import date, datetime, timezone

from flask import current_app
from flask_login import UserMixin
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer
from werkzeug.security import check_password_hash, generate_password_hash

from app import db

STUDY_LEVELS = ("enfant", "college", "lycee", "etudiant_adulte")
RESET_TOKEN_SALT = "password-reset"


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
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def set_password(self, raw_password: str) -> None:
        self.password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password: str) -> bool:
        return check_password_hash(self.password_hash, raw_password)

    def get_reset_token(self, expires_sec: int = 1800) -> str:
        serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        return serializer.dumps({"user_id": self.id}, salt=RESET_TOKEN_SALT)

    @staticmethod
    def verify_reset_token(token: str, expires_sec: int = 1800):
        serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        try:
            data = serializer.loads(token, salt=RESET_TOKEN_SALT, max_age=expires_sec)
        except (BadSignature, SignatureExpired):
            return None
        return db.session.get(User, data.get("user_id"))

    def record_quiz_win(self, xp_reward: int = 20, token_reward: int = 5) -> None:
        today = date.today()
        if self.last_quiz_date != today:
            self.streak_days = (self.streak_days + 1) if self.last_quiz_date else 1
            self.last_quiz_date = today
        self.xp += xp_reward
        self.tokens += token_reward

    def __repr__(self):
        return f"<User {self.username}>"
