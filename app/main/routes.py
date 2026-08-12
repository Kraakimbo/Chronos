import random

from flask import Blueprint, abort, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app import db
from app.data import AVATARS, QUIZ_QUESTIONS
from app.event_images import EVENT_IMAGES, IMAGE_TYPE_INFO, cover_image
from app.events import (
    all_categories,
    events_list,
    find_todays_event,
    get_event,
    search_events,
    today_french_label,
    years_ago,
)
from app.level_content import resolve_event_content, resolve_quiz
from app.progress import badges_for, eras_progress, level_info

main_bp = Blueprint("main", __name__)

ERAS = [
    {
        "key": "prehistoire", "name": "Préhistoire", "range": "-3M à -3000",
        "description": "L'aube de l'humanité et les premières expressions artistiques.",
        "illustration_slug": None,
        # No event in EVENTS covers this era (the oldest, "assassinat-cesar",
        # is -44/Antiquité) so there's no existing cover image to reuse.
        # Found via web search, not opened directly -- Wikimedia Commons is
        # unreachable from this environment. See
        # Illustrations_epoques!A2 in the archives spreadsheet for the
        # sourcing note; verify before relying on it for anything but this
        # decorative background (there's an SVG fallback either way).
        "illustration_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Lascaux_painting.jpg",
    },
    {"key": "antiquite", "name": "Antiquité", "range": "-3000 à 476", "description": "L'essor des grandes civilisations et de l'écriture.", "illustration_slug": "assassinat-cesar"},
    {"key": "moyen-age", "name": "Moyen Âge", "range": "476 à 1492", "description": "Châteaux, chevaliers et expansion spirituelle.", "illustration_slug": "chute-de-constantinople"},
    {"key": "renaissance", "name": "Renaissance", "range": "1492 à 1789", "description": "Renouveau artistique, scientifique et grandes découvertes.", "illustration_slug": "arrivee-christophe-colomb"},
    {"key": "epoque-contemporaine", "name": "Époque Contemporaine", "range": "1789 à aujourd'hui", "description": "Révolutions, guerres mondiales et conquête spatiale.", "illustration_slug": "prise-de-la-bastille"},
]


class QuizResult:
    def __init__(self, chosen_index: int, correct: bool, reward_granted: bool = False):
        self.chosen_index = chosen_index
        self.correct = correct
        self.reward_granted = reward_granted


@main_bp.route("/")
def home():
    if not current_user.is_authenticated:
        return redirect(url_for("public.discover"))
    study_level = current_user.study_level
    event, is_exact_match = find_todays_event()
    other_events = [e for e in events_list(chronological=True) if e["slug"] != event["slug"]][:2]
    event = resolve_event_content(event, study_level)
    return render_template(
        "pages/home.html",
        event=event,
        is_exact_match=is_exact_match,
        today_label=today_french_label(),
        years_ago=years_ago(event) if is_exact_match else None,
        other_events=[resolve_event_content(e, study_level) for e in other_events],
        active_page="home",
        level=level_info(current_user),
        badges=badges_for(current_user),
    )


@main_bp.route("/explorer")
@login_required
def explorer():
    study_level = current_user.study_level
    query = request.args.get("q", "").strip()
    category = request.args.get("category", "Tous")
    era_key = request.args.get("era_key", "")
    view = request.args.get("view", "frise")

    has_filter = bool(query or category != "Tous" or era_key)
    results = search_events(query=query, category=category, era_key=era_key) if has_filter else None
    if results is not None:
        results = [resolve_event_content(e, study_level) for e in results]
    map_events = [
        resolve_event_content(e, study_level)
        for e in events_list(chronological=True)
        if e.get("map_pos")
    ]

    return render_template(
        "pages/explorer.html",
        eras=ERAS,
        results=results,
        query=query,
        category=category,
        era_key=era_key,
        categories=["Tous"] + all_categories(),
        view=view,
        map_events=map_events,
        timeline_events=[resolve_event_content(e, study_level) for e in events_list(chronological=True)],
        active_page="explorer",
    )


@main_bp.route("/evenement/<slug>")
@login_required
def event_detail(slug):
    event = get_event(slug)
    if event is None:
        abort(404)
    event = resolve_event_content(event, current_user.study_level)
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
    event = get_event(slug)
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
    study_level = current_user.study_level

    if request.method == "POST":
        slug = request.form.get("question_slug")
        base_question = QUIZ_QUESTIONS.get(slug)
        if base_question is None:
            abort(400)
        question = resolve_quiz(base_question, study_level)

        try:
            chosen_index = int(request.form["answer_index"])
        except (KeyError, ValueError):
            abort(400)

        correct = chosen_index == question["correct_index"]
        reward_granted = False
        if correct:
            reward_granted = current_user.record_quiz_win()
            db.session.commit()
        result = QuizResult(chosen_index=chosen_index, correct=correct, reward_granted=reward_granted)
    else:
        base_question = QUIZ_QUESTIONS[random.choice(list(QUIZ_QUESTIONS))]
        question = resolve_quiz(base_question, study_level)

    return render_template("pages/quiz.html", question=question, result=result, active_page="quiz")


@main_bp.route("/profil")
@login_required
def profile():
    return render_template(
        "pages/profile.html",
        active_page="profile",
        level=level_info(current_user),
        eras=eras_progress(current_user),
        recent_events=current_user.events[:10],
    )


@main_bp.route("/profil/avatar", methods=["POST"])
@login_required
def update_avatar():
    avatar_id = request.form.get("avatar_id")
    if avatar_id in AVATARS:
        current_user.avatar_id = avatar_id
        db.session.commit()
    return redirect(url_for("main.profile"))
