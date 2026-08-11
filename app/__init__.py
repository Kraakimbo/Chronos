import logging
import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from werkzeug.middleware.proxy_fix import ProxyFix

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
mail = Mail()
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
    csrf.init_app(app)
    mail.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Connecte-toi pour continuer ton exploration."
    login_manager.login_message_category = "info"

    app.config.setdefault("RATELIMIT_ENABLED", True)
    app.config.setdefault("RATELIMIT_STORAGE_URI", "memory://")
    limiter.init_app(app)

    from app.auth.routes import auth_bp
    from app.main.routes import main_bp
    from app.public.routes import public_bp

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

    with app.app_context():
        db.create_all()

        from app.seed import seed_admin_account

        seed_admin_account()

    return app
