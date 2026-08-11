"""XP level, badges and era-mastery helpers.

Small, self-contained formulas derived from xp/streak_days — no extra
tables needed. Not meant to model a "real" curriculum, just to give the
progression UI (ring, badges, collections) something to react to.
"""

XP_PER_LEVEL = 500

BADGES = [
    {"key": "decouvreur", "emoji": "🔍", "label": "Découvreur", "unlocked": lambda u: u.xp > 0},
    {"key": "erudit", "emoji": "📚", "label": "Érudit", "unlocked": lambda u: u.xp >= 100},
    {"key": "gardien-du-temps", "emoji": "⏳", "label": "Gardien du temps", "unlocked": lambda u: u.streak_days >= 3},
]

ERAS = [
    {"key": "prehistoire", "name": "Préhistoire", "threshold": 0},
    {"key": "antiquite", "name": "Antiquité", "threshold": 50},
    {"key": "moyen-age", "name": "Moyen Âge", "threshold": 150},
    {"key": "renaissance", "name": "Renaissance", "threshold": 300},
    {"key": "revolution-industrielle", "name": "Révolution Industrielle", "threshold": 500},
    {"key": "guerres-mondiales", "name": "Guerres Mondiales", "threshold": 750},
    {"key": "ere-spatiale", "name": "Ère Spatiale", "threshold": 1000},
]


RANKS = [
    (1, "Novice"),
    (3, "Explorateur"),
    (6, "Historien"),
    (10, "Maître Historien"),
    (20, "Gardien du Temps"),
]


def rank_for(level):
    title = RANKS[0][1]
    for min_level, name in RANKS:
        if level >= min_level:
            title = name
    return title


def level_info(user):
    level = user.xp // XP_PER_LEVEL + 1
    xp_in_level = user.xp % XP_PER_LEVEL
    progress = xp_in_level / XP_PER_LEVEL
    circumference = 283
    return {
        "level": level,
        "xp_in_level": xp_in_level,
        "xp_target": XP_PER_LEVEL,
        "ring_circumference": circumference,
        "ring_dashoffset": round(circumference * (1 - progress), 1),
        "progress_percent": round(progress * 100, 1),
        "rank": rank_for(level),
    }


def badges_for(user):
    return [
        {"key": b["key"], "emoji": b["emoji"], "label": b["label"], "unlocked": b["unlocked"](user)}
        for b in BADGES
    ]


def eras_progress(user):
    result = []
    for i, era in enumerate(ERAS):
        next_threshold = ERAS[i + 1]["threshold"] if i + 1 < len(ERAS) else era["threshold"] + 250
        span = next_threshold - era["threshold"]
        if user.xp <= era["threshold"]:
            status = "Verrouillé"
            percent = 0
        elif user.xp >= next_threshold:
            status = "Maîtrisé"
            percent = 100
        else:
            percent = round((user.xp - era["threshold"]) / span * 100)
            status = f"{percent}% terminé"
        result.append({**era, "status": status, "percent": percent, "next_threshold": next_threshold})
    return result
