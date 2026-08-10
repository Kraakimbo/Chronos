"""Historical content: the "on this day" calendar, avatars and quiz bank.

This stands in for a future content database/CMS: enough to give the
app a real, growing body of historical content without overbuilding a
full content-management system for a demo.
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

# Each event: month/day (for the "on this day" calendar), year, era bucket
# (matches app/main/routes.py ERAS keys), category (for Explorer filters),
# map_pos (x%, y% on the stylized Explorer map — decorative, not a real
# projection), and the same depth of writing as the original Bastille entry:
# before/during/after, a 3-paragraph narrative, why_it_matters and 2-3 key
# figures.
EVENTS = {
    "prise-de-la-bastille": {
        "slug": "prise-de-la-bastille",
        "title": "La prise de la Bastille",
        "month": 7,
        "day": 14,
        "year": 1789,
        "date_label": "14 Juillet 1789",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Politique",
        "location": "Paris, France",
        "location_label": "Place de la Bastille",
        "map_pos": (48, 35),
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
                "forteresse de la Bastille, à l'est de Paris. Ils viennent de "
                "piller l'Hôtel des Invalides, s'emparant de milliers de "
                "fusils, mais il leur manque l'essentiel : la poudre à canon "
                "et les balles, stockées en masse dans l'arsenal de la prison."
            ),
            (
                "La Bastille, défendue par une petite garnison de soldats "
                "invalides et de gardes suisses sous le commandement du "
                "gouverneur Bernard-René de Launay, représente également le "
                "symbole de l'arbitraire royal, bien qu'elle ne contienne ce "
                "jour-là que sept prisonniers. Après des heures de "
                "négociations infructueuses, des coups de feu éclatent."
            ),
            (
                "Rejoints par des gardes françaises mutinées apportant des "
                "canons, les assaillants parviennent à briser les chaînes du "
                "pont-levis. Face à cette puissance de feu, le gouverneur de "
                "Launay capitule en fin d'après-midi. La foule investit les "
                "lieux, libère les prisonniers et s'empare des munitions."
            ),
        ],
        "why_it_matters": (
            "Militairement modeste, la prise de la Bastille marque la première "
            "intervention violente et décisive du peuple parisien dans la "
            "Révolution et force Louis XVI à reculer, rappeler Necker et "
            "reconnaître la nouvelle municipalité de Paris."
        ),
        "characters": [
            {"name": "Louis XVI", "role": "Roi de France", "emoji": "👑", "bg": "#FFF3C4"},
            {"name": "C. Desmoulins", "role": "Journaliste, Orateur", "emoji": "📢", "bg": "#FDECD8"},
            {"name": "De Launay", "role": "Gouverneur", "emoji": "🎖️", "bg": "#E9E4D8"},
        ],
        "quiz_slug": "bastille-importance",
    },
    "prise-des-tuileries": {
        "slug": "prise-des-tuileries",
        "title": "La prise des Tuileries",
        "month": 8,
        "day": 10,
        "year": 1792,
        "date_label": "10 Août 1792",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Politique",
        "location": "Paris, France",
        "location_label": "Palais des Tuileries",
        "map_pos": (48, 35),
        "summary": (
            "L'insurrection parisienne prend d'assaut le palais des "
            "Tuileries, met fin à la monarchie de fait et précipite la chute "
            "de Louis XVI."
        ),
        "before": (
            "La patrie est déclarée en danger face à l'invasion prussienne et "
            "autrichienne. La confiance dans la loyauté du roi s'effondre "
            "après sa fuite manquée à Varennes."
        ),
        "during": (
            "Des sections parisiennes et des fédérés marchent sur les "
            "Tuileries. Louis XVI se réfugie auprès de l'Assemblée "
            "législative, laissant les Gardes suisses défendre seuls le "
            "palais."
        ),
        "after": (
            "L'Assemblée suspend le roi. Six semaines plus tard, la "
            "Convention proclame la première République française."
        ),
        "narrative": [
            (
                "Au matin du 10 août 1792, des bataillons de gardes "
                "nationaux fédérés, venus notamment de Marseille et de "
                "Bretagne, convergent avec les sections révolutionnaires "
                "parisiennes vers le palais des Tuileries, résidence du roi "
                "depuis son retour forcé de Versailles en 1789."
            ),
            (
                "Craignant pour sa vie, Louis XVI quitte le palais avec sa "
                "famille pour se placer sous la protection de l'Assemblée "
                "législative toute proche. Les quelque neuf cents Gardes "
                "suisses restés sur place, sans ordre clair de se retirer, "
                "affrontent seuls l'assaut : les combats font près d'un "
                "millier de morts, pour l'essentiel des gardes suisses."
            ),
            (
                "Le palais est pillé, les insurgés s'emparent des lieux. "
                "Face au fait accompli, l'Assemblée législative vote la "
                "suspension du roi de ses fonctions et convoque une "
                "Convention nationale élue au suffrage universel masculin."
            ),
        ],
        "why_it_matters": (
            "Le 10 août 1792 met fin, dans les faits, à un millénaire de "
            "monarchie en France. Il ouvre la voie à la proclamation de la "
            "République le 21 septembre 1792 et, quelques mois plus tard, au "
            "procès et à l'exécution de Louis XVI."
        ),
        "characters": [
            {"name": "Louis XVI", "role": "Roi de France (suspendu)", "emoji": "👑", "bg": "#FFF3C4"},
            {"name": "Marie-Antoinette", "role": "Reine de France", "emoji": "💎", "bg": "#F3E8E1"},
            {"name": "Gardes Suisses", "role": "Défenseurs du palais", "emoji": "🛡️", "bg": "#E9E4D8"},
        ],
        "quiz_slug": "tuileries-consequence",
    },
    "assassinat-cesar": {
        "slug": "assassinat-cesar",
        "title": "L'assassinat de Jules César",
        "month": 3,
        "day": 15,
        "year": -44,
        "date_label": "15 Mars 44 av. J.-C.",
        "era": "Antiquité",
        "era_key": "antiquite",
        "category": "Politique",
        "location": "Rome, Italie",
        "location_label": "Théâtre de Pompée",
        "map_pos": (52, 42),
        "summary": (
            "Un groupe de sénateurs romains, craignant l'instauration d'une "
            "monarchie, assassine Jules César en plein Sénat aux Ides de mars."
        ),
        "before": (
            "César, nommé dictateur à vie, concentre des pouvoirs jugés "
            "excessifs par une partie du Sénat, qui redoute la fin de la "
            "République."
        ),
        "during": (
            "Un groupe de sénateurs, les « Libérateurs », l'entoure et le "
            "poignarde à plusieurs reprises lors d'une séance du Sénat."
        ),
        "after": (
            "Le vide politique laissé par César déclenche une nouvelle "
            "guerre civile, dont sortira vainqueur son fils adoptif Octave, "
            "futur empereur Auguste."
        ),
        "narrative": [
            (
                "Le 15 mars de l'an 44 av. J.-C. — les Ides de mars dans le "
                "calendrier romain —, Jules César se rend à une séance du "
                "Sénat qui se tient exceptionnellement dans la curie du "
                "théâtre de Pompée, le bâtiment habituel étant en rénovation."
            ),
            (
                "Un groupe d'une soixantaine de sénateurs, mené par Marcus "
                "Junius Brutus et Cassius Longinus, l'entoure sous prétexte "
                "de lui présenter une pétition. Ils le poignardent à de "
                "nombreuses reprises. César, selon la tradition, ne "
                "cherche pas à se défendre face à l'ampleur du complot."
            ),
            (
                "Les conjurés espéraient restaurer les pleins pouvoirs du "
                "Sénat en supprimant celui qu'ils considéraient comme un "
                "tyran en devenir. Au lieu de cela, son assassinat plonge "
                "Rome dans une nouvelle guerre civile entre les partisans "
                "de César et ses assassins."
            ),
        ],
        "why_it_matters": (
            "Loin de sauver la République, l'assassinat de César précipite "
            "sa chute définitive : la guerre civile qui suit se conclut par "
            "l'avènement d'Octave-Auguste et la naissance de l'Empire romain "
            "en 27 av. J.-C."
        ),
        "characters": [
            {"name": "Jules César", "role": "Dictateur de Rome", "emoji": "🏛️", "bg": "#FFF3C4"},
            {"name": "Brutus", "role": "Sénateur, conjuré", "emoji": "🗡️", "bg": "#F3E8E1"},
            {"name": "Marc Antoine", "role": "Général, allié de César", "emoji": "🛡️", "bg": "#E9E4D8"},
        ],
        "quiz_slug": "cesar-assassinat",
    },
    "alunissage-apollo-11": {
        "slug": "alunissage-apollo-11",
        "title": "L'alunissage d'Apollo 11",
        "month": 7,
        "day": 21,
        "year": 1969,
        "date_label": "21 Juillet 1969",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Science",
        "location": "Mer de la Tranquillité, Lune",
        "location_label": "Mer de la Tranquillité",
        "map_pos": None,
        "summary": (
            "Neil Armstrong devient le premier être humain à marcher sur la "
            "Lune, retransmis en direct devant des centaines de millions de "
            "téléspectateurs."
        ),
        "before": (
            "En pleine course à l'espace avec l'URSS, les États-Unis lancent "
            "le programme Apollo pour poser un équipage sur la Lune avant "
            "1970."
        ),
        "during": (
            "Le module lunaire Eagle se pose sur la Mer de la Tranquillité ; "
            "Armstrong puis Aldrin sortent marcher à la surface pendant que "
            "Collins reste en orbite lunaire."
        ),
        "after": (
            "L'équipage rapporte des échantillons lunaires et rentre sain et "
            "sauf sur Terre, marquant l'apogée du programme spatial américain."
        ),
        "narrative": [
            (
                "Le 16 juillet 1969, la fusée Saturn V emporte Neil "
                "Armstrong, Buzz Aldrin et Michael Collins depuis le Centre "
                "spatial Kennedy. Quatre jours plus tard, le module lunaire "
                "Eagle se sépare du module de commande et entame sa descente "
                "vers la surface lunaire."
            ),
            (
                "Le 20 juillet, Armstrong pose l'Eagle manuellement sur la "
                "Mer de la Tranquillité, évitant de justesse un champ de "
                "rochers, avec à peine quelques dizaines de secondes de "
                "carburant restant. Le lendemain, à 2h56 (heure de Paris) le "
                "21 juillet, il pose le pied sur le sol lunaire."
            ),
            (
                "« C'est un petit pas pour l'homme, un bond de géant pour "
                "l'humanité », déclare-t-il. Buzz Aldrin le rejoint peu "
                "après. Les deux astronautes plantent un drapeau américain, "
                "collectent des roches lunaires et repartent après environ "
                "21 heures passées sur place."
            ),
        ],
        "why_it_matters": (
            "L'alunissage d'Apollo 11 marque l'aboutissement de la course à "
            "l'espace entre les États-Unis et l'URSS et reste l'un des "
            "exploits techniques et humains les plus marquants du XXe siècle."
        ),
        "characters": [
            {"name": "Neil Armstrong", "role": "Commandant de mission", "emoji": "👨‍🚀", "bg": "#E4E1E7"},
            {"name": "Buzz Aldrin", "role": "Pilote du module lunaire", "emoji": "🚀", "bg": "#FDECD8"},
            {"name": "Michael Collins", "role": "Pilote du module de commande", "emoji": "🛰️", "bg": "#F3E8E1"},
        ],
        "quiz_slug": "apollo-11-lune",
    },
    "chute-mur-berlin": {
        "slug": "chute-mur-berlin",
        "title": "La chute du mur de Berlin",
        "month": 11,
        "day": 9,
        "year": 1989,
        "date_label": "9 Novembre 1989",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Politique",
        "location": "Berlin, Allemagne",
        "location_label": "Point de passage Bornholmer Straße",
        "map_pos": (53, 30),
        "summary": (
            "L'annonce inattendue de l'ouverture des frontières est-allemandes "
            "provoque l'effondrement du mur de Berlin, symbole de la guerre "
            "froide depuis 1961."
        ),
        "before": (
            "Des mois de manifestations pacifiques en Allemagne de l'Est et "
            "l'assouplissement du bloc soviétique fragilisent le régime "
            "est-allemand."
        ),
        "during": (
            "Une annonce gouvernementale mal formulée laisse croire à une "
            "ouverture immédiate des frontières ; des milliers de Berlinois "
            "affluent vers les points de passage, submergeant les gardes."
        ),
        "after": (
            "Le mur est ouvert puis peu à peu démantelé par la foule, "
            "ouvrant la voie à la réunification allemande le 3 octobre 1990."
        ),
        "narrative": [
            (
                "Le 9 novembre 1989 au soir, le porte-parole du gouvernement "
                "est-allemand Günter Schabowski annonce en conférence de "
                "presse, de façon confuse, que les citoyens de RDA peuvent "
                "désormais voyager librement « immédiatement, sans délai »."
            ),
            (
                "En quelques heures, des milliers de Berlinois de l'Est se "
                "pressent aux points de passage du mur, notamment à "
                "Bornholmer Straße. Débordés et sans instructions claires, "
                "les gardes-frontières finissent par ouvrir les barrières "
                "vers 23h30."
            ),
            (
                "Des foules de Berlinois de l'Est et de l'Ouest se "
                "retrouvent, certains montent sur le mur, d'autres "
                "commencent à le fissurer à coups de marteau et de burin. "
                "Les scènes de liesse sont retransmises dans le monde "
                "entier en direct."
            ),
        ],
        "why_it_matters": (
            "La chute du mur de Berlin marque symboliquement la fin de la "
            "guerre froide et du rideau de fer en Europe, et ouvre la voie à "
            "la réunification allemande moins d'un an plus tard."
        ),
        "characters": [
            {"name": "Günter Schabowski", "role": "Porte-parole du gouvernement", "emoji": "🎙️", "bg": "#E9E4D8"},
            {"name": "Helmut Kohl", "role": "Chancelier ouest-allemand", "emoji": "🏛️", "bg": "#FFF3C4"},
            {"name": "Mikhaïl Gorbatchev", "role": "Dirigeant soviétique", "emoji": "🕊️", "bg": "#F3E8E1"},
        ],
        "quiz_slug": "mur-berlin-annee",
    },
    "debarquement-normandie": {
        "slug": "debarquement-normandie",
        "title": "Le débarquement de Normandie",
        "month": 6,
        "day": 6,
        "year": 1944,
        "date_label": "6 Juin 1944",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Militaire",
        "location": "Normandie, France",
        "location_label": "Plages du Débarquement",
        "map_pos": (46, 33),
        "summary": (
            "Les forces alliées débarquent sur les côtes normandes lors de "
            "l'opération Overlord, la plus grande invasion maritime de "
            "l'histoire, ouvrant un second front décisif contre l'Allemagne "
            "nazie."
        ),
        "before": (
            "Après des années de préparation et de désinformation pour "
            "tromper l'état-major allemand sur le lieu du débarquement, les "
            "Alliés rassemblent une force amphibie sans précédent."
        ),
        "during": (
            "Près de 156 000 soldats alliés débarquent sur cinq plages "
            "codées Utah, Omaha, Gold, Juno et Sword, appuyés par des "
            "parachutistes largués dans la nuit."
        ),
        "after": (
            "Malgré de lourdes pertes, notamment à Omaha Beach, les Alliés "
            "établissent une tête de pont qui permettra la libération de la "
            "France dans les mois suivants."
        ),
        "narrative": [
            (
                "Dans la nuit du 5 au 6 juin 1944, des milliers de "
                "parachutistes américains et britanniques sont largués "
                "derrière les lignes allemandes en Normandie, chargés de "
                "sécuriser des points stratégiques avant l'assaut principal."
            ),
            (
                "À l'aube, une armada de plus de 5 000 navires appuie le "
                "débarquement de troupes américaines, britanniques, "
                "canadiennes et de la France libre sur cinq plages. Les "
                "combats sont particulièrement meurtriers à Omaha Beach, où "
                "les défenses allemandes infligent de lourdes pertes."
            ),
            (
                "Malgré la résistance allemande, les têtes de pont sont "
                "solidement établies en fin de journée. Cette opération "
                "Overlord ouvre un second front décisif à l'ouest, tandis "
                "que l'Armée rouge repousse déjà les forces allemandes à "
                "l'est."
            ),
        ],
        "why_it_matters": (
            "Le débarquement de Normandie constitue un tournant majeur de la "
            "Seconde Guerre mondiale en Europe de l'Ouest, menant à la "
            "libération de Paris en août 1944 et à la capitulation "
            "allemande moins d'un an plus tard."
        ),
        "characters": [
            {"name": "Dwight D. Eisenhower", "role": "Commandant suprême allié", "emoji": "🎖️", "bg": "#E9E4D8"},
            {"name": "Charles de Gaulle", "role": "Chef de la France libre", "emoji": "🇫🇷", "bg": "#FFF3C4"},
            {"name": "Erwin Rommel", "role": "Maréchal allemand", "emoji": "🛡️", "bg": "#F3E8E1"},
        ],
        "quiz_slug": "debarquement-date",
    },
    "armistice-1918": {
        "slug": "armistice-1918",
        "title": "L'armistice de 1918",
        "month": 11,
        "day": 11,
        "year": 1918,
        "date_label": "11 Novembre 1918",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Militaire",
        "location": "Compiègne, France",
        "location_label": "Clairière de Rethondes",
        "map_pos": (48, 34),
        "summary": (
            "La signature de l'armistice dans un wagon-restaurant en forêt "
            "de Compiègne met fin aux combats de la Première Guerre mondiale."
        ),
        "before": (
            "Épuisée, l'Allemagne voit ses alliés capituler les uns après "
            "les autres et fait face à des troubles révolutionnaires "
            "internes."
        ),
        "during": (
            "Une délégation allemande signe l'armistice avec les Alliés dans "
            "le wagon du maréchal Foch, à Rethondes, tôt le matin du 11 "
            "novembre."
        ),
        "after": (
            "Les combats cessent à 11h, heure symbolique du « onzième jour "
            "du onzième mois à la onzième heure ». Le traité de paix "
            "définitif sera signé à Versailles en 1919."
        ),
        "narrative": [
            (
                "À l'automne 1918, l'Allemagne, épuisée et privée du soutien "
                "de ses alliés austro-hongrois et ottomans, doit se résoudre "
                "à demander un armistice face à l'avancée alliée sur le "
                "front occidental."
            ),
            (
                "Dans la nuit du 10 au 11 novembre, une délégation allemande "
                "négocie les conditions de cessation des hostilités avec le "
                "maréchal Ferdinand Foch, dans un wagon-restaurant aménagé "
                "en salle de réunion, en forêt de Compiègne."
            ),
            (
                "L'armistice est signé à 5h15 du matin et entre en vigueur à "
                "11 heures précises. Sur tout le front, les combats cessent "
                "progressivement, mettant fin à plus de quatre années d'une "
                "guerre qui a fait environ 10 millions de morts militaires."
            ),
        ],
        "why_it_matters": (
            "L'armistice du 11 novembre 1918 met fin à la Première Guerre "
            "mondiale et devient une date de commémoration nationale dans de "
            "nombreux pays. Le traité de Versailles qui suivra en 1919 "
            "redessinera la carte de l'Europe."
        ),
        "characters": [
            {"name": "Ferdinand Foch", "role": "Maréchal de France", "emoji": "🎖️", "bg": "#E9E4D8"},
            {"name": "Georges Clemenceau", "role": "Président du Conseil", "emoji": "🏛️", "bg": "#FFF3C4"},
        ],
        "quiz_slug": "armistice-heure",
    },
    "declaration-independance-americaine": {
        "slug": "declaration-independance-americaine",
        "title": "La déclaration d'indépendance américaine",
        "month": 7,
        "day": 4,
        "year": 1776,
        "date_label": "4 Juillet 1776",
        "era": "Renaissance",
        "era_key": "renaissance",
        "category": "Politique",
        "location": "Philadelphie, États-Unis",
        "location_label": "Independence Hall",
        "map_pos": (25, 38),
        "summary": (
            "Le Congrès continental adopte la déclaration proclamant "
            "l'indépendance des treize colonies américaines vis-à-vis de la "
            "Grande-Bretagne."
        ),
        "before": (
            "Les colonies américaines, en guerre depuis 1775 contre la "
            "couronne britannique, réclament la fin des taxes imposées sans "
            "représentation politique."
        ),
        "during": (
            "Le Congrès continental adopte le texte rédigé principalement "
            "par Thomas Jefferson, proclamant les treize colonies libres et "
            "indépendantes."
        ),
        "after": (
            "La guerre d'indépendance se poursuit jusqu'en 1783, date à "
            "laquelle la Grande-Bretagne reconnaît officiellement les "
            "États-Unis d'Amérique."
        ),
        "narrative": [
            (
                "Depuis 1775, les treize colonies britanniques d'Amérique du "
                "Nord sont en guerre ouverte contre la couronne, exaspérées "
                "par des taxes imposées sans qu'elles aient de représentants "
                "au Parlement de Londres."
            ),
            (
                "Réuni à Philadelphie, le Congrès continental charge un "
                "comité de cinq membres, dont Thomas Jefferson, John Adams "
                "et Benjamin Franklin, de rédiger une déclaration justifiant "
                "la rupture avec la Grande-Bretagne. Le texte est adopté le "
                "4 juillet 1776."
            ),
            (
                "La déclaration proclame que « tous les hommes sont créés "
                "égaux » et dotés de droits inaliénables, dont la vie, la "
                "liberté et la recherche du bonheur. Elle énumère aussi les "
                "griefs contre le roi George III pour justifier la "
                "séparation."
            ),
        ],
        "why_it_matters": (
            "Ce texte fondateur donne naissance aux États-Unis d'Amérique et "
            "inspirera par la suite d'autres déclarations de droits, dont la "
            "Déclaration des droits de l'homme et du citoyen française de "
            "1789."
        ),
        "characters": [
            {"name": "Thomas Jefferson", "role": "Principal rédacteur", "emoji": "🪶", "bg": "#FDECD8"},
            {"name": "Benjamin Franklin", "role": "Membre du comité", "emoji": "🔭", "bg": "#E4E1E7"},
            {"name": "George Washington", "role": "Commandant des armées", "emoji": "🎖️", "bg": "#E9E4D8"},
        ],
        "quiz_slug": "independance-americaine-annee",
    },
    "arrivee-christophe-colomb": {
        "slug": "arrivee-christophe-colomb",
        "title": "L'arrivée de Christophe Colomb aux Amériques",
        "month": 10,
        "day": 12,
        "year": 1492,
        "date_label": "12 Octobre 1492",
        "era": "Renaissance",
        "era_key": "renaissance",
        "category": "Exploration",
        "location": "Bahamas",
        "location_label": "Île de Guanahani",
        "map_pos": (22, 55),
        "summary": (
            "Après plus de deux mois de traversée, l'expédition de "
            "Christophe Colomb atteint une île des Bahamas, marquant le "
            "début des grandes découvertes européennes en Amérique."
        ),
        "before": (
            "Financé par les rois catholiques d'Espagne, Colomb cherche une "
            "route occidentale vers les Indes en traversant l'Atlantique."
        ),
        "during": (
            "Après 36 jours de traversée sans terre en vue, un marin de la "
            "Pinta aperçoit la côte d'une île qu'ils nomment San Salvador."
        ),
        "after": (
            "Colomb explore ensuite Cuba et Hispaniola, convaincu d'avoir "
            "atteint les abords de l'Asie, avant de rentrer en Espagne "
            "porter la nouvelle."
        ),
        "narrative": [
            (
                "Le 3 août 1492, Christophe Colomb quitte le port de Palos, "
                "en Espagne, avec trois navires — la Santa María, la Pinta "
                "et la Niña — et un équipage d'environ 90 hommes, dans "
                "l'espoir de rejoindre l'Asie en naviguant vers l'ouest."
            ),
            (
                "Après plus de deux mois de traversée éprouvante, marquée "
                "par les doutes de l'équipage, un vigie de la Pinta aperçoit "
                "la terre dans la nuit du 11 au 12 octobre 1492. L'expédition "
                "débarque sur une île des Bahamas que Colomb baptise San "
                "Salvador."
            ),
            (
                "Persuadé d'avoir atteint les Indes orientales, Colomb "
                "nomme les habitants qu'il rencontre « Indiens ». Il "
                "poursuit son exploration vers Cuba et Hispaniola avant de "
                "regagner l'Espagne, où la nouvelle de sa découverte se "
                "répand rapidement en Europe."
            ),
        ],
        "why_it_matters": (
            "Ce premier contact durable entre l'Europe et le continent "
            "américain ouvre l'ère de la colonisation européenne des "
            "Amériques, aux conséquences immenses — et dévastatrices pour "
            "les populations autochtones — pour les siècles suivants."
        ),
        "characters": [
            {"name": "Christophe Colomb", "role": "Navigateur", "emoji": "⛵", "bg": "#E4E1E7"},
            {"name": "Isabelle Ire de Castille", "role": "Reine d'Espagne", "emoji": "👑", "bg": "#FFF3C4"},
        ],
        "quiz_slug": "colomb-annee",
    },
    "nuit-du-4-aout": {
        "slug": "nuit-du-4-aout",
        "title": "La nuit du 4 août 1789",
        "month": 8,
        "day": 4,
        "year": 1789,
        "date_label": "4 Août 1789",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Politique",
        "location": "Versailles, France",
        "location_label": "Assemblée constituante",
        "map_pos": (47, 35),
        "summary": (
            "Dans un climat d'émotion collective, l'Assemblée constituante "
            "vote l'abolition des privilèges féodaux, mettant fin de facto "
            "au système seigneurial en France."
        ),
        "before": (
            "Depuis la prise de la Bastille, des révoltes paysannes contre "
            "les droits seigneuraux se multiplient dans les campagnes, "
            "épisode connu sous le nom de « Grande Peur »."
        ),
        "during": (
            "Lors d'une séance de nuit, des députés nobles et ecclésiastiques "
            "renoncent tour à tour à leurs privilèges, dans un mouvement "
            "d'entraînement collectif."
        ),
        "after": (
            "Les décrets qui suivent suppriment la dîme, les droits "
            "féodaux et les privilèges fiscaux, posant les bases juridiques "
            "d'une société d'égalité devant la loi."
        ),
        "narrative": [
            (
                "À l'été 1789, la « Grande Peur » s'empare des campagnes "
                "françaises : des rumeurs d'un complot aristocratique "
                "poussent les paysans à attaquer châteaux et registres "
                "seigneuriaux pour détruire les preuves de leurs obligations "
                "féodales."
            ),
            (
                "Dans la soirée du 4 août 1789, à l'Assemblée constituante, "
                "le vicomte de Noailles et le duc d'Aiguillon proposent "
                "l'abolition des droits féodaux pour apaiser les campagnes. "
                "Dans un mouvement d'émulation, nobles et clergé renoncent "
                "les uns après les autres à leurs privilèges."
            ),
            (
                "En quelques heures nocturnes, l'Assemblée vote l'abolition "
                "de la dîme, des droits seigneuriaux, des privilèges "
                "fiscaux des ordres et de la vénalité des offices. Les "
                "décrets définitifs seront rédigés et votés dans les jours "
                "suivants."
            ),
        ],
        "why_it_matters": (
            "La nuit du 4 août 1789 met fin, en droit, à des siècles de "
            "société d'ordres et de privilèges féodaux, posant l'un des "
            "fondements de l'égalité civile proclamée quelques jours plus "
            "tard dans la Déclaration des droits de l'homme et du citoyen."
        ),
        "characters": [
            {"name": "Vicomte de Noailles", "role": "Député, initiateur", "emoji": "📜", "bg": "#FDECD8"},
            {"name": "Duc d'Aiguillon", "role": "Député noble", "emoji": "🎖️", "bg": "#E9E4D8"},
        ],
        "quiz_slug": "nuit-4-aout-consequence",
    },
    "bataille-de-waterloo": {
        "slug": "bataille-de-waterloo",
        "title": "La bataille de Waterloo",
        "month": 6,
        "day": 18,
        "year": 1815,
        "date_label": "18 Juin 1815",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Militaire",
        "location": "Waterloo, Belgique",
        "location_label": "Mont-Saint-Jean",
        "map_pos": (49, 32),
        "summary": (
            "L'armée de Napoléon est défaite par les forces coalisées "
            "britanniques et prussiennes, mettant fin définitivement à "
            "l'épopée impériale française."
        ),
        "before": (
            "Revenu du bannissement de l'île d'Elbe, Napoléon reprend le "
            "pouvoir en France pendant les Cent-Jours, provoquant la "
            "formation d'une septième coalition contre lui."
        ),
        "during": (
            "L'armée française affronte les troupes britanniques du duc de "
            "Wellington, puis l'arrivée décisive de l'armée prussienne de "
            "Blücher en fin de journée fait basculer la bataille."
        ),
        "after": (
            "Napoléon abdique une seconde fois quatre jours plus tard et est "
            "exilé sur l'île de Sainte-Hélène, où il mourra en 1821."
        ),
        "narrative": [
            (
                "Après son évasion de l'île d'Elbe en février 1815, Napoléon "
                "reprend le pouvoir en France sans coup férir. Les grandes "
                "puissances européennes, réunies au congrès de Vienne, "
                "forment aussitôt une nouvelle coalition pour l'arrêter."
            ),
            (
                "Le 18 juin 1815, près du village belge de Waterloo, "
                "l'armée française affronte les troupes anglo-alliées du "
                "duc de Wellington, retranchées sur le plateau du "
                "Mont-Saint-Jean. Les assauts français, dont la célèbre "
                "charge de cavalerie du maréchal Ney, ne parviennent pas à "
                "percer les lignes ennemies."
            ),
            (
                "En fin d'après-midi, l'armée prussienne du maréchal "
                "Blücher, que Napoléon croyait tenue à distance, arrive sur "
                "le flanc droit français. Prise en tenaille, la Grande "
                "Armée se débande. La Garde impériale, engagée en dernier "
                "recours, est repoussée."
            ),
        ],
        "why_it_matters": (
            "Waterloo met un terme définitif à l'épopée napoléonienne et "
            "ouvre en Europe une longue période de restauration monarchique "
            "et d'équilibre entre grandes puissances qui durera jusqu'à la "
            "Première Guerre mondiale."
        ),
        "characters": [
            {"name": "Napoléon Ier", "role": "Empereur des Français", "emoji": "👑", "bg": "#FFF3C4"},
            {"name": "Duc de Wellington", "role": "Commandant anglo-allié", "emoji": "🎖️", "bg": "#E9E4D8"},
            {"name": "Maréchal Blücher", "role": "Commandant prussien", "emoji": "🛡️", "bg": "#F3E8E1"},
        ],
        "quiz_slug": "waterloo-consequence",
    },
    "sacre-napoleon": {
        "slug": "sacre-napoleon",
        "title": "Le sacre de Napoléon Ier",
        "month": 12,
        "day": 2,
        "year": 1804,
        "date_label": "2 Décembre 1804",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Politique",
        "location": "Paris, France",
        "location_label": "Cathédrale Notre-Dame",
        "map_pos": (48, 35),
        "summary": (
            "Napoléon Bonaparte se couronne empereur des Français à "
            "Notre-Dame de Paris, en présence du pape Pie VII, marquant la "
            "naissance du Premier Empire."
        ),
        "before": (
            "Premier consul depuis 1799 puis consul à vie, Bonaparte fait "
            "approuver par référendum populaire l'instauration d'un Empire "
            "héréditaire."
        ),
        "during": (
            "Lors d'une cérémonie fastueuse à Notre-Dame, Napoléon se "
            "couronne lui-même, puis couronne son épouse Joséphine, sous le "
            "regard du pape venu spécialement de Rome."
        ),
        "after": (
            "Le Premier Empire est instauré ; Napoléon règne sur la France "
            "jusqu'à sa première abdication en 1814."
        ),
        "narrative": [
            (
                "Après le coup d'État du 18 brumaire en 1799 et plusieurs "
                "années passées comme Premier consul, Napoléon Bonaparte "
                "fait plébisciter par le peuple français l'instauration "
                "d'un Empire héréditaire à son profit."
            ),
            (
                "Le 2 décembre 1804, la cathédrale Notre-Dame de Paris "
                "accueille une cérémonie de sacre fastueuse, orchestrée par "
                "le peintre Jacques-Louis David. Le pape Pie VII, venu tout "
                "exprès de Rome, bénit les insignes impériaux, mais c'est "
                "Napoléon lui-même qui pose la couronne sur sa tête, puis "
                "couronne son épouse Joséphine."
            ),
            (
                "Ce geste, resté célèbre, symbolise la volonté de Napoléon "
                "de tenir son pouvoir du peuple et de lui-même plutôt que de "
                "l'Église, tout en s'inscrivant dans la continuité "
                "cérémonielle des sacres royaux français."
            ),
        ],
        "why_it_matters": (
            "Le sacre marque la transformation de la République française "
            "en Empire héréditaire et l'apogée politique de Napoléon, qui "
            "dominera l'Europe militairement jusqu'à sa défaite de 1814-1815."
        ),
        "characters": [
            {"name": "Napoléon Ier", "role": "Empereur des Français", "emoji": "👑", "bg": "#FFF3C4"},
            {"name": "Joséphine de Beauharnais", "role": "Impératrice", "emoji": "💎", "bg": "#F3E8E1"},
            {"name": "Pape Pie VII", "role": "Chef de l'Église catholique", "emoji": "⛪", "bg": "#E9E4D8"},
        ],
        "quiz_slug": "sacre-napoleon-lieu",
    },
    "chute-de-constantinople": {
        "slug": "chute-de-constantinople",
        "title": "La chute de Constantinople",
        "month": 5,
        "day": 29,
        "year": 1453,
        "date_label": "29 Mai 1453",
        "era": "Moyen Âge",
        "era_key": "moyen-age",
        "category": "Militaire",
        "location": "Constantinople",
        "location_label": "Constantinople (Istanbul)",
        "map_pos": (58, 40),
        "summary": (
            "Après un siège de près de deux mois, les troupes ottomanes de "
            "Mehmed II s'emparent de Constantinople, mettant fin à onze "
            "siècles d'Empire byzantin."
        ),
        "before": (
            "Affaibli et isolé, l'Empire byzantin ne contrôle plus que sa "
            "capitale, encerclée par l'armée ottomane du jeune sultan "
            "Mehmed II."
        ),
        "during": (
            "Après des semaines de siège et de bombardements par une "
            "artillerie inédite, les troupes ottomanes percent les "
            "murailles théodosiennes et envahissent la ville."
        ),
        "after": (
            "Constantinople devient la capitale de l'Empire ottoman sous le "
            "nom d'Istanbul ; la chute de la ville est traditionnellement "
            "considérée comme la fin du Moyen Âge en Europe."
        ),
        "narrative": [
            (
                "Depuis des siècles, Constantinople résiste aux sièges "
                "grâce à ses puissantes murailles théodosiennes. Mais en "
                "1453, le jeune sultan ottoman Mehmed II rassemble une "
                "armée immense et une artillerie de canons géants conçus "
                "spécialement pour percer ces remparts."
            ),
            (
                "Le siège débute début avril. Pendant près de deux mois, la "
                "ville, défendue par une garnison réduite sous l'empereur "
                "Constantin XI, résiste malgré des bombardements "
                "incessants. Mehmed II fait même transporter une partie de "
                "sa flotte par voie terrestre pour contourner une chaîne "
                "bloquant l'accès à la Corne d'Or."
            ),
            (
                "Le 29 mai 1453 à l'aube, un assaut général finit par percer "
                "les défenses. Constantin XI meurt dans les combats. La "
                "ville est prise, marquant la fin de l'Empire byzantin, "
                "héritier direct de l'Empire romain d'Orient depuis plus de "
                "onze siècles."
            ),
        ],
        "why_it_matters": (
            "La chute de Constantinople met fin à l'Empire byzantin et "
            "marque, pour de nombreux historiens, la transition symbolique "
            "entre le Moyen Âge et la Renaissance en Europe, notamment par "
            "l'exil de savants byzantins qui contribuera à la diffusion des "
            "textes antiques en Occident."
        ),
        "characters": [
            {"name": "Mehmed II", "role": "Sultan ottoman", "emoji": "🏹", "bg": "#FDECD8"},
            {"name": "Constantin XI", "role": "Dernier empereur byzantin", "emoji": "👑", "bg": "#FFF3C4"},
        ],
        "quiz_slug": "constantinople-consequence",
    },
    "signature-magna-carta": {
        "slug": "signature-magna-carta",
        "title": "La signature de la Magna Carta",
        "month": 6,
        "day": 15,
        "year": 1215,
        "date_label": "15 Juin 1215",
        "era": "Moyen Âge",
        "era_key": "moyen-age",
        "category": "Politique",
        "location": "Runnymede, Angleterre",
        "location_label": "Prairie de Runnymede",
        "map_pos": (44, 25),
        "summary": (
            "Le roi Jean sans Terre appose son sceau sur la Grande Charte, "
            "un texte limitant pour la première fois le pouvoir royal "
            "anglais face à ses barons."
        ),
        "before": (
            "Impopulaire après des défaites militaires en France et une "
            "fiscalité jugée abusive, le roi Jean sans Terre fait face à "
            "une révolte de ses barons."
        ),
        "during": (
            "Réunis à Runnymede, les barons contraignent le roi à sceller "
            "un document limitant son pouvoir et garantissant certains "
            "droits, notamment celui d'être jugé par ses pairs."
        ),
        "after": (
            "Bien que rapidement contestée par le roi lui-même, la Grande "
            "Charte sera plusieurs fois réaffirmée et deviendra un texte "
            "fondateur du droit constitutionnel anglais."
        ),
        "narrative": [
            (
                "Au début du XIIIe siècle, le roi Jean sans Terre "
                "d'Angleterre s'aliène ses barons par de lourdes taxes "
                "destinées à financer des guerres coûteuses et infructueuses "
                "contre le roi de France, ainsi que par des conflits avec "
                "la papauté."
            ),
            (
                "En 1215, une coalition de barons en révolte s'empare de "
                "Londres et contraint le roi à négocier. Le 15 juin, dans "
                "la prairie de Runnymede au bord de la Tamise, Jean sans "
                "Terre appose son sceau sur la Magna Carta, un document en "
                "soixante-trois articles."
            ),
            (
                "Le texte garantit notamment qu'aucun homme libre ne peut "
                "être emprisonné ou dépossédé sans jugement légal de ses "
                "pairs, et qu'aucune taxe exceptionnelle ne peut être levée "
                "sans l'accord d'un conseil de barons — une première limite "
                "posée au pouvoir royal absolu."
            ),
        ],
        "why_it_matters": (
            "Bien que largement pensée pour protéger les intérêts des "
            "barons plutôt que du peuple, la Magna Carta est devenue un "
            "symbole fondateur de l'État de droit et a inspiré des "
            "principes constitutionnels repris bien plus tard, jusque dans "
            "la Déclaration d'indépendance américaine."
        ),
        "characters": [
            {"name": "Jean sans Terre", "role": "Roi d'Angleterre", "emoji": "👑", "bg": "#FFF3C4"},
            {"name": "Barons rebelles", "role": "Noblesse anglaise", "emoji": "🛡️", "bg": "#E9E4D8"},
        ],
        "quiz_slug": "magna-carta-principe",
    },
    "eruption-vesuve": {
        "slug": "eruption-vesuve",
        "title": "L'éruption du Vésuve et la destruction de Pompéi",
        "month": 8,
        "day": 24,
        "year": 79,
        "date_label": "24 Août 79",
        "era": "Antiquité",
        "era_key": "antiquite",
        "category": "Catastrophe naturelle",
        "location": "Pompéi, Italie",
        "location_label": "Golfe de Naples",
        "map_pos": (53, 44),
        "summary": (
            "L'éruption soudaine du Vésuve ensevelit les villes romaines de "
            "Pompéi et Herculanum sous plusieurs mètres de cendres, figeant "
            "leur vie quotidienne pour deux millénaires."
        ),
        "before": (
            "Pompéi et Herculanum sont des villes romaines prospères au "
            "pied du Vésuve, un volcan considéré comme endormi depuis des "
            "générations."
        ),
        "during": (
            "En quelques heures, le volcan projette une colonne de cendres "
            "et de pierre ponce sur des kilomètres, avant que des coulées "
            "pyroclastiques brûlantes ne recouvrent les villes."
        ),
        "after": (
            "Les cités sont abandonnées et oubliées pendant plus de "
            "seize siècles, avant d'être redécouvertes par des fouilles "
            "archéologiques à partir du XVIIIe siècle."
        ),
        "narrative": [
            (
                "Le Vésuve, volcan surplombant la baie de Naples, était "
                "considéré comme éteint par les habitants de la région. Le "
                "24 août de l'an 79, il entre brutalement en éruption, "
                "projetant une immense colonne de cendres et de pierre "
                "ponce à près de 30 kilomètres d'altitude."
            ),
            (
                "Pendant plusieurs heures, cendres et pierres s'abattent sur "
                "Pompéi, poussant une partie de la population à fuir. Dans "
                "la nuit, des coulées pyroclastiques — des nuées de gaz "
                "brûlants et de débris dévalant les pentes du volcan à "
                "grande vitesse — surprennent et tuent ceux restés sur "
                "place, notamment à Herculanum, ensevelie plus rapidement "
                "encore."
            ),
            (
                "L'écrivain romain Pline le Jeune, témoin depuis l'autre "
                "rive du golfe de Naples, laisse un récit détaillé de la "
                "catastrophe, au cours de laquelle son oncle Pline "
                "l'Ancien, parti porter secours, trouve la mort."
            ),
        ],
        "why_it_matters": (
            "L'éruption a paradoxalement permis la conservation "
            "exceptionnelle de Pompéi et Herculanum sous les cendres, "
            "offrant aux archéologues depuis le XVIIIe siècle un instantané "
            "unique et détaillé de la vie quotidienne romaine."
        ),
        "characters": [
            {"name": "Pline l'Ancien", "role": "Naturaliste, amiral romain", "emoji": "📜", "bg": "#FDECD8"},
            {"name": "Pline le Jeune", "role": "Écrivain, témoin", "emoji": "🪶", "bg": "#F3E8E1"},
        ],
        "quiz_slug": "vesuve-consequence",
    },
    "krach-de-1929": {
        "slug": "krach-de-1929",
        "title": "Le krach de 1929",
        "month": 10,
        "day": 24,
        "year": 1929,
        "date_label": "24 Octobre 1929",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Économie",
        "location": "New York, États-Unis",
        "location_label": "Wall Street",
        "map_pos": (24, 37),
        "summary": (
            "Le « jeudi noir » à la Bourse de New York déclenche un krach "
            "boursier qui précipite le monde dans la Grande Dépression des "
            "années 1930."
        ),
        "before": (
            "Après des années de spéculation effrénée alimentée par "
            "l'achat d'actions à crédit, les cours de la Bourse de New York "
            "atteignent des niveaux jugés intenables."
        ),
        "during": (
            "Le 24 octobre 1929, une vague de ventes paniquées s'abat sur "
            "Wall Street ; malgré une intervention des grandes banques, la "
            "confiance s'effondre définitivement les jours suivants."
        ),
        "after": (
            "Le krach entraîne faillites bancaires et chômage de masse aux "
            "États-Unis, puis se propage à l'économie mondiale, provoquant "
            "la Grande Dépression."
        ),
        "narrative": [
            (
                "Durant les « années folles », la Bourse de New York connaît "
                "une hausse spectaculaire, largement alimentée par des "
                "investisseurs empruntant massivement pour acheter des "
                "actions, pariant sur une hausse continue des cours."
            ),
            (
                "Le 24 octobre 1929, surnommé « jeudi noir », une vague de "
                "ventes massives et paniquées s'abat sur le New York Stock "
                "Exchange. Un consortium de grandes banques tente "
                "d'enrayer la chute en rachetant des actions, offrant un "
                "répit temporaire."
            ),
            (
                "Mais la confiance ne revient pas : les 28 et 29 octobre, "
                "surnommés « lundi noir » et « mardi noir », voient de "
                "nouvelles chutes vertigineuses. En quelques jours, des "
                "milliards de dollars de valeur boursière s'évaporent, "
                "ruinant nombre d'investisseurs."
            ),
        ],
        "why_it_matters": (
            "Le krach de 1929 déclenche la Grande Dépression, la pire crise "
            "économique du XXe siècle, marquée par des faillites bancaires "
            "en série, un chômage massif et des répercussions économiques "
            "et politiques mondiales durant toute la décennie suivante."
        ),
        "characters": [
            {"name": "Herbert Hoover", "role": "Président des États-Unis", "emoji": "🏛️", "bg": "#E9E4D8"},
        ],
        "quiz_slug": "krach-1929-consequence",
    },
    "attaque-pearl-harbor": {
        "slug": "attaque-pearl-harbor",
        "title": "L'attaque de Pearl Harbor",
        "month": 12,
        "day": 7,
        "year": 1941,
        "date_label": "7 Décembre 1941",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Militaire",
        "location": "Hawaï, États-Unis",
        "location_label": "Base navale de Pearl Harbor",
        "map_pos": (12, 48),
        "summary": (
            "L'aviation japonaise attaque par surprise la flotte américaine "
            "du Pacifique, provoquant l'entrée en guerre des États-Unis "
            "dans la Seconde Guerre mondiale."
        ),
        "before": (
            "Les tensions entre les États-Unis et le Japon impérial "
            "s'aggravent après l'embargo américain sur le pétrole imposé "
            "en réponse à l'expansion japonaise en Asie."
        ),
        "during": (
            "Des avions japonais lancés depuis des porte-avions frappent "
            "sans avertissement la flotte américaine ancrée à Pearl Harbor, "
            "détruisant ou endommageant de nombreux navires de guerre."
        ),
        "after": (
            "Les États-Unis déclarent la guerre au Japon dès le lendemain, "
            "entraînant leur entrée dans le conflit mondial aux côtés des "
            "Alliés."
        ),
        "narrative": [
            (
                "Au matin du 7 décembre 1941, alors que les négociations "
                "diplomatiques se poursuivent officiellement à Washington, "
                "des centaines d'avions japonais décollent de porte-avions "
                "et frappent par surprise la base navale américaine de "
                "Pearl Harbor, à Hawaï."
            ),
            (
                "En un peu moins de deux heures, l'attaque coule ou "
                "endommage huit cuirassés américains et détruit près de "
                "200 avions, faisant environ 2 400 morts, pour la plupart "
                "des militaires. Les porte-avions américains, absents ce "
                "jour-là, échappent à la destruction."
            ),
            (
                "Le président Franklin D. Roosevelt qualifie le 7 décembre "
                "de « date qui restera dans l'infamie » devant le Congrès, "
                "qui vote la déclaration de guerre au Japon dès le "
                "lendemain."
            ),
        ],
        "why_it_matters": (
            "L'attaque de Pearl Harbor précipite l'entrée en guerre des "
            "États-Unis, jusque-là officiellement neutres, et transforme "
            "définitivement le conflit européen en une guerre véritablement "
            "mondiale."
        ),
        "characters": [
            {"name": "Franklin D. Roosevelt", "role": "Président des États-Unis", "emoji": "🏛️", "bg": "#E9E4D8"},
            {"name": "Isoroku Yamamoto", "role": "Amiral japonais", "emoji": "⚓", "bg": "#F3E8E1"},
        ],
        "quiz_slug": "pearl-harbor-consequence",
    },
    "bombardement-hiroshima": {
        "slug": "bombardement-hiroshima",
        "title": "Le bombardement d'Hiroshima",
        "month": 8,
        "day": 6,
        "year": 1945,
        "date_label": "6 Août 1945",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Militaire",
        "location": "Hiroshima, Japon",
        "location_label": "Hiroshima",
        "map_pos": (78, 40),
        "summary": (
            "Les États-Unis larguent la première bombe atomique de "
            "l'histoire militaire sur la ville d'Hiroshima, provoquant des "
            "destructions et des pertes humaines sans précédent."
        ),
        "before": (
            "Dans les derniers mois de la guerre du Pacifique, le Japon "
            "refuse de capituler malgré des bombardements conventionnels "
            "dévastateurs sur ses grandes villes."
        ),
        "during": (
            "Le bombardier américain Enola Gay largue la bombe atomique "
            "« Little Boy » sur Hiroshima, détruisant la majeure partie de "
            "la ville en quelques instants."
        ),
        "after": (
            "Une seconde bombe atomique frappe Nagasaki trois jours plus "
            "tard ; le Japon annonce sa capitulation le 15 août 1945, "
            "mettant fin à la Seconde Guerre mondiale."
        ),
        "narrative": [
            (
                "À l'été 1945, malgré une situation militaire désespérée, "
                "le gouvernement japonais refuse la capitulation sans "
                "conditions exigée par les Alliés, qui redoutent le coût "
                "humain d'une invasion terrestre du Japon."
            ),
            (
                "Le 6 août 1945 à 8h15 du matin, le bombardier américain "
                "Enola Gay largue sur Hiroshima la bombe atomique « Little "
                "Boy ». L'explosion détruit instantanément une grande "
                "partie de la ville et tue des dizaines de milliers de "
                "personnes sur le coup, un bilan qui continuera de "
                "s'alourdir dans les mois suivants du fait des radiations."
            ),
            (
                "Le Japon ne capitule pas immédiatement. Le 9 août, une "
                "seconde bombe atomique frappe la ville de Nagasaki. "
                "L'empereur Hirohito annonce la capitulation du Japon le "
                "15 août, mettant un terme définitif à la Seconde Guerre "
                "mondiale."
            ),
        ],
        "why_it_matters": (
            "Premier usage militaire de l'arme atomique de l'histoire, le "
            "bombardement d'Hiroshima précipite la fin de la Seconde Guerre "
            "mondiale tout en ouvrant l'ère nucléaire et ses lourdes "
            "questions éthiques et stratégiques, encore débattues "
            "aujourd'hui."
        ),
        "characters": [
            {"name": "Harry S. Truman", "role": "Président des États-Unis", "emoji": "🏛️", "bg": "#E9E4D8"},
            {"name": "Hirohito", "role": "Empereur du Japon", "emoji": "👑", "bg": "#FFF3C4"},
        ],
        "quiz_slug": "hiroshima-date",
    },
    "capitulation-allemande-1945": {
        "slug": "capitulation-allemande-1945",
        "title": "La capitulation allemande de 1945",
        "month": 5,
        "day": 8,
        "year": 1945,
        "date_label": "8 Mai 1945",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Militaire",
        "location": "Reims puis Berlin",
        "location_label": "Berlin, quartier de Karlshorst",
        "map_pos": (53, 30),
        "summary": (
            "La capitulation sans conditions de l'Allemagne nazie met fin à "
            "la Seconde Guerre mondiale en Europe, célébrée comme le "
            "« Jour de la Victoire »."
        ),
        "before": (
            "Après le suicide d'Hitler le 30 avril 1945 et la chute de "
            "Berlin encerclée par l'Armée rouge, l'effondrement militaire "
            "allemand est total."
        ),
        "during": (
            "Une première capitulation est signée à Reims le 7 mai ; une "
            "seconde cérémonie, exigée par Staline, se tient à Berlin dans "
            "la nuit du 8 au 9 mai."
        ),
        "after": (
            "La guerre continue en Asie jusqu'à la capitulation du Japon en "
            "août, mais le 8 mai reste commémoré comme la fin des combats "
            "en Europe."
        ),
        "narrative": [
            (
                "Fin avril 1945, l'Armée rouge encercle Berlin. Adolf "
                "Hitler se suicide dans son bunker le 30 avril, alors que "
                "les combats font rage dans les rues de la capitale "
                "allemande en ruines."
            ),
            (
                "Le 7 mai, le général Alfred Jodl signe à Reims, au "
                "quartier général du général Eisenhower, l'acte de "
                "capitulation sans conditions de toutes les forces "
                "allemandes. Staline, jugeant la cérémonie insuffisamment "
                "solennelle et voulant que la capitulation soit actée sur "
                "le sol allemand, exige une seconde signature."
            ),
            (
                "Dans la nuit du 8 au 9 mai, une nouvelle cérémonie se "
                "tient à Berlin-Karlshorst devant les représentants "
                "soviétiques. En France et dans la plupart des pays "
                "occidentaux, c'est le 8 mai qui reste célébré comme le "
                "jour de la victoire en Europe."
            ),
        ],
        "why_it_matters": (
            "La capitulation allemande met fin à près de six ans de guerre "
            "en Europe, ayant fait des dizaines de millions de morts, et "
            "ouvre la voie à la partition de l'Allemagne et au début de la "
            "guerre froide entre les Alliés occidentaux et l'URSS."
        ),
        "characters": [
            {"name": "Dwight D. Eisenhower", "role": "Commandant suprême allié", "emoji": "🎖️", "bg": "#E9E4D8"},
            {"name": "Joseph Staline", "role": "Dirigeant soviétique", "emoji": "⭐", "bg": "#F3E8E1"},
        ],
        "quiz_slug": "victoire-europe-mois",
    },
    "vol-de-gagarine": {
        "slug": "vol-de-gagarine",
        "title": "Le vol de Youri Gagarine",
        "month": 4,
        "day": 12,
        "year": 1961,
        "date_label": "12 Avril 1961",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Science",
        "location": "Baïkonour, URSS",
        "location_label": "Cosmodrome de Baïkonour",
        "map_pos": (66, 26),
        "summary": (
            "Le cosmonaute soviétique Youri Gagarine devient le premier "
            "être humain à voyager dans l'espace, à bord du vaisseau "
            "Vostok 1."
        ),
        "before": (
            "En pleine guerre froide, l'URSS et les États-Unis se livrent à "
            "une course à l'espace acharnée depuis le lancement du "
            "satellite Spoutnik en 1957."
        ),
        "during": (
            "Gagarine effectue une orbite complète autour de la Terre à "
            "bord de Vostok 1, un vol d'un peu moins de deux heures, avant "
            "d'atterrir en parachute en Russie."
        ),
        "after": (
            "Gagarine devient un héros mondial et un symbole de la "
            "propagande soviétique, relançant la course à l'espace qui "
            "mènera les Américains sur la Lune huit ans plus tard."
        ),
        "narrative": [
            (
                "Le 12 avril 1961, le cosmonaute soviétique Youri Gagarine, "
                "un pilote de chasse de 27 ans, décolle du cosmodrome de "
                "Baïkonour à bord du vaisseau Vostok 1 pour devenir le "
                "premier être humain à quitter l'atmosphère terrestre."
            ),
            (
                "En 108 minutes, Gagarine effectue une orbite complète "
                "autour de la Terre à une altitude d'environ 300 "
                "kilomètres. Durant le vol, largement automatisé, il "
                "observe et décrit la courbure de la Terre, une vision "
                "alors inédite pour un être humain."
            ),
            (
                "Le vaisseau redescend et Gagarine s'éjecte pour atterrir "
                "en parachute près de la Volga, comme prévu par la "
                "procédure soviétique. Il est immédiatement célébré comme "
                "un héros national et devient une figure mondiale de la "
                "conquête spatiale."
            ),
        ],
        "why_it_matters": (
            "Le vol de Gagarine constitue une victoire majeure de l'URSS "
            "dans la course à l'espace et pousse les États-Unis à "
            "accélérer leur propre programme spatial, qui aboutira à "
            "l'alunissage d'Apollo 11 en 1969."
        ),
        "characters": [
            {"name": "Youri Gagarine", "role": "Cosmonaute soviétique", "emoji": "👨‍🚀", "bg": "#E4E1E7"},
            {"name": "Sergueï Korolev", "role": "Ingénieur en chef du programme spatial", "emoji": "🚀", "bg": "#FDECD8"},
        ],
        "quiz_slug": "gagarine-duree",
    },
    "discours-i-have-a-dream": {
        "slug": "discours-i-have-a-dream",
        "title": "Le discours « I Have a Dream »",
        "month": 8,
        "day": 28,
        "year": 1963,
        "date_label": "28 Août 1963",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Société",
        "location": "Washington, États-Unis",
        "location_label": "Lincoln Memorial",
        "map_pos": (23, 37),
        "summary": (
            "Martin Luther King prononce son discours emblématique devant "
            "plus de 200 000 personnes, lors de la Marche sur Washington "
            "pour l'emploi et la liberté."
        ),
        "before": (
            "Le mouvement pour les droits civiques prend de l'ampleur aux "
            "États-Unis face à la ségrégation raciale persistante, "
            "notamment dans les États du Sud."
        ),
        "during": (
            "Devant le Lincoln Memorial, Martin Luther King prononce un "
            "discours appelant à la fin du racisme et à l'égalité entre "
            "Américains, culminant sur la formule « I have a dream »."
        ),
        "after": (
            "Le discours contribue à l'adoption du Civil Rights Act en "
            "1964 et du Voting Rights Act en 1965, interdisant la "
            "discrimination raciale légale aux États-Unis."
        ),
        "narrative": [
            (
                "Le 28 août 1963, plus de 200 000 personnes se rassemblent "
                "à Washington pour la « Marche sur Washington pour l'emploi "
                "et la liberté », réclamant la fin de la ségrégation "
                "raciale et l'égalité économique pour les Afro-Américains."
            ),
            (
                "Devant le Lincoln Memorial, le pasteur Martin Luther King "
                "prononce un discours qui restera l'un des plus célèbres du "
                "XXe siècle. S'écartant en partie de son texte préparé, il "
                "développe une vision d'une Amérique où ses enfants "
                "« ne seront pas jugés sur la couleur de leur peau mais sur "
                "le contenu de leur caractère »."
            ),
            (
                "Le discours, retransmis à la télévision devant des "
                "millions de téléspectateurs, marque un tournant dans la "
                "prise de conscience nationale sur les droits civiques aux "
                "États-Unis."
            ),
        ],
        "why_it_matters": (
            "Ce discours reste un symbole majeur du mouvement américain "
            "pour les droits civiques, qui aboutira l'année suivante au "
            "Civil Rights Act de 1964 interdisant la discrimination raciale "
            "dans de nombreux domaines de la vie publique."
        ),
        "characters": [
            {"name": "Martin Luther King", "role": "Pasteur, militant des droits civiques", "emoji": "🎙️", "bg": "#FDECD8"},
            {"name": "John Lewis", "role": "Militant, futur député", "emoji": "📢", "bg": "#F3E8E1"},
        ],
        "quiz_slug": "mlk-discours-lieu",
    },
    "revolution-doctobre": {
        "slug": "revolution-doctobre",
        "title": "La révolution d'Octobre",
        "month": 11,
        "day": 7,
        "year": 1917,
        "date_label": "7 Novembre 1917",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Politique",
        "location": "Petrograd, Russie",
        "location_label": "Palais d'Hiver",
        "map_pos": (62, 24),
        "summary": (
            "Les bolcheviks de Lénine renversent le gouvernement "
            "provisoire russe lors d'une insurrection presque sans effusion "
            "de sang, ouvrant la voie au premier État communiste du monde."
        ),
        "before": (
            "Affaibli par la Première Guerre mondiale et la révolution de "
            "février 1917 qui a renversé le tsar, le gouvernement "
            "provisoire russe perd le soutien populaire."
        ),
        "during": (
            "Des gardes rouges bolcheviks s'emparent des points "
            "stratégiques de Petrograd puis prennent d'assaut le Palais "
            "d'Hiver, siège du gouvernement provisoire."
        ),
        "after": (
            "Lénine proclame un gouvernement soviétique ; une guerre civile "
            "éclate bientôt en Russie, menant à la fondation de l'URSS en "
            "1922."
        ),
        "narrative": [
            (
                "Après l'abdication du tsar Nicolas II en février 1917, un "
                "gouvernement provisoire peine à s'imposer face à une "
                "population russe épuisée par la guerre et la famine, "
                "tandis que les soviets — conseils d'ouvriers et de "
                "soldats — gagnent en influence, notamment sous "
                "l'impulsion des bolcheviks de Vladimir Lénine."
            ),
            (
                "Dans la nuit du 6 au 7 novembre 1917 (24-25 octobre selon "
                "le calendrier julien alors en vigueur en Russie, d'où le "
                "nom de « révolution d'Octobre »), des gardes rouges "
                "bolcheviks occupent sans grande résistance les points "
                "stratégiques de Petrograd — gares, ponts, centrale "
                "téléphonique — avant de prendre d'assaut le Palais "
                "d'Hiver, siège du gouvernement provisoire."
            ),
            (
                "Le lendemain, Lénine proclame la formation d'un "
                "gouvernement soviétique et annonce des décrets immédiats "
                "sur la paix et sur la terre, cherchant à s'assurer le "
                "soutien des soldats et des paysans."
            ),
        ],
        "why_it_matters": (
            "La révolution d'Octobre installe le premier État communiste de "
            "l'histoire, qui deviendra l'URSS en 1922 et façonnera une "
            "grande partie de la géopolitique mondiale du XXe siècle, "
            "jusqu'à sa dissolution en 1991."
        ),
        "characters": [
            {"name": "Vladimir Lénine", "role": "Chef des bolcheviks", "emoji": "📢", "bg": "#FDECD8"},
            {"name": "Alexandre Kerenski", "role": "Chef du gouvernement provisoire", "emoji": "🏛️", "bg": "#E9E4D8"},
        ],
        "quiz_slug": "revolution-octobre-lieu",
    },
    "these-de-luther": {
        "slug": "these-de-luther",
        "title": "Les 95 thèses de Luther",
        "month": 10,
        "day": 31,
        "year": 1517,
        "date_label": "31 Octobre 1517",
        "era": "Renaissance",
        "era_key": "renaissance",
        "category": "Religion",
        "location": "Wittenberg, Saint-Empire",
        "location_label": "Église du château de Wittenberg",
        "map_pos": (52, 27),
        "summary": (
            "Le moine Martin Luther affiche ses 95 thèses critiquant la "
            "vente des indulgences, un geste considéré comme le point de "
            "départ de la Réforme protestante."
        ),
        "before": (
            "L'Église catholique finance notamment la basilique Saint-Pierre "
            "de Rome par la vente d'indulgences, promettant la réduction des "
            "peines des péchés en échange d'argent."
        ),
        "during": (
            "Le moine augustin Martin Luther rédige 95 thèses théologiques "
            "contestant cette pratique et, selon la tradition, les affiche "
            "sur la porte de l'église du château de Wittenberg."
        ),
        "after": (
            "Le texte se diffuse rapidement grâce à l'imprimerie et "
            "déclenche une rupture religieuse majeure, menant à la "
            "naissance du protestantisme."
        ),
        "narrative": [
            (
                "Au début du XVIe siècle, l'Église catholique autorise la "
                "vente d'indulgences pour financer notamment la "
                "construction de la basilique Saint-Pierre de Rome. Le "
                "prédicateur Johann Tetzel promeut cette pratique en "
                "Allemagne avec un zèle qui scandalise le moine augustin "
                "Martin Luther, professeur de théologie à Wittenberg."
            ),
            (
                "Le 31 octobre 1517, Luther rédige 95 thèses en latin "
                "contestant la théologie des indulgences et, selon la "
                "tradition la plus répandue, les affiche sur la porte de "
                "l'église du château de Wittenberg — un lieu qui servait "
                "aussi de tableau d'affichage universitaire."
            ),
            (
                "Grâce à l'imprimerie récemment développée par Gutenberg, "
                "le texte est rapidement traduit en allemand et diffusé "
                "dans tout le Saint-Empire, déclenchant un débat théologique "
                "qui échappe vite au contrôle de l'Église romaine."
            ),
        ],
        "why_it_matters": (
            "Cet acte est traditionnellement considéré comme le point de "
            "départ de la Réforme protestante, qui va diviser durablement "
            "le christianisme occidental et bouleverser la carte religieuse "
            "et politique de l'Europe pour les siècles suivants."
        ),
        "characters": [
            {"name": "Martin Luther", "role": "Moine, théologien", "emoji": "📜", "bg": "#FDECD8"},
            {"name": "Johann Tetzel", "role": "Prédicateur des indulgences", "emoji": "⛪", "bg": "#E9E4D8"},
        ],
        "quiz_slug": "luther-consequence",
    },
    "liberation-mandela": {
        "slug": "liberation-mandela",
        "title": "La libération de Nelson Mandela",
        "month": 2,
        "day": 11,
        "year": 1990,
        "date_label": "11 Février 1990",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Politique",
        "location": "Le Cap, Afrique du Sud",
        "location_label": "Prison de Victor Verster",
        "map_pos": (52, 68),
        "summary": (
            "Après 27 ans d'emprisonnement, Nelson Mandela est libéré, "
            "marquant le début du démantèlement officiel du régime "
            "d'apartheid en Afrique du Sud."
        ),
        "before": (
            "Emprisonné depuis 1962 pour son opposition au régime "
            "ségrégationniste de l'apartheid, Mandela est devenu le symbole "
            "mondial de la lutte contre la discrimination raciale en "
            "Afrique du Sud."
        ),
        "during": (
            "Sous la pression internationale croissante, le président "
            "sud-africain Frederik de Klerk annonce la libération de "
            "Mandela, qui sort de prison le 11 février 1990 sous les "
            "acclamations."
        ),
        "after": (
            "Mandela négocie avec de Klerk la fin de l'apartheid, avant "
            "d'être élu premier président noir d'Afrique du Sud lors des "
            "premières élections multiraciales de 1994."
        ),
        "narrative": [
            (
                "Condamné à la prison à vie en 1964 pour sabotage et "
                "complot contre l'État sud-africain, Nelson Mandela, "
                "dirigeant du Congrès national africain (ANC), devient "
                "pendant ses 27 années de détention le symbole mondial de "
                "la résistance au régime d'apartheid."
            ),
            (
                "Face à des sanctions économiques internationales "
                "croissantes et à une contestation interne grandissante, le "
                "président Frederik de Klerk, arrivé au pouvoir en 1989, "
                "amorce une politique de réformes et lève l'interdiction "
                "frappant l'ANC."
            ),
            (
                "Le 11 février 1990, Nelson Mandela sort de la prison de "
                "Victor Verster, près du Cap, sous les acclamations de la "
                "foule et une couverture médiatique mondiale. Il entame "
                "aussitôt des négociations avec de Klerk pour démanteler "
                "l'apartheid."
            ),
        ],
        "why_it_matters": (
            "La libération de Mandela ouvre la voie aux négociations qui "
            "mettront fin à l'apartheid et aux premières élections "
            "multiraciales de 1994, lors desquelles Mandela est élu "
            "président, devenant un symbole mondial de réconciliation."
        ),
        "characters": [
            {"name": "Nelson Mandela", "role": "Dirigeant de l'ANC", "emoji": "✊", "bg": "#FDECD8"},
            {"name": "Frederik de Klerk", "role": "Président d'Afrique du Sud", "emoji": "🏛️", "bg": "#E9E4D8"},
        ],
        "quiz_slug": "mandela-duree-prison",
    },
    "lancement-spoutnik": {
        "slug": "lancement-spoutnik",
        "title": "Le lancement de Spoutnik 1",
        "month": 10,
        "day": 4,
        "year": 1957,
        "date_label": "4 Octobre 1957",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Science",
        "location": "Baïkonour, URSS",
        "location_label": "Cosmodrome de Baïkonour",
        "map_pos": (66, 26),
        "summary": (
            "L'URSS met sur orbite Spoutnik 1, premier satellite artificiel "
            "de l'histoire, déclenchant la course à l'espace avec les "
            "États-Unis."
        ),
        "before": (
            "En pleine guerre froide, l'URSS et les États-Unis développent "
            "chacun des programmes de fusées, initialement à but militaire, "
            "capables d'atteindre l'espace."
        ),
        "during": (
            "Une fusée soviétique R-7 place en orbite Spoutnik 1, une "
            "sphère métallique de 58 centimètres émettant un simple signal "
            "radio régulier."
        ),
        "after": (
            "La nouvelle provoque un choc aux États-Unis, qui créent la "
            "NASA l'année suivante et accélèrent leur propre programme "
            "spatial."
        ),
        "narrative": [
            (
                "Le 4 octobre 1957, l'Union soviétique lance depuis le "
                "cosmodrome de Baïkonour une fusée R-7 emportant Spoutnik "
                "1, une sphère métallique polie d'à peine 58 centimètres de "
                "diamètre équipée de quatre antennes radio."
            ),
            (
                "Une fois en orbite, le satellite se contente d'émettre un "
                "signal radio simple et régulier, un « bip-bip » captable "
                "par des radioamateurs du monde entier, preuve manifeste de "
                "la réussite soviétique."
            ),
            (
                "Aux États-Unis, la nouvelle provoque une onde de choc "
                "connue sous le nom de « moment Spoutnik » : l'opinion "
                "publique et le gouvernement américains, pris de court, "
                "craignent d'avoir pris du retard technologique et "
                "militaire sur l'URSS."
            ),
        ],
        "why_it_matters": (
            "Spoutnik 1 marque le début de l'ère spatiale et de la course "
            "à l'espace entre les États-Unis et l'URSS, qui aboutira "
            "notamment à la création de la NASA en 1958 et, onze ans plus "
            "tard, à l'alunissage d'Apollo 11."
        ),
        "characters": [
            {"name": "Sergueï Korolev", "role": "Ingénieur en chef du programme spatial", "emoji": "🚀", "bg": "#FDECD8"},
            {"name": "Nikita Khrouchtchev", "role": "Dirigeant soviétique", "emoji": "⭐", "bg": "#F3E8E1"},
        ],
        "quiz_slug": "spoutnik-annee",
    },
    "chute-empire-romain-occident": {
        "slug": "chute-empire-romain-occident",
        "title": "La chute de l'Empire romain d'Occident",
        "month": 9,
        "day": 4,
        "year": 476,
        "date_label": "4 Septembre 476",
        "era": "Antiquité",
        "era_key": "antiquite",
        "category": "Politique",
        "location": "Ravenne, Italie",
        "location_label": "Ravenne, capitale impériale",
        "map_pos": (52, 41),
        "summary": (
            "Le chef germanique Odoacre dépose le dernier empereur romain "
            "d'Occident, Romulus Augustule, marquant traditionnellement la "
            "fin de l'Antiquité en Europe."
        ),
        "before": (
            "Affaibli par des décennies d'invasions, de crises économiques "
            "et de coups d'État militaires, l'Empire romain d'Occident ne "
            "contrôle plus qu'une fraction de son territoire d'origine."
        ),
        "during": (
            "Le chef militaire germanique Odoacre renverse le jeune "
            "empereur Romulus Augustule et se proclame roi d'Italie, sans "
            "nommer de nouvel empereur."
        ),
        "after": (
            "Odoacre renvoie les insignes impériaux à Constantinople, "
            "laissant l'empereur d'Orient seul héritier officiel du titre "
            "impérial romain."
        ),
        "narrative": [
            (
                "Au Ve siècle, l'Empire romain d'Occident est exsangue : "
                "invasions germaniques répétées, généraux qui font et "
                "défont les empereurs à leur guise, économie exsangue. Le "
                "dernier empereur, Romulus Augustule, n'a que quelques mois "
                "de règne, porté au pouvoir enfant par son propre père."
            ),
            (
                "En 476, Odoacre, chef militaire d'origine germanique à la "
                "tête de troupes fédérées au service de Rome, se retourne "
                "contre le pouvoir impérial après le refus de lui accorder "
                "des terres en Italie. Il dépose Romulus Augustule sans "
                "effusion de sang notable et se proclame roi d'Italie."
            ),
            (
                "Plutôt que de se faire proclamer empereur à son tour, "
                "Odoacre renvoie les insignes impériaux à Constantinople, "
                "reconnaissant symboliquement l'empereur d'Orient, Zénon, "
                "comme seul souverain légitime — mettant ainsi fin à la "
                "lignée des empereurs d'Occident."
            ),
        ],
        "why_it_matters": (
            "Cet événement est conventionnellement retenu par les "
            "historiens comme la date de la fin de l'Empire romain "
            "d'Occident et de l'Antiquité, ouvrant la période du Moyen Âge "
            "en Europe occidentale."
        ),
        "characters": [
            {"name": "Odoacre", "role": "Chef germanique, roi d'Italie", "emoji": "🛡️", "bg": "#E9E4D8"},
            {"name": "Romulus Augustule", "role": "Dernier empereur d'Occident", "emoji": "👑", "bg": "#FFF3C4"},
        ],
        "quiz_slug": "chute-rome-consequence",
    },
    "invention-machine-vapeur-watt": {
        "slug": "invention-machine-vapeur-watt",
        "title": "Le brevet de la machine à vapeur de Watt",
        "month": 1,
        "day": 5,
        "year": 1769,
        "date_label": "5 Janvier 1769",
        "era": "Renaissance",
        "era_key": "renaissance",
        "category": "Science",
        "location": "Écosse, Royaume-Uni",
        "location_label": "Glasgow",
        "map_pos": (44, 21),
        "summary": (
            "L'ingénieur écossais James Watt dépose le brevet de sa machine "
            "à vapeur perfectionnée, une innovation décisive qui va "
            "déclencher la révolution industrielle."
        ),
        "before": (
            "Les machines à vapeur existantes, comme celle de Newcomen, "
            "sont peu efficaces énergétiquement et limitées au pompage de "
            "l'eau dans les mines."
        ),
        "during": (
            "James Watt met au point un condenseur séparé qui améliore "
            "radicalement le rendement de la machine à vapeur, et en "
            "dépose le brevet."
        ),
        "after": (
            "Associé à l'industriel Matthew Boulton, Watt commercialise ses "
            "machines, qui se répandent dans les mines puis les usines "
            "textiles, propulsant la révolution industrielle britannique."
        ),
        "narrative": [
            (
                "Dans les années 1760, l'ingénieur écossais James Watt "
                "travaille comme réparateur d'instruments à l'université de "
                "Glasgow, où on lui confie la réparation d'un modèle de "
                "machine à vapeur de Newcomen, utilisée pour pomper l'eau "
                "des mines."
            ),
            (
                "Watt remarque que la machine gaspille énormément d'énergie "
                "en refroidissant puis en réchauffant sans cesse le même "
                "cylindre. Il conçoit un condenseur séparé, permettant de "
                "maintenir le cylindre principal chaud en permanence, ce "
                "qui améliore considérablement le rendement énergétique."
            ),
            (
                "Le 5 janvier 1769, Watt dépose le brevet de son invention. "
                "Faute de moyens pour l'exploiter seul, il s'associe "
                "quelques années plus tard à l'industriel Matthew Boulton, "
                "et leurs machines à vapeur perfectionnées se répandent "
                "rapidement dans les mines puis les usines textiles "
                "britanniques."
            ),
        ],
        "why_it_matters": (
            "L'amélioration de la machine à vapeur par Watt est considérée "
            "comme l'un des déclencheurs majeurs de la révolution "
            "industrielle, en fournissant une source d'énergie mécanique "
            "fiable qui transformera profondément l'économie et la société "
            "des XVIIIe et XIXe siècles."
        ),
        "characters": [
            {"name": "James Watt", "role": "Ingénieur, inventeur", "emoji": "⚙️", "bg": "#E4E1E7"},
            {"name": "Matthew Boulton", "role": "Industriel, associé", "emoji": "🏭", "bg": "#F3E8E1"},
        ],
        "quiz_slug": "watt-invention",
    },
    "decouverte-tombe-toutankhamon": {
        "slug": "decouverte-tombe-toutankhamon",
        "title": "La découverte de la tombe de Toutânkhamon",
        "month": 11,
        "day": 4,
        "year": 1922,
        "date_label": "4 Novembre 1922",
        "era": "Époque Contemporaine",
        "era_key": "epoque-contemporaine",
        "category": "Exploration",
        "location": "Vallée des Rois, Égypte",
        "location_label": "Vallée des Rois",
        "map_pos": (56, 44),
        "summary": (
            "L'archéologue britannique Howard Carter découvre l'entrée de "
            "la tombe intacte du pharaon Toutânkhamon, l'une des plus "
            "grandes découvertes archéologiques du XXe siècle."
        ),
        "before": (
            "Après des années de fouilles infructueuses financées par Lord "
            "Carnarvon, Howard Carter cherche la tombe d'un pharaon mineur "
            "dont l'existence n'était que supposée."
        ),
        "during": (
            "Les ouvriers de Carter dégagent un escalier menant à une porte "
            "scellée portant les sceaux intacts de Toutânkhamon, encore "
            "jamais pillée."
        ),
        "after": (
            "Le dégagement et l'inventaire du trésor funéraire, comprenant "
            "le célèbre masque en or, dureront près de dix ans et "
            "captiveront le monde entier."
        ),
        "narrative": [
            (
                "Depuis 1907, l'archéologue britannique Howard Carter fouille "
                "la Vallée des Rois pour le compte de son mécène, Lord "
                "Carnarvon, à la recherche de la tombe du pharaon "
                "Toutânkhamon, un souverain mineur mort jeune dont "
                "l'emplacement du tombeau restait inconnu."
            ),
            (
                "Le 4 novembre 1922, après des années de recherches "
                "infructueuses et alors que le financement touchait à sa "
                "fin, les ouvriers de Carter découvrent une marche taillée "
                "dans la roche. Elle mène à un escalier, puis à une porte "
                "scellée portant des cachets encore intacts."
            ),
            (
                "Le 26 novembre, Carter perce un petit trou dans la porte "
                "intérieure et, à la lueur d'une bougie, aperçoit « des "
                "choses merveilleuses » : la tombe, quasiment inviolée "
                "depuis plus de 3 000 ans, regorge d'un trésor funéraire "
                "exceptionnel, dont le célèbre masque funéraire en or du "
                "pharaon."
            ),
        ],
        "why_it_matters": (
            "La découverte de la tombe de Toutânkhamon reste l'une des plus "
            "importantes de l'archéologie moderne : sa richesse quasi "
            "intacte a considérablement enrichi la connaissance de l'Égypte "
            "ancienne et déclenché un engouement mondial pour "
            "l'égyptologie."
        ),
        "characters": [
            {"name": "Howard Carter", "role": "Archéologue britannique", "emoji": "🔍", "bg": "#E4E1E7"},
            {"name": "Lord Carnarvon", "role": "Mécène de l'expédition", "emoji": "💰", "bg": "#FDECD8"},
            {"name": "Toutânkhamon", "role": "Pharaon d'Égypte", "emoji": "👑", "bg": "#FFF3C4"},
        ],
        "quiz_slug": "toutankhamon-decouvreur",
    },
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
    "tuileries-consequence": {
        "slug": "tuileries-consequence",
        "era": "Révolution Française",
        "prompt": "Quelle a été la conséquence directe de la prise des Tuileries le 10 août 1792 ?",
        "options": [
            "Le couronnement de Louis XVI",
            "La suspension du roi et la fin de la monarchie de fait",
            "La signature de la paix avec la Prusse",
            "La construction d'un nouveau palais royal",
        ],
        "correct_index": 1,
        "fun_fact": (
            "Après le 10 août 1792, l'Assemblée législative suspend Louis "
            "XVI. Six semaines plus tard, la Convention proclame la première "
            "République française."
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
    "mur-berlin-annee": {
        "slug": "mur-berlin-annee",
        "era": "XXe siècle",
        "prompt": "En quelle année le mur de Berlin est-il tombé ?",
        "options": ["1961", "1975", "1989", "1991"],
        "correct_index": 2,
        "fun_fact": (
            "Le mur de Berlin, érigé en 1961, est tombé le 9 novembre 1989 "
            "après une annonce gouvernementale confuse qui a poussé des "
            "milliers de Berlinois vers les points de passage."
        ),
    },
    "debarquement-date": {
        "slug": "debarquement-date",
        "era": "XXe siècle",
        "prompt": "Sur combien de plages les troupes alliées ont-elles débarqué le 6 juin 1944 ?",
        "options": ["Deux", "Trois", "Cinq", "Sept"],
        "correct_index": 2,
        "fun_fact": (
            "Les Alliés ont débarqué sur cinq plages normandes codées Utah, "
            "Omaha, Gold, Juno et Sword, appuyés par des parachutistes "
            "largués dans la nuit du 5 au 6 juin 1944."
        ),
    },
    "armistice-heure": {
        "slug": "armistice-heure",
        "era": "XXe siècle",
        "prompt": "À quelle heure les combats ont-ils officiellement cessé le 11 novembre 1918 ?",
        "options": ["6 heures", "9 heures", "11 heures", "Minuit"],
        "correct_index": 2,
        "fun_fact": (
            "L'armistice, signé à 5h15 dans un wagon en forêt de Compiègne, "
            "est entré en vigueur à 11 heures précises — le « onzième jour "
            "du onzième mois à la onzième heure »."
        ),
    },
    "independance-americaine-annee": {
        "slug": "independance-americaine-annee",
        "era": "Renaissance",
        "prompt": "Qui a principalement rédigé la déclaration d'indépendance américaine de 1776 ?",
        "options": ["George Washington", "Thomas Jefferson", "Benjamin Franklin", "John Adams"],
        "correct_index": 1,
        "fun_fact": (
            "Thomas Jefferson a rédigé l'essentiel du texte, adopté par le "
            "Congrès continental à Philadelphie le 4 juillet 1776, proclamant "
            "l'indépendance des treize colonies britanniques."
        ),
    },
    "colomb-annee": {
        "slug": "colomb-annee",
        "era": "Renaissance",
        "prompt": "En quelle année l'expédition de Christophe Colomb atteint-elle les Amériques ?",
        "options": ["1453", "1492", "1517", "1534"],
        "correct_index": 1,
        "fun_fact": (
            "Le 12 octobre 1492, après 36 jours de traversée, l'expédition "
            "de Colomb débarque sur une île des Bahamas qu'il baptise San "
            "Salvador, persuadé d'avoir atteint les abords de l'Asie."
        ),
    },
    "nuit-4-aout-consequence": {
        "slug": "nuit-4-aout-consequence",
        "era": "Révolution Française",
        "prompt": "Qu'a aboli l'Assemblée constituante dans la nuit du 4 août 1789 ?",
        "options": [
            "La monarchie",
            "Les privilèges féodaux",
            "L'esclavage dans les colonies",
            "La peine de mort",
        ],
        "correct_index": 1,
        "fun_fact": (
            "Dans un mouvement d'entraînement collectif, nobles et clergé "
            "renoncent tour à tour à leurs privilèges féodaux et fiscaux, "
            "mettant fin de facto au système seigneurial en France."
        ),
    },
    "waterloo-consequence": {
        "slug": "waterloo-consequence",
        "era": "Époque Contemporaine",
        "prompt": "Qu'est-il arrivé à Napoléon après sa défaite à Waterloo ?",
        "options": [
            "Il a repris le pouvoir en France",
            "Il a été exilé sur l'île de Sainte-Hélène",
            "Il a été exécuté",
            "Il est devenu roi d'Espagne",
        ],
        "correct_index": 1,
        "fun_fact": (
            "Napoléon abdique le 22 juin 1815, quatre jours après Waterloo, "
            "et est exilé par les Britanniques sur l'île isolée de "
            "Sainte-Hélène, dans l'Atlantique Sud, où il mourra en 1821."
        ),
    },
    "sacre-napoleon-lieu": {
        "slug": "sacre-napoleon-lieu",
        "era": "Époque Contemporaine",
        "prompt": "Qui a couronné Napoléon Ier lors de son sacre en 1804 ?",
        "options": [
            "Le pape Pie VII",
            "Napoléon s'est couronné lui-même",
            "Le roi d'Espagne",
            "L'archevêque de Paris",
        ],
        "correct_index": 1,
        "fun_fact": (
            "Bien que le pape Pie VII ait fait le déplacement de Rome pour "
            "bénir les insignes impériaux, c'est Napoléon lui-même qui a "
            "posé la couronne sur sa tête, un geste hautement symbolique."
        ),
    },
    "constantinople-consequence": {
        "slug": "constantinople-consequence",
        "era": "Moyen Âge",
        "prompt": "Quel empire prend fin avec la chute de Constantinople en 1453 ?",
        "options": [
            "L'Empire romain d'Occident",
            "L'Empire byzantin",
            "L'Empire perse",
            "L'Empire carolingien",
        ],
        "correct_index": 1,
        "fun_fact": (
            "La chute de Constantinople met fin à l'Empire byzantin, "
            "héritier direct de l'Empire romain d'Orient depuis plus de "
            "onze siècles, et marque pour beaucoup la fin du Moyen Âge."
        ),
    },
    "magna-carta-principe": {
        "slug": "magna-carta-principe",
        "era": "Moyen Âge",
        "prompt": "Quel principe la Magna Carta de 1215 a-t-elle établi ?",
        "options": [
            "Le suffrage universel",
            "La limitation du pouvoir royal face aux barons",
            "L'abolition de l'esclavage",
            "La liberté de la presse",
        ],
        "correct_index": 1,
        "fun_fact": (
            "La Magna Carta garantit notamment qu'aucun homme libre ne peut "
            "être emprisonné sans jugement légal, posant une limite inédite "
            "au pouvoir absolu du roi d'Angleterre."
        ),
    },
    "vesuve-consequence": {
        "slug": "vesuve-consequence",
        "era": "Antiquité",
        "prompt": "Qu'est-il arrivé à Pompéi après l'éruption du Vésuve en l'an 79 ?",
        "options": [
            "La ville a été reconstruite immédiatement",
            "La ville a été ensevelie et oubliée pendant des siècles",
            "La ville a été déplacée",
            "La ville est devenue une nouvelle capitale romaine",
        ],
        "correct_index": 1,
        "fun_fact": (
            "Ensevelie sous plusieurs mètres de cendres, Pompéi a été "
            "oubliée pendant plus de seize siècles avant d'être redécouverte "
            "par des fouilles archéologiques au XVIIIe siècle."
        ),
    },
    "krach-1929-consequence": {
        "slug": "krach-1929-consequence",
        "era": "Époque Contemporaine",
        "prompt": "Quelle crise économique majeure le krach de 1929 a-t-il déclenchée ?",
        "options": [
            "La Grande Dépression",
            "La crise du pétrole",
            "L'hyperinflation allemande",
            "La crise des subprimes",
        ],
        "correct_index": 0,
        "fun_fact": (
            "Le krach de Wall Street en octobre 1929 précipite la Grande "
            "Dépression, la pire crise économique du XXe siècle, marquée "
            "par un chômage de masse dans le monde entier."
        ),
    },
    "pearl-harbor-consequence": {
        "slug": "pearl-harbor-consequence",
        "era": "Époque Contemporaine",
        "prompt": "Quelle a été la conséquence directe de l'attaque de Pearl Harbor ?",
        "options": [
            "Le Japon a capitulé",
            "Les États-Unis sont entrés en guerre",
            "La France a été libérée",
            "L'URSS a rejoint l'Axe",
        ],
        "correct_index": 1,
        "fun_fact": (
            "Le lendemain de l'attaque du 7 décembre 1941, les États-Unis "
            "déclarent la guerre au Japon, entraînant leur entrée dans la "
            "Seconde Guerre mondiale."
        ),
    },
    "hiroshima-date": {
        "slug": "hiroshima-date",
        "era": "Époque Contemporaine",
        "prompt": "En quelle année la bombe atomique a-t-elle été larguée sur Hiroshima ?",
        "options": ["1943", "1944", "1945", "1946"],
        "correct_index": 2,
        "fun_fact": (
            "Le 6 août 1945, le bombardier Enola Gay largue la première "
            "bombe atomique de l'histoire militaire sur Hiroshima, "
            "précipitant la capitulation du Japon quelques jours plus tard."
        ),
    },
    "victoire-europe-mois": {
        "slug": "victoire-europe-mois",
        "era": "Époque Contemporaine",
        "prompt": "En quel mois la capitulation allemande de 1945 a-t-elle été signée ?",
        "options": ["Janvier", "Mai", "Août", "Décembre"],
        "correct_index": 1,
        "fun_fact": (
            "L'Allemagne capitule le 8 mai 1945, mettant fin à la Seconde "
            "Guerre mondiale en Europe — une date encore commémorée chaque "
            "année en France."
        ),
    },
    "gagarine-duree": {
        "slug": "gagarine-duree",
        "era": "Époque Contemporaine",
        "prompt": "Qu'a accompli Youri Gagarine le 12 avril 1961 ?",
        "options": [
            "Le premier alunissage",
            "Le premier vol spatial habité",
            "La première sortie dans l'espace",
            "Le premier satellite artificiel",
        ],
        "correct_index": 1,
        "fun_fact": (
            "En 108 minutes, Gagarine devient le premier être humain à "
            "voyager dans l'espace, effectuant une orbite complète autour "
            "de la Terre à bord de Vostok 1."
        ),
    },
    "mlk-discours-lieu": {
        "slug": "mlk-discours-lieu",
        "era": "Époque Contemporaine",
        "prompt": "Où Martin Luther King a-t-il prononcé son discours « I Have a Dream » ?",
        "options": [
            "Devant la Maison-Blanche",
            "Devant le Lincoln Memorial à Washington",
            "À l'ONU à New York",
            "Au Capitole",
        ],
        "correct_index": 1,
        "fun_fact": (
            "Le 28 août 1963, King prononce son discours devant plus de "
            "200 000 personnes rassemblées au Lincoln Memorial lors de la "
            "Marche sur Washington."
        ),
    },
    "revolution-octobre-lieu": {
        "slug": "revolution-octobre-lieu",
        "era": "Époque Contemporaine",
        "prompt": "Quel bâtiment les bolcheviks prennent-ils d'assaut lors de la révolution d'Octobre ?",
        "options": [
            "Le Kremlin",
            "Le Palais d'Hiver",
            "La cathédrale Saint-Basile",
            "Le palais de Peterhof",
        ],
        "correct_index": 1,
        "fun_fact": (
            "Le Palais d'Hiver de Petrograd, siège du gouvernement "
            "provisoire, est pris d'assaut par les gardes rouges bolcheviks "
            "dans la nuit du 6 au 7 novembre 1917."
        ),
    },
    "luther-consequence": {
        "slug": "luther-consequence",
        "era": "Renaissance",
        "prompt": "Quel mouvement religieux les 95 thèses de Luther ont-elles déclenché ?",
        "options": [
            "La Réforme protestante",
            "Les croisades",
            "Le schisme d'Orient",
            "L'Inquisition",
        ],
        "correct_index": 0,
        "fun_fact": (
            "En contestant la vente des indulgences en 1517, Luther "
            "déclenche la Réforme protestante, qui divisera durablement le "
            "christianisme occidental."
        ),
    },
    "mandela-duree-prison": {
        "slug": "mandela-duree-prison",
        "era": "Époque Contemporaine",
        "prompt": "Combien d'années Nelson Mandela a-t-il passées en prison avant sa libération en 1990 ?",
        "options": ["7 ans", "17 ans", "27 ans", "37 ans"],
        "correct_index": 2,
        "fun_fact": (
            "Emprisonné en 1962 pour son opposition à l'apartheid, Mandela "
            "est libéré le 11 février 1990 après 27 ans de détention, "
            "devenant plus tard le premier président noir d'Afrique du Sud."
        ),
    },
    "spoutnik-annee": {
        "slug": "spoutnik-annee",
        "era": "Époque Contemporaine",
        "prompt": "En quelle année l'URSS a-t-elle lancé Spoutnik 1, premier satellite artificiel ?",
        "options": ["1949", "1957", "1961", "1969"],
        "correct_index": 1,
        "fun_fact": (
            "Lancé le 4 octobre 1957, Spoutnik 1 marque le début de l'ère "
            "spatiale et déclenche la course à l'espace entre l'URSS et les "
            "États-Unis."
        ),
    },
    "chute-rome-consequence": {
        "slug": "chute-rome-consequence",
        "era": "Antiquité",
        "prompt": "Qui dépose le dernier empereur romain d'Occident en 476 ?",
        "options": ["Attila", "Odoacre", "Clovis", "Charlemagne"],
        "correct_index": 1,
        "fun_fact": (
            "Le chef germanique Odoacre dépose Romulus Augustule en 476 et "
            "renvoie les insignes impériaux à Constantinople — une date "
            "conventionnellement retenue comme la fin de l'Antiquité."
        ),
    },
    "watt-invention": {
        "slug": "watt-invention",
        "era": "Renaissance",
        "prompt": "Quelle amélioration James Watt apporte-t-il à la machine à vapeur en 1769 ?",
        "options": [
            "Un condenseur séparé",
            "Des roues en caoutchouc",
            "Un moteur électrique",
            "Une chaudière en verre",
        ],
        "correct_index": 0,
        "fun_fact": (
            "En ajoutant un condenseur séparé, Watt évite de refroidir puis "
            "réchauffer sans cesse le même cylindre, améliorant "
            "considérablement le rendement énergétique de la machine à "
            "vapeur."
        ),
    },
    "toutankhamon-decouvreur": {
        "slug": "toutankhamon-decouvreur",
        "era": "Époque Contemporaine",
        "prompt": "Qui a découvert la tombe de Toutânkhamon en 1922 ?",
        "options": ["Jean-François Champollion", "Howard Carter", "Heinrich Schliemann", "Flinders Petrie"],
        "correct_index": 1,
        "fun_fact": (
            "Le 4 novembre 1922, l'archéologue britannique Howard Carter "
            "découvre l'entrée de la tombe quasi intacte de Toutânkhamon "
            "dans la Vallée des Rois, après des années de recherches."
        ),
    },
}

DEFAULT_QUIZ_SLUG = "bastille-importance"
