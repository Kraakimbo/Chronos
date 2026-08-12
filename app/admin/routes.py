from functools import wraps

from flask import Blueprint, abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app import db
from app.admin.forms import EventEditForm, LevelContentForm
from app.models import EventLevelContent, HistoricalEvent, STUDY_LEVELS

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

LEVEL_LABELS = {
    "enfant": "Enfant (6-10 ans)",
    "college": "Collège (11-14 ans)",
    "lycee": "Lycée (15-18 ans)",
    "etudiant_adulte": "Étudiant / Adulte (+18 ans)",
}


def admin_required(view):
    @wraps(view)
    @login_required
    def wrapped(*args, **kwargs):
        if not current_user.is_admin:
            abort(404)
        return view(*args, **kwargs)

    return wrapped


def _format_narrative(paragraphs: list) -> str:
    return "\n\n".join(paragraphs or [])


def _parse_narrative(text: str) -> list:
    blocks = [block.strip() for block in text.replace("\r\n", "\n").split("\n\n")]
    return [block for block in blocks if block]


def _format_characters(characters: list) -> str:
    return "\n".join(
        f"{c.get('name', '')} | {c.get('role', '')} | {c.get('emoji', '')} | {c.get('bg', '')}"
        for c in (characters or [])
    )


def _parse_characters(text: str):
    """Returns (characters, error_message). error_message is None on success."""
    characters = []
    for line in text.replace("\r\n", "\n").split("\n"):
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 4 or not parts[0] or not parts[1]:
            return None, f'Ligne de personnage invalide : "{line}" (attendu : Nom | Rôle | Emoji | #couleur)'
        name, role, emoji, bg = parts
        characters.append({"name": name, "role": role, "emoji": emoji, "bg": bg})
    return characters, None


@admin_bp.route("/evenements")
@admin_required
def events_list():
    events = HistoricalEvent.query.order_by(HistoricalEvent.year, HistoricalEvent.month, HistoricalEvent.day).all()
    return render_template("admin/events_list.html", events=events)


@admin_bp.route("/evenements/<slug>/modifier", methods=["GET", "POST"])
@admin_required
def edit_event(slug):
    event = HistoricalEvent.query.get(slug)
    if event is None:
        abort(404)

    form = EventEditForm(obj=event)

    if form.validate_on_submit():
        characters, error = _parse_characters(form.characters.data or "")
        if error:
            flash(error, "error")
        else:
            # narrative/characters are stored as lists but edited as plain
            # text -- populate_obj would otherwise overwrite them with the
            # raw textarea strings, so convert those two explicitly after.
            form.populate_obj(event)
            event.narrative = _parse_narrative(form.narrative.data)
            event.characters = characters
            db.session.commit()
            flash(f"« {event.title} » a été mis à jour.", "success")
            return redirect(url_for("admin.events_list"))
    elif not form.is_submitted():
        form.narrative.data = _format_narrative(event.narrative)
        form.characters.data = _format_characters(event.characters)

    return render_template(
        "admin/event_edit.html",
        form=form,
        event=event,
        levels=STUDY_LEVELS,
        level_labels=LEVEL_LABELS,
    )


@admin_bp.route("/evenements/<slug>/niveau/<level>", methods=["GET", "POST"])
@admin_required
def edit_event_level(slug, level):
    event = HistoricalEvent.query.get(slug)
    if event is None or level not in STUDY_LEVELS:
        abort(404)

    row = EventLevelContent.query.filter_by(event_slug=slug, level=level).first()

    form = LevelContentForm(obj=row)
    if form.validate_on_submit():
        if row is None:
            row = EventLevelContent(event_slug=slug, level=level)
            db.session.add(row)
        row.summary = form.summary.data
        row.before = form.before.data
        row.during = form.during.data
        row.after = form.after.data
        row.narrative = _parse_narrative(form.narrative.data)
        row.why_it_matters = form.why_it_matters.data
        db.session.commit()
        flash(f"Texte niveau « {LEVEL_LABELS[level]} » mis à jour pour « {event.title} ».", "success")
        return redirect(url_for("admin.edit_event_level", slug=slug, level=level))
    elif not form.is_submitted():
        source = row if row is not None else event
        form.summary.data = source.summary
        form.before.data = source.before
        form.during.data = source.during
        form.after.data = source.after
        form.narrative.data = _format_narrative(source.narrative)
        form.why_it_matters.data = source.why_it_matters

    return render_template(
        "admin/event_level_edit.html",
        form=form,
        event=event,
        level=level,
        levels=STUDY_LEVELS,
        level_labels=LEVEL_LABELS,
        has_override=row is not None,
    )
