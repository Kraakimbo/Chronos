"""Static demo content for the historical events and quiz.

This stands in for a future content database/CMS: enough to wire the
Stitch screens to real routes and real per-user progress without
overbuilding a full content-management system for a demo.
"""

AVATARS = {
    "1": {"emoji": "🏛️", "bg": "#FFF9E6", "label": "Temple"},
    "2": {"emoji": "📜", "bg": "#FDECD8", "label": "Parchemin"},
    "3": {"emoji": "⚔️", "bg": "#F3E8E1", "label": "Épée"},
    "4": {"emoji": "🗿", "bg": "#EFEEEC", "label": "Statue"},
    "5": {"emoji": "👑", "bg": "#FFF3C4", "label": "Couronne"},
    "6": {"emoji": "🦉", "bg": "#E9E4D8", "label": "Chouette"},
    "7": {"emoji": "⏳", "bg": "#F4E9D6", "label": "Sablier"},
    "8": {"emoji": "🔭", "bg": "#E4E1E7", "label": "Longue-vue"},
}
DEFAULT_AVATAR_ID = "1"

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
    },
    "pyramide-gizeh": {
        "slug": "pyramide-gizeh",
        "era": "Antiquité",
        "prompt": "Pour qui la grande pyramide de Gizeh a-t-elle été construite ?",
        "options": [
            "Le pharaon Khéops",
            "La reine Cléopâtre",
            "L'empereur Alexandre le Grand",
            "Le pharaon Toutânkhamon",
        ],
        "correct_index": 0,
        "fun_fact": (
            "Achevée vers 2560 av. J.-C., la grande pyramide de Gizeh est "
            "restée le plus haut monument construit par l'homme pendant "
            "plus de 3 800 ans."
        ),
    },
    "cesar-assassinat": {
        "slug": "cesar-assassinat",
        "era": "Antiquité",
        "prompt": "En quelle année Jules César a-t-il été assassiné ?",
        "options": ["44 av. J.-C.", "27 av. J.-C.", "476", "753 av. J.-C."],
        "correct_index": 0,
        "fun_fact": (
            "César est poignardé le 15 mars (les Ides de mars) 44 av. J.-C., "
            "par un groupe de sénateurs menés par Brutus et Cassius, "
            "craignant qu'il ne devienne roi de Rome."
        ),
    },
    "gutenberg-imprimerie": {
        "slug": "gutenberg-imprimerie",
        "era": "Moyen Âge",
        "prompt": "Quelle invention de Gutenberg a bouleversé la diffusion du savoir ?",
        "options": [
            "La boussole",
            "L'imprimerie à caractères mobiles",
            "La poudre à canon",
            "Le moulin à eau",
        ],
        "correct_index": 1,
        "fun_fact": (
            "Vers 1450, Gutenberg met au point l'imprimerie à caractères "
            "mobiles à Mayence, rendant les livres bien plus rapides et "
            "moins coûteux à produire — un tournant majeur pour l'accès au savoir."
        ),
    },
    "joconde-peintre": {
        "slug": "joconde-peintre",
        "era": "Renaissance",
        "prompt": "Qui a peint la Joconde (Mona Lisa) ?",
        "options": [
            "Michel-Ange",
            "Raphaël",
            "Léonard de Vinci",
            "Sandro Botticelli",
        ],
        "correct_index": 2,
        "fun_fact": (
            "Peinte au début du XVIe siècle, la Joconde est aujourd'hui "
            "exposée au musée du Louvre à Paris et reste l'une des œuvres "
            "d'art les plus visitées au monde."
        ),
    },
    "prehistoire-feu": {
        "slug": "prehistoire-feu",
        "era": "Préhistoire",
        "prompt": "Quel usage la maîtrise du feu a-t-elle rendu possible pour les hommes préhistoriques ?",
        "options": [
            "Cuire les aliments et se protéger du froid",
            "Fabriquer des outils en métal",
            "Naviguer de nuit",
            "Fondre le verre",
        ],
        "correct_index": 0,
        "fun_fact": (
            "La maîtrise du feu, il y a plusieurs centaines de milliers "
            "d'années, a permis de cuire les aliments, de se chauffer, de "
            "se protéger des prédateurs et de prolonger les activités après "
            "la tombée de la nuit."
        ),
    },
    "apollo-11-lune": {
        "slug": "apollo-11-lune",
        "era": "XXe siècle",
        "prompt": "Qui a été le premier homme à marcher sur la Lune, en 1969 ?",
        "options": ["Buzz Aldrin", "Youri Gagarine", "Neil Armstrong", "John Glenn"],
        "correct_index": 2,
        "fun_fact": (
            "Le 21 juillet 1969, Neil Armstrong pose le pied sur la Lune "
            "lors de la mission Apollo 11, prononçant la célèbre phrase "
            "« C'est un petit pas pour l'homme, un bond de géant pour l'humanité »."
        ),
    },
}

DEFAULT_QUIZ_SLUG = "bastille-importance"
