"""Static demo content for the historical events and quiz.

This stands in for a future content database/CMS: enough to wire the
Stitch screens to real routes and real per-user progress without
overbuilding a full content-management system for a demo.
"""

EVENTS = {
    "prise-de-la-bastille": {
        "slug": "prise-de-la-bastille",
        "title": "La prise de la Bastille",
        "date_label": "14 Juillet 1789",
        "era": "Révolution Française",
        "location": "Paris, France",
        "summary": (
            "Un événement majeur de la Révolution française où les insurgés "
            "parisiens s'emparent de la forteresse de la Bastille, symbole "
            "de l'absolutisme royal."
        ),
        "before": (
            "Tensions croissantes à Paris, renvoi de Necker, concentration "
            "des troupes royales autour de la capitale."
        ),
        "during": (
            "Le peuple cherche des armes et de la poudre, se dirigeant vers "
            "la forteresse-prison symbole de l'absolutisme."
        ),
        "after": (
            "Capitulation du gouverneur de Launay, création de la Garde "
            "nationale, début du démantèlement de la forteresse."
        ),
        "narrative": [
            (
                "Le 14 juillet 1789, au matin, une foule nombreuse d'artisans, "
                "de boutiquiers et de bourgeois se rassemble devant la "
                "forteresse de la Bastille, à l'est de Paris."
            ),
            (
                "La Bastille, défendue par une petite garnison sous le "
                "commandement du gouverneur Bernard-René de Launay, représente "
                "le symbole de l'arbitraire royal."
            ),
            (
                "Rejoints par des gardes françaises mutinés apportant des "
                "canons, les assaillants brisent les chaînes du pont-levis. "
                "Le gouverneur de Launay capitule en fin d'après-midi."
            ),
        ],
        "why_it_matters": (
            "Militairement modeste, la prise de la Bastille marque la première "
            "intervention décisive du peuple parisien dans la Révolution et "
            "force Louis XVI à reculer."
        ),
        "quiz_slug": "bastille-importance",
    }
}

TODAY_EVENT_SLUG = "prise-de-la-bastille"

QUIZ_QUESTIONS = {
    "bastille-importance": {
        "slug": "bastille-importance",
        "era": "Révolution Française",
        "prompt": "Pourquoi la Bastille était-elle importante ?",
        "options": [
            "C'était un palais d'été pour la royauté.",
            "Prison symbole du pouvoir royal",
            "Le premier musée national de France.",
            "Une forteresse abandonnée depuis des siècles.",
        ],
        "correct_index": 1,
        "fun_fact": (
            "La prise de la Bastille le 14 juillet 1789 est considérée comme "
            "le point de départ de la Révolution française. Bien qu'elle ne "
            "contenait que sept prisonniers à ce moment-là, elle représentait "
            "l'arbitraire du pouvoir absolu du roi."
        ),
    }
}

DEFAULT_QUIZ_SLUG = "bastille-importance"
