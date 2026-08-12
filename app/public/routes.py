"""Public, no-login-required surface: a read-only preview of events.

Every route in app.main is behind @login_required, which means Chronos'
entire content is invisible to search engines and to a visitor who hasn't
created an account yet -- there is nothing to demonstrate the product
before asking for a signup. This blueprint exposes a deliberately small,
read-only slice of the same content (no quiz, no XP, no personalization)
so it can be indexed and linked from search/social, with a clear call to
action to create an account for the full experience.
"""

from flask import Blueprint, abort, render_template, url_for

from app.event_images import cover_image
from app.events import all_slugs, events_list, get_event, years_ago

public_bp = Blueprint("public", __name__)


@public_bp.route("/decouvrir")
def discover():
    events = events_list(chronological=True)
    return render_template(
        "public/discover.html",
        events=events,
        meta_description=(
            "Chronos : 45 événements historiques expliqués simplement, "
            "de la Préhistoire à aujourd'hui. Consultation libre, sans compte."
        ),
    )


@public_bp.route("/decouvrir/<slug>")
def discover_event(slug):
    event = get_event(slug)
    if event is None:
        abort(404)
    return render_template(
        "public/event_detail.html",
        event=event,
        years_ago=years_ago(event),
        cover=cover_image(slug),
        meta_description=event["summary"],
        canonical_url=url_for("public.discover_event", slug=slug, _external=True),
    )


@public_bp.route("/sitemap.xml")
def sitemap():
    urls = [url_for("public.discover", _external=True)]
    urls += [
        url_for("public.discover_event", slug=slug, _external=True)
        for slug in all_slugs()
    ]
    xml = render_template("public/sitemap.xml", urls=urls)
    return xml, 200, {"Content-Type": "application/xml"}


@public_bp.route("/robots.txt")
def robots():
    lines = [
        "User-agent: *",
        "Allow: /decouvrir",
        "Disallow: /profil",
        "Disallow: /quiz",
        "Disallow: /auth",
        f"Sitemap: {url_for('public.sitemap', _external=True)}",
    ]
    return "\n".join(lines) + "\n", 200, {"Content-Type": "text/plain"}
