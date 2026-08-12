import logging
import os
import socket
import sys

import sentry_sdk
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from sentry_sdk.integrations.flask import FlaskIntegration
from werkzeug.middleware.proxy_fix import ProxyFix

load_dotenv()

# Defensive default: bounds any socket the process opens that doesn't set
# its own timeout, so a stalled network call can't hang a request (and
# eventually the whole gunicorn worker) forever.
socket.setdefaulttimeout(10)

# Opt-in error monitoring: unset SENTRY_DSN locally/in tests to skip this
# entirely (nothing is sent anywhere without it configured).
if os.environ.get("SENTRY_DSN"):
    sentry_sdk.init(
        dsn=os.environ["SENTRY_DSN"],
        integrations=[FlaskIntegration()],
        environment=os.environ.get("FLASK_ENV", "development"),
        # Error tracking only -- no performance/trace sampling, to keep
        # this simple and stay comfortably within Sentry's free tier.
        traces_sample_rate=0.0,
    )

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()
# In-memory storage: fine for a single-process deploy. If Chronos ever runs
# with multiple gunicorn workers, this needs a shared backend (e.g. Redis)
# or each worker enforces its own separate limit.
limiter = Limiter(key_func=get_remote_address)


def create_app(config_object="config.Config"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    # Flask lazily attaches a default handler to app.logger (writing to the
    # WSGI errors stream, i.e. stderr under gunicorn) the first time it's
    # used, but leaves the logger's own level unset once debug=False, which
    # defaults to WARNING — so app.logger.info() calls (bootstrap admin
    # creation, password-reset links when no SMTP is configured) silently
    # vanish in production. Force INFO through explicitly.
    if not app.debug:
        app.logger.setLevel(logging.INFO)

    # Render (and most PaaS) terminate TLS at a reverse proxy and forward
    # plain HTTP internally: trust its X-Forwarded-* headers so
    # request.is_secure and url_for(_external=True) reflect https.
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Connecte-toi pour continuer ton exploration."
    login_manager.login_message_category = "info"

    app.config.setdefault("RATELIMIT_ENABLED", True)
    app.config.setdefault("RATELIMIT_STORAGE_URI", "memory://")
    limiter.init_app(app)

    from app.admin.routes import admin_bp
    from app.auth.routes import auth_bp
    from app.main.routes import main_bp
    from app.public.routes import public_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(public_bp)

    from app.data import AVATARS
    from app.event_images import IMAGE_TYPE_INFO, cover_image
    from app.character_images import character_image

    @app.context_processor
    def inject_avatars():
        return {"avatars": AVATARS}

    @app.context_processor
    def inject_event_images():
        return {
            "cover_image_for": cover_image,
            "image_type_info": IMAGE_TYPE_INFO,
            "character_image_for": character_image,
        }

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(_error):
        return render_template("errors/500.html"), 500

    # Schema is managed by Flask-Migrate (see Procfile: `flask db upgrade`
    # runs before gunicorn starts) rather than db.create_all(), which only
    # creates missing tables and silently leaves new columns on existing
    # tables unapplied -- exactly what broke the users.email_confirmed
    # rollout. Tests are the one exception: they want a throwaway schema
    # that always matches the current models, not a migration history.
    with app.app_context():
        if os.environ.get("FLASK_ENV") == "testing":
            db.create_all()

        # Skip when invoked as `flask db ...`: Flask-Migrate loads this same
        # factory to introspect models, before any migration has run --
        # querying tables here would fail on a database that doesn't have
        # them yet (or, for `db migrate`, isn't even meant to be touched).
        if "db" not in sys.argv:
            from app.seed import (
                seed_admin_account,
                seed_event_images,
                seed_event_level_content,
                seed_events,
            )

            seed_admin_account()
            seed_events()
            seed_event_level_content()
            seed_event_images()

    return app
