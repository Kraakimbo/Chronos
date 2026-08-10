from urllib.parse import urlparse

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app import db
from app.auth.forms import LoginForm, RegistrationForm, RequestResetForm, ResetPasswordForm
from app.email import send_reset_email
from app.models import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


def _is_safe_redirect_target(target: str) -> bool:
    if not target:
        return False
    ref_url = urlparse(request.host_url)
    test_url = urlparse(target)
    return test_url.scheme in ("", "http", "https") and ref_url.netloc == test_url.netloc


@auth_bp.route("/inscription", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data.strip(),
            email=form.email.data.strip().lower(),
            study_level=form.study_level.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash("Bienvenue dans Chronos ! Ton compte a été créé.", "success")
        return redirect(url_for("main.home"))

    return render_template("auth/register.html", form=form)


@auth_bp.route("/connexion", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = LoginForm()
    if form.validate_on_submit():
        identifier = form.identifier.data.strip()
        user = User.query.filter(
            (User.username == identifier) | (User.email == identifier.lower())
        ).first()

        if user is None or not user.check_password(form.password.data):
            flash("Identifiant ou mot de passe incorrect.", "error")
            return render_template("auth/login.html", form=form)

        login_user(user, remember=form.remember_me.data)
        flash(f"Content de te revoir, {user.username} !", "success")

        next_page = request.args.get("next")
        if next_page and _is_safe_redirect_target(next_page):
            return redirect(next_page)
        return redirect(url_for("main.home"))

    return render_template("auth/login.html", form=form)


@auth_bp.route("/deconnexion")
@login_required
def logout():
    logout_user()
    flash("À bientôt sur Chronos !", "info")
    return redirect(url_for("auth.login"))


@auth_bp.route("/mot-de-passe-oublie", methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.strip().lower()).first()
        if user:
            send_reset_email(user)
        # Same message whether or not the account exists, to avoid leaking
        # which emails are registered.
        flash(
            "Si un compte existe avec cet email, un lien de réinitialisation "
            "vient d'être envoyé.",
            "info",
        )
        return redirect(url_for("auth.login"))

    return render_template("auth/reset_request.html", form=form)


@auth_bp.route("/reinitialiser/<token>", methods=["GET", "POST"])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    user = User.verify_reset_token(token)
    if user is None:
        flash("Ce lien de réinitialisation est invalide ou a expiré.", "error")
        return redirect(url_for("auth.reset_request"))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash("Ton mot de passe a été mis à jour, tu peux te connecter.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/reset_password.html", form=form)
