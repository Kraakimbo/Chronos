"""Helpers for the "on this day" calendar: today's event, search, dates."""

import unicodedata
from datetime import date

from app.data import EVENTS


def _normalize(text):
    """Lowercase and strip accents, so "cesar" matches "César"."""
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(c for c in decomposed if not unicodedata.combining(c)).lower()

MONTHS_FR = [
    "", "janvier", "février", "mars", "avril", "mai", "juin",
    "juillet", "août", "septembre", "octobre", "novembre", "décembre",
]


def events_list():
    return list(EVENTS.values())


def today_french_label(today=None):
    today = today or date.today()
    return f"{today.day} {MONTHS_FR[today.month].capitalize()}"


def years_ago(event, today=None):
    today = today or date.today()
    if event["year"] < 0:
        # No year zero in the calendar: 44 BC -> 1 AD is 44 years, not 45.
        return today.year + abs(event["year"]) - 1
    return today.year - event["year"]


def find_todays_event(today=None):
    """Return (event, is_exact_match) for today's real date.

    Falls back to a deterministic "featured" pick (stable for the whole
    day, rotates daily) when no event in the calendar matches today's
    month/day exactly — so the home page always has something to show
    without ever claiming a false "this happened today".
    """
    today = today or date.today()
    events = events_list()

    for event in events:
        if event["month"] == today.month and event["day"] == today.day:
            return event, True

    featured = events[today.timetuple().tm_yday % len(events)]
    return featured, False


def search_events(query=None, category=None, era_key=None):
    results = events_list()
    if category and category != "Tous":
        results = [e for e in results if e["category"] == category]
    if era_key:
        results = [e for e in results if e["era_key"] == era_key]
    if query:
        q = _normalize(query.strip())
        results = [
            e
            for e in results
            if q in _normalize(e["title"])
            or q in _normalize(e["era"])
            or q in _normalize(e["category"])
            or q in _normalize(e["location"])
        ]
    return results


def all_categories():
    return sorted({e["category"] for e in events_list()})
