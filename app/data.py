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
}

DEFAULT_QUIZ_SLUG = "bastille-importance"
