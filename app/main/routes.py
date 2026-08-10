import random

from flask import Blueprint, abort, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app import db
from app.data import AVATARS, DEFAULT_QUIZ_SLUG, EVENTS, QUIZ_QUESTIONS, TODAY_EVENT_SLUG

main_bp = Blueprint("main", __name__)


class QuizResult:
    def __init__(self, chosen_index: int, correct: bool):
        self.chosen_index = chosen_index
        self.correct = correct


@main_bp.route("/")
@login_required
def home():
    event = EVENTS[TODAY_EVENT_SLUG]
    return render_template("pages/home.html", event=event, active_page="home")


@main_bp.route("/explorer")
@login_required
def explorer():
    event = EVENTS[TODAY_EVENT_SLUG]
    eras = [
        {"key": "prehistoire", "name": "Préhistoire", "range": "-3M à -3000", "description": "L'aube de l'humanité et les premières expressions artistiques."},
        {"key": "antiquite", "name": "Antiquité", "range": "-3000 à 476", "description": "L'essor des grandes civilisations et de l'écriture."},
        {"key": "moyen-age", "name": "Moyen Âge", "range": "476 à 1492", "description": "Châteaux, chevaliers et expansion spirituelle."},
        {"key": "renaissance", "name": "Renaissance", "range": "1492 à 1789", "description": "Renouveau artistique, scientifique et grandes découvertes."},
    ]
    return render_template("pages/explorer.html", event=event, eras=eras, active_page="explorer")


@main_bp.route("/evenement/<slug>")
@login_required
def event_detail(slug):
    event = EVENTS.get(slug)
    if event is None:
        abort(404)
    return render_template("pages/event_detail.html", event=event, active_page="explorer")


@main_bp.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    result = None

    if request.method == "POST":
        slug = request.form.get("question_slug")
        question = QUIZ_QUESTIONS.get(slug)
        if question is None:
            abort(400)

        try:
            chosen_index = int(request.form["answer_index"])
        except (KeyError, ValueError):
            abort(400)

        correct = chosen_index == question["correct_index"]
        if correct:
            current_user.record_quiz_win()
            db.session.commit()
        result = QuizResult(chosen_index=chosen_index, correct=correct)
    else:
        question = QUIZ_QUESTIONS[random.choice(list(QUIZ_QUESTIONS))]

    return render_template("pages/quiz.html", question=question, result=result, active_page="quiz")


@main_bp.route("/profil")
@login_required
def profile():
    return render_template("pages/profile.html", active_page="profile")


@main_bp.route("/profil/avatar", methods=["POST"])
@login_required
def update_avatar():
    avatar_id = request.form.get("avatar_id")
    if avatar_id in AVATARS:
        current_user.avatar_id = avatar_id
        db.session.commit()
    return redirect(url_for("main.profile"))
