import random

from flask import Blueprint, abort, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app import db
from app.data import AVATARS, DEFAULT_QUIZ_SLUG, EVENTS, QUIZ_QUESTIONS
from app.event_images import EVENT_IMAGES, IMAGE_TYPE_INFO, cover_image
from app.events import (
    all_categories,
    events_list,
    find_todays_event,
    search_events,
    today_french_label,
    years_ago,
)
from app.progress import badges_for, eras_progress, level_info

main_bp = Blueprint("main", __name__)

ERAS = [
    {"key": "prehistoire", "name": "Préhistoire", "range": "-3M à -3000", "description": "L'aube de l'humanité et les premières expressions artistiques."},
    {"key": "antiquite", "name": "Antiquité", "range": "-3000 à 476", "description": "L'essor des grandes civilisations et de l'écriture."},
    {"key": "moyen-age", "name": "Moyen Âge", "range": "476 à 1492", "description": "Châteaux, chevaliers et expansion spirituelle."},
    {"key": "renaissance", "name": "Renaissance", "range": "1492 à 1789", "description": "Renouveau artistique, scientifique et grandes découvertes."},
    {"key": "epoque-contemporaine", "name": "Époque Contemporaine", "range": "1789 à aujourd'hui", "description": "Révolutions, guerres mondiales et conquête spatiale."},
]


class QuizResult:
    def __init__(self, chosen_index: int, correct: bool):
        self.chosen_index = chosen_index
        self.correct = correct


@main_bp.route("/")
@login_required
def home():
    event, is_exact_match = find_todays_event()
    return render_template(
        "pages/home.html",
        event=event,
        is_exact_match=is_exact_match,
        today_label=today_french_label(),
        years_ago=years_ago(event) if is_exact_match else None,
        other_events=[e for e in events_list(chronological=True) if e["slug"] != event["slug"]][:2],
        active_page="home",
        level=level_info(current_user),
        badges=badges_for(current_user),
    )


@main_bp.route("/explorer")
@login_required
def explorer():
    event, _ = find_todays_event()
    query = request.args.get("q", "").strip()
    category = request.args.get("category", "Tous")
    era_key = request.args.get("era_key", "")
    view = request.args.get("view", "frise")

    has_filter = bool(query or category != "Tous" or era_key)
    results = search_events(query=query, category=category, era_key=era_key) if has_filter else None
    map_events = [e for e in events_list(chronological=True) if e.get("map_pos")]

    collections = [
        EVENTS["chute-empire-romain-occident"],
        EVENTS["invention-machine-vapeur-watt"],
        EVENTS["decouverte-tombe-toutankhamon"],
    ]
    return render_template(
        "pages/explorer.html",
        event=event,
        eras=ERAS,
        collections=collections,
        results=results,
        query=query,
        category=category,
        era_key=era_key,
        categories=["Tous"] + all_categories(),
        view=view,
        map_events=map_events,
        active_page="explorer",
    )


@main_bp.route("/evenement/<slug>")
@login_required
def event_detail(slug):
    event = EVENTS.get(slug)
    if event is None:
        abort(404)
    return render_template(
        "pages/event_detail.html",
        event=event,
        years_ago=years_ago(event),
        images=EVENT_IMAGES.get(slug, {}),
        cover=cover_image(slug),
        active_page="explorer",
    )


@main_bp.route("/evenement/<slug>/image/<image_type>")
@login_required
def event_image_detail(slug, image_type):
    event = EVENTS.get(slug)
    if event is None:
        abort(404)
    image = EVENT_IMAGES.get(slug, {}).get(image_type)
    if image is None:
        abort(404)
    return render_template(
        "pages/event_image_detail.html",
        event=event,
        image=image,
        image_type=image_type,
        type_info=IMAGE_TYPE_INFO[image_type],
        active_page="explorer",
    )


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
    return render_template(
        "pages/profile.html",
        active_page="profile",
        level=level_info(current_user),
        eras=eras_progress(current_user),
    )


@main_bp.route("/profil/avatar", methods=["POST"])
@login_required
def update_avatar():
    avatar_id = request.form.get("avatar_id")
    if avatar_id in AVATARS:
        current_user.avatar_id = avatar_id
        db.session.commit()
    return redirect(url_for("main.profile"))
