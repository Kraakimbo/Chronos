"""Study-level-adapted event content and quiz questions.

Chronos already stores a study_level on each user (app.models.STUDY_LEVELS:
"enfant" / "college" / "lycee" / "etudiant_adulte"), but every event only
had one version of its text, written for an adult reader, and one quiz
question of fixed difficulty. This module adds, per event slug, a
narrative rewritten at each of the four levels -- simpler vocabulary and
shorter sentences for "enfant", up to more nuanced/detailed phrasing for
"etudiant_adulte" -- plus a matching quiz question per level whose prompt
and wrong answers are built from that level's own wording, so a harder
level asks a harder, more specific question.

Coverage is partial by design: this started as a pilot on a handful of
events (spanning eras/categories) to validate tone before rewriting all
45. See app.data.EVENTS for the slugs still missing an entry here --
resolve_event_content()/resolve_quiz() fall back to the original
single-level text for those, so nothing breaks for events not yet
covered.

Each level's dict for an event has the same shape as the relevant
subset of app.data.EVENTS[slug]: summary, before, during, after,
narrative (list of paragraphs), why_it_matters. Each level's quiz dict
has the same shape as app.data.QUIZ_QUESTIONS[*]: prompt, options,
correct_index, fun_fact.
"""

from app.models import STUDY_LEVELS

DEFAULT_LEVEL = "etudiant_adulte"


CONTENT_BY_LEVEL = {
    "prise-de-la-bastille": {
        "enfant": {
            "summary": (
                "Le 14 juillet 1789, les habitants de Paris attaquent la "
                "Bastille, une grande prison-forteresse. C'est le début "
                "de la Révolution française."
            ),
            "before": (
                "Le roi renvoie un ministre aimé du peuple et fait venir "
                "des soldats autour de Paris. Les Parisiens ont peur et "
                "se fâchent."
            ),
            "during": (
                "La foule va chercher des fusils, puis de la poudre pour "
                "tirer avec. Elle marche vers la Bastille, qui garde "
                "beaucoup de poudre à canon."
            ),
            "after": (
                "Le chef de la Bastille se rend. Les Parisiens libèrent "
                "les prisonniers et créent une nouvelle armée pour "
                "protéger la ville : la Garde nationale."
            ),
            "narrative": [
                "Le matin du 14 juillet 1789, une grande foule de Parisiens "
                "se rassemble devant la Bastille, une forteresse qui sert "
                "de prison. Ils ont déjà pris des fusils ailleurs dans la "
                "ville, mais il leur manque la poudre pour tirer.",
                "La Bastille est gardée par des soldats. Elle ne contient "
                "pourtant que sept prisonniers, mais pour les gens de "
                "Paris, elle représente le pouvoir du roi sur eux. Après "
                "des heures de discussion, des coups de feu partent.",
                "Des soldats rejoignent la foule avec des canons. Le "
                "gouverneur de la forteresse, à court de moyens, finit "
                "par se rendre. La foule entre, libère les prisonniers "
                "et récupère les munitions.",
            ],
            "why_it_matters": (
                "C'est la première fois que le peuple de Paris se soulève "
                "avec autant de force. Le roi a peur et doit reculer : "
                "c'est le vrai début de la Révolution française."
            ),
        },
        "college": {
            "summary": (
                "Le 14 juillet 1789, le peuple parisien s'empare de la "
                "Bastille, une forteresse-prison symbole du pouvoir "
                "absolu du roi. Cet événement marque le début de la "
                "Révolution française."
            ),
            "before": (
                "Depuis plusieurs mois, la crise financière et "
                "politique s'aggrave en France. Le renvoi du ministre "
                "populaire Necker, le 11 juillet, ainsi que le "
                "rassemblement de troupes royales autour de Paris, "
                "provoquent la colère et l'inquiétude des Parisiens, "
                "qui craignent un coup de force du roi contre "
                "l'Assemblée."
            ),
            "during": (
                "Après avoir pillé l'Hôtel des Invalides pour s'emparer "
                "de milliers de fusils, la foule se dirige vers la "
                "Bastille afin d'y récupérer la poudre à canon qui y "
                "est stockée. Les négociations avec le gouverneur "
                "échouent et des coups de feu éclatent des deux côtés."
            ),
            "after": (
                "Après plusieurs heures de combat, le gouverneur de "
                "Launay capitule. La foule libère les sept prisonniers "
                "et s'empare des munitions. Dans les jours qui suivent, "
                "une nouvelle force armée, la Garde nationale, est "
                "créée pour maintenir l'ordre à Paris, et Louis XVI est "
                "contraint de reculer."
            ),
            "narrative": [
                "Le 14 juillet 1789, une foule d'artisans et de "
                "bourgeois se rassemble devant la Bastille, à l'est de "
                "Paris. Ils viennent de s'emparer de milliers de fusils "
                "aux Invalides, mais il leur manque la poudre à canon, "
                "stockée dans la forteresse.",
                "Défendue par une petite garnison sous les ordres du "
                "gouverneur de Launay, la Bastille ne contient que sept "
                "prisonniers ce jour-là, mais elle symbolise l'arbitraire "
                "du pouvoir royal. Après des négociations qui échouent, "
                "des coups de feu éclatent.",
                "Des gardes françaises passées du côté du peuple "
                "apportent des canons et permettent de briser les "
                "chaînes du pont-levis. Face à cette force, de Launay "
                "capitule en fin d'après-midi : la foule libère les "
                "prisonniers et s'empare des munitions.",
            ],
            "why_it_matters": (
                "Modeste militairement, la prise de la Bastille est la "
                "première intervention violente et décisive du peuple "
                "parisien dans la Révolution. Elle force Louis XVI à "
                "reculer et à rappeler Necker."
            ),
        },
        "lycee": {
            "summary": (
                "Un événement majeur de la Révolution française où les "
                "insurgés parisiens s'emparent de la forteresse de la "
                "Bastille, symbole de l'absolutisme royal."
            ),
            "before": (
                "Les tensions politiques et sociales s'accumulent à "
                "Paris depuis le printemps 1789 : renvoi du ministre "
                "Necker le 11 juillet, disette persistante et "
                "concentration de régiments royaux autour de la "
                "capitale font craindre un coup de force contre "
                "l'Assemblée nationale naissante."
            ),
            "during": (
                "En quête d'armes et de poudre, le peuple parisien, "
                "déjà en possession de fusils pris aux Invalides, se "
                "dirige vers la forteresse-prison de la Bastille, "
                "symbole de l'absolutisme royal. Les négociations avec "
                "le gouverneur de Launay échouent et l'assaut est donné "
                "en fin de matinée."
            ),
            "after": (
                "Le gouverneur de Launay capitule en fin d'après-midi "
                "face à l'arrivée de canons apportés par des gardes "
                "françaises ralliées à la foule. Les prisonniers sont "
                "libérés, la Garde nationale est créée sous La Fayette, "
                "et le démantèlement de la forteresse commence dans la "
                "foulée."
            ),
            "narrative": [
                "Le 14 juillet 1789, au matin, une foule nombreuse "
                "d'artisans, de boutiquiers et de bourgeois se rassemble "
                "devant la forteresse de la Bastille, à l'est de Paris. "
                "Ils viennent de piller l'Hôtel des Invalides, "
                "s'emparant de milliers de fusils, mais il leur manque "
                "l'essentiel : la poudre à canon et les balles, "
                "stockées en masse dans l'arsenal de la prison.",
                "La Bastille, défendue par une petite garnison de "
                "soldats invalides et de gardes suisses sous le "
                "commandement du gouverneur Bernard-René de Launay, "
                "représente également le symbole de l'arbitraire royal, "
                "bien qu'elle ne contienne ce jour-là que sept "
                "prisonniers. Après des heures de négociations "
                "infructueuses, des coups de feu éclatent.",
                "Rejoints par des gardes françaises mutinées apportant "
                "des canons, les assaillants parviennent à briser les "
                "chaînes du pont-levis. Face à cette puissance de feu, "
                "le gouverneur de Launay capitule en fin d'après-midi. "
                "La foule investit les lieux, libère les prisonniers et "
                "s'empare des munitions.",
            ],
            "why_it_matters": (
                "Militairement modeste, la prise de la Bastille marque "
                "la première intervention violente et décisive du "
                "peuple parisien dans la Révolution et force Louis XVI "
                "à reculer, rappeler Necker et reconnaître la nouvelle "
                "municipalité de Paris."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Un événement majeur de la Révolution française où les "
                "insurgés parisiens s'emparent de la forteresse de la "
                "Bastille, symbole de l'absolutisme royal, dans un "
                "contexte de crise politique et de disette."
            ),
            "before": (
                "Tensions croissantes à Paris, renvoi de Necker le 11 "
                "juillet, concentration de régiments étrangers autour "
                "de la capitale : le climat insurrectionnel s'installe "
                "dès le 12 juillet, jour où l'annonce du renvoi se "
                "répand dans la ville."
            ),
            "during": (
                "Le peuple, déjà en possession de fusils pris aux "
                "Invalides, se dirige vers la forteresse-prison à la "
                "recherche de poudre, transformant une émeute pour des "
                "munitions en assaut symbolique contre l'absolutisme."
            ),
            "after": (
                "Capitulation du gouverneur de Launay, lynché par la "
                "foule malgré une reddition négociée ; création de la "
                "Garde nationale sous La Fayette ; début du "
                "démantèlement méthodique de la forteresse, dont les "
                "pierres seront vendues comme souvenirs."
            ),
            "narrative": [
                "Le 14 juillet 1789, au matin, une foule nombreuse "
                "d'artisans, de boutiquiers et de bourgeois se rassemble "
                "devant la forteresse de la Bastille, à l'est de Paris, "
                "dans un climat de disette et de peur d'un « complot "
                "aristocratique ». Ils viennent de piller l'Hôtel des "
                "Invalides, s'emparant de milliers de fusils, mais il "
                "leur manque l'essentiel : la poudre à canon et les "
                "balles, stockées en masse dans l'arsenal de la prison.",
                "La Bastille, défendue par une garnison réduite d'une "
                "centaine d'hommes — invalides et gardes suisses — sous "
                "le commandement du gouverneur Bernard-René de Launay, "
                "représente avant tout le symbole de l'arbitraire royal "
                "et des lettres de cachet, bien qu'elle ne contienne ce "
                "jour-là que sept prisonniers de droit commun. Après des "
                "heures de négociations infructueuses, des coups de feu "
                "éclatent, faisant une centaine de morts parmi les "
                "assaillants.",
                "Rejoints en début d'après-midi par des gardes "
                "françaises mutinées apportant des canons, les "
                "assaillants parviennent à briser les chaînes du "
                "pont-levis. Face à cette puissance de feu, et sans "
                "espoir de secours, le gouverneur de Launay capitule "
                "vers 17 heures. La foule investit les lieux, libère les "
                "sept prisonniers et s'empare des munitions ; de Launay "
                "sera massacré en chemin vers l'Hôtel de Ville malgré "
                "les termes de la reddition.",
            ],
            "why_it_matters": (
                "Militairement modeste — une garnison de moins de cent "
                "hommes face à une foule de plusieurs milliers — la "
                "prise de la Bastille marque la première intervention "
                "violente et décisive du « tiers état en armes » dans "
                "la Révolution et force Louis XVI à reculer dès le 15 "
                "juillet : il rappelle Necker, se rend à l'Assemblée et "
                "reconnaît la nouvelle municipalité insurrectionnelle "
                "de Paris, cédant pour la première fois du terrain "
                "politique à la rue."
            ),
        },
    },
    "assassinat-cesar": {
        "enfant": {
            "summary": (
                "Des sénateurs romains ont peur que Jules César devienne "
                "roi. Le 15 mars, ils le tuent avec des poignards, en "
                "plein Sénat."
            ),
            "before": (
                "César a pris tous les pouvoirs à Rome. Certains "
                "sénateurs pensent qu'il veut devenir roi, ce que les "
                "Romains détestent."
            ),
            "during": (
                "Un groupe de sénateurs entoure César et le frappe avec "
                "des poignards, plusieurs fois de suite, pendant une "
                "réunion du Sénat."
            ),
            "after": (
                "Sans César, c'est le désordre à Rome : une nouvelle "
                "guerre commence. C'est son fils adoptif, Octave, qui "
                "gagnera à la fin."
            ),
            "narrative": [
                "Le 15 mars de l'an 44 avant Jésus-Christ, Jules César "
                "se rend à une réunion du Sénat, à Rome.",
                "Un groupe de sénateurs, menés par deux hommes appelés "
                "Brutus et Cassius, s'approche de lui. Ils le frappent "
                "avec des poignards, plusieurs fois. César ne se défend "
                "pas.",
                "Les sénateurs pensaient sauver la République en tuant "
                "César. Mais c'est le contraire qui arrive : une longue "
                "guerre éclate, et Rome devient bientôt un empire.",
            ],
            "why_it_matters": (
                "En voulant empêcher César de devenir roi, ses tueurs "
                "ont en fait ouvert la porte à un empire romain encore "
                "plus puissant, dirigé par son fils adoptif Auguste."
            ),
        },
        "college": {
            "summary": (
                "Un groupe de sénateurs romains, craignant l'instauration "
                "d'une monarchie, assassine Jules César en plein Sénat, "
                "le jour des Ides de mars."
            ),
            "before": (
                "Vainqueur de la guerre civile contre son rival Pompée, "
                "César a été nommé dictateur à vie en février 44 av. "
                "J.-C. Il concentre entre ses mains des pouvoirs jugés "
                "excessifs par une partie du Sénat, qui redoute de le "
                "voir se proclamer roi et mettre fin à la République."
            ),
            "during": (
                "Un groupe de sénateurs, surnommés les « Libérateurs » "
                "et menés par Brutus et Cassius, profite d'une séance du "
                "Sénat pour l'entourer sous prétexte de lui présenter "
                "une pétition. Ils le poignardent alors à de multiples "
                "reprises, sans qu'il ne cherche vraiment à se "
                "défendre."
            ),
            "after": (
                "Loin d'apaiser la situation, l'assassinat plonge Rome "
                "dans le chaos : privés d'un plan de gouvernement, les "
                "conjurés perdent rapidement le contrôle des "
                "événements, et une nouvelle guerre civile éclate, "
                "remportée par le fils adoptif de César, Octave, futur "
                "empereur Auguste."
            ),
            "narrative": [
                "Le 15 mars 44 av. J.-C. — les Ides de mars — Jules "
                "César se rend à une séance du Sénat qui se tient "
                "exceptionnellement dans la curie du théâtre de Pompée.",
                "Une soixantaine de sénateurs, menés par Marcus Junius "
                "Brutus et Cassius Longinus, l'entourent sous prétexte "
                "de lui présenter une pétition, puis le poignardent à de "
                "nombreuses reprises.",
                "Les conjurés espéraient restaurer les pleins pouvoirs "
                "du Sénat en supprimant celui qu'ils considéraient comme "
                "un tyran en devenir. Son assassinat plonge au contraire "
                "Rome dans une nouvelle guerre civile.",
            ],
            "why_it_matters": (
                "Loin de sauver la République, l'assassinat de César "
                "précipite sa chute : la guerre civile qui suit se "
                "conclut par l'avènement d'Octave-Auguste et la "
                "naissance de l'Empire romain."
            ),
        },
        "lycee": {
            "summary": (
                "Un groupe de sénateurs romains, craignant l'instauration "
                "d'une monarchie, assassine Jules César en plein Sénat "
                "aux Ides de mars."
            ),
            "before": (
                "César, vainqueur de la guerre civile qui l'opposait à "
                "Pompée, a été nommé dictateur à vie en février 44 av. "
                "J.-C. Cette concentration de pouvoirs, ajoutée à des "
                "honneurs quasi royaux, inquiète une partie du Sénat, "
                "attachée à la tradition républicaine et hostile à "
                "toute idée de monarchie."
            ),
            "during": (
                "Réunis en un groupe d'une soixantaine de sénateurs "
                "surnommés les « Libérateurs » et menés par Marcus "
                "Junius Brutus et Cassius Longinus, les conjurés "
                "entourent César sous prétexte d'une pétition lors "
                "d'une séance tenue exceptionnellement dans la curie du "
                "théâtre de Pompée, puis le poignardent à de nombreuses "
                "reprises."
            ),
            "after": (
                "Convaincus que la seule suppression du « tyran » "
                "suffirait à restaurer la République, les conjurés "
                "n'avaient préparé aucun plan de gouvernement pour "
                "l'après-César. Le vide politique qu'ils laissent "
                "déclenche au contraire une nouvelle guerre civile, "
                "dont sortira vainqueur le fils adoptif de César, "
                "Octave, futur empereur Auguste."
            ),
            "narrative": [
                "Le 15 mars de l'an 44 av. J.-C. — les Ides de mars dans "
                "le calendrier romain —, Jules César se rend à une "
                "séance du Sénat qui se tient exceptionnellement dans la "
                "curie du théâtre de Pompée, le bâtiment habituel étant "
                "en rénovation.",
                "Un groupe d'une soixantaine de sénateurs, mené par "
                "Marcus Junius Brutus et Cassius Longinus, l'entoure "
                "sous prétexte de lui présenter une pétition. Ils le "
                "poignardent à de nombreuses reprises. César, selon la "
                "tradition, ne cherche pas à se défendre face à "
                "l'ampleur du complot.",
                "Les conjurés espéraient restaurer les pleins pouvoirs "
                "du Sénat en supprimant celui qu'ils considéraient comme "
                "un tyran en devenir. Au lieu de cela, son assassinat "
                "plonge Rome dans une nouvelle guerre civile entre les "
                "partisans de César et ses assassins.",
            ],
            "why_it_matters": (
                "Loin de sauver la République, l'assassinat de César "
                "précipite sa chute définitive : la guerre civile qui "
                "suit se conclut par l'avènement d'Octave-Auguste et la "
                "naissance de l'Empire romain en 27 av. J.-C."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Un groupe d'une soixantaine de sénateurs romains, "
                "craignant l'instauration d'une monarchie sous couvert "
                "de dictature perpétuelle, assassine Jules César en "
                "plein Sénat aux Ides de mars, précipitant la fin de la "
                "République qu'ils prétendaient sauver."
            ),
            "before": (
                "Vainqueur de la guerre civile contre Pompée, César "
                "cumule les pouvoirs — dictature perpétuelle obtenue en "
                "février 44, contrôle du Sénat, honneurs quasi royaux — "
                "et une partie de l'aristocratie sénatoriale, formée à "
                "la tradition anti-monarchique romaine, y voit la "
                "préparation d'une royauté déguisée."
            ),
            "during": (
                "Le groupe des « Libérateurs », mené par Brutus et "
                "Cassius et rassemblant d'anciens partisans de Pompée "
                "comme de César lui-même, l'entoure sous prétexte d'une "
                "pétition en faveur d'un sénateur exilé et le poignarde "
                "à vingt-trois reprises lors d'une séance tenue "
                "exceptionnellement dans la curie de Pompée."
            ),
            "after": (
                "Le vide politique laissé par César, sans plan de "
                "succession clair de la part des conjurés, déclenche une "
                "nouvelle série de guerres civiles opposant "
                "successivement les assassins, puis le second triumvirat, "
                "dont sortira vainqueur son petit-neveu et fils adoptif "
                "Octave, futur empereur Auguste."
            ),
            "narrative": [
                "Le 15 mars de l'an 44 av. J.-C. — les Ides de mars dans "
                "le calendrier romain —, Jules César se rend à une "
                "séance du Sénat qui se tient exceptionnellement dans la "
                "curie du théâtre de Pompée, le bâtiment habituel étant "
                "en rénovation ; il ignore, malgré plusieurs "
                "avertissements rapportés par la tradition, la "
                "conjuration qui se prépare.",
                "Un groupe d'une soixantaine de sénateurs, mené par "
                "Marcus Junius Brutus et Cassius Longinus, l'entoure "
                "sous prétexte de lui présenter une pétition en faveur "
                "d'un exilé. Ils le poignardent à vingt-trois reprises. "
                "César, selon la tradition rapportée par Suétone, "
                "cesserait de se défendre en reconnaissant Brutus parmi "
                "ses agresseurs.",
                "Les conjurés, persuadés que la seule suppression du "
                "« tyran » suffirait à restaurer les pleins pouvoirs du "
                "Sénat, n'avaient préparé aucun plan de gouvernement de "
                "l'après-César. Son assassinat plonge au contraire Rome "
                "dans plus d'une décennie de guerres civiles.",
            ],
            "why_it_matters": (
                "Loin de sauver la République, l'assassinat de César "
                "en précipite la chute définitive : privés d'un "
                "programme politique de rechange, les conjurés perdent "
                "rapidement le contrôle des événements, et la guerre "
                "civile qui suit — entre le second triumvirat et les "
                "assassins, puis entre triumvirs — se conclut par "
                "l'avènement d'Octave-Auguste en 27 av. J.-C. et la fin "
                "de cinq siècles de République romaine."
            ),
        },
    },
    "alunissage-apollo-11": {
        "enfant": {
            "summary": (
                "En 1969, Neil Armstrong devient le premier homme à "
                "marcher sur la Lune. Le monde entier regarde ce moment "
                "à la télévision."
            ),
            "before": (
                "Les États-Unis et l'URSS sont en compétition pour "
                "conquérir l'espace. Les Américains veulent être les "
                "premiers à envoyer des hommes sur la Lune."
            ),
            "during": (
                "Le module Eagle se pose sur la Lune. Armstrong puis "
                "Aldrin sortent marcher dessus, pendant que Collins "
                "attend dans le vaisseau, en orbite."
            ),
            "after": (
                "Les astronautes rapportent des cailloux de la Lune et "
                "reviennent en toute sécurité sur Terre. C'est un grand "
                "succès pour les États-Unis."
            ),
            "narrative": [
                "Le 16 juillet 1969, une immense fusée décolle avec à "
                "son bord trois astronautes : Neil Armstrong, Buzz "
                "Aldrin et Michael Collins.",
                "Le 20 juillet, leur petit vaisseau, appelé Eagle, se "
                "pose sur la Lune. Le lendemain, Neil Armstrong sort et "
                "pose le pied sur le sol lunaire : « C'est un petit pas "
                "pour l'homme, un bond de géant pour l'humanité. »",
                "Buzz Aldrin le rejoint. Ensemble, ils plantent un "
                "drapeau américain et ramassent des roches, avant de "
                "repartir vers la Terre.",
            ],
            "why_it_matters": (
                "C'est la première fois qu'un être humain marche sur un "
                "autre monde que la Terre. Cet exploit est resté dans "
                "l'histoire de l'humanité."
            ),
        },
        "college": {
            "summary": (
                "Neil Armstrong devient le premier être humain à marcher "
                "sur la Lune, un moment retransmis en direct devant des "
                "centaines de millions de téléspectateurs."
            ),
            "before": (
                "Depuis le lancement du satellite Spoutnik par l'URSS "
                "en 1957, les États-Unis sont engagés dans une course à "
                "l'espace acharnée avec les Soviétiques. Le président "
                "Kennedy fixe dès 1961 l'objectif d'envoyer un équipage "
                "sur la Lune avant la fin de la décennie, donnant "
                "naissance au programme Apollo."
            ),
            "during": (
                "Le 16 juillet 1969, la fusée Saturn V décolle du "
                "Centre spatial Kennedy avec Armstrong, Aldrin et "
                "Collins à son bord. Quatre jours plus tard, le module "
                "lunaire Eagle se pose sur la Mer de la Tranquillité ; "
                "Armstrong puis Aldrin sortent marcher à sa surface, "
                "tandis que Collins reste seul en orbite lunaire à bord "
                "du module de commande."
            ),
            "after": (
                "L'équipage rapporte des échantillons de roches "
                "lunaires et regagne la Terre sain et sauf après un "
                "amerrissage dans le Pacifique. La mission marque "
                "l'apogée du programme spatial américain et une "
                "victoire symbolique majeure dans la guerre froide."
            ),
            "narrative": [
                "Le 16 juillet 1969, la fusée Saturn V emporte Neil "
                "Armstrong, Buzz Aldrin et Michael Collins depuis le "
                "Centre spatial Kennedy. Le module lunaire Eagle se "
                "sépare ensuite du vaisseau principal pour descendre "
                "vers la Lune.",
                "Le 20 juillet, Armstrong pose l'Eagle sur la Mer de la "
                "Tranquillité, en évitant de justesse un champ de "
                "rochers. Le lendemain, il pose le pied sur le sol "
                "lunaire en déclarant : « C'est un petit pas pour "
                "l'homme, un bond de géant pour l'humanité. »",
                "Buzz Aldrin le rejoint peu après. Les deux astronautes "
                "plantent un drapeau américain, collectent des roches "
                "lunaires et repassent environ 21 heures sur place avant "
                "de redécoller.",
            ],
            "why_it_matters": (
                "L'alunissage d'Apollo 11 marque l'aboutissement de la "
                "course à l'espace entre les États-Unis et l'URSS et "
                "reste l'un des exploits techniques les plus marquants "
                "du XXe siècle."
            ),
        },
        "lycee": {
            "summary": (
                "Neil Armstrong devient le premier être humain à marcher "
                "sur la Lune, retransmis en direct devant des centaines "
                "de millions de téléspectateurs."
            ),
            "before": (
                "Depuis le lancement du satellite Spoutnik par l'URSS "
                "en 1957 puis le premier vol habité de Youri Gagarine "
                "en 1961, les États-Unis sont engagés dans une course à "
                "l'espace acharnée. Kennedy fixe dès 1961 l'objectif "
                "d'un alunissage humain avant la fin de la décennie, "
                "lançant le programme Apollo, qui mobilisera jusqu'à "
                "400 000 personnes."
            ),
            "during": (
                "Le 16 juillet 1969, la fusée Saturn V emporte "
                "Armstrong, Aldrin et Collins depuis le Centre spatial "
                "Kennedy. Le 20 juillet, le module lunaire Eagle se "
                "pose sur la Mer de la Tranquillité malgré des alertes "
                "informatiques et un terrain semé de rochers ; le "
                "lendemain, Armstrong puis Aldrin sortent marcher à la "
                "surface pendant que Collins reste seul en orbite "
                "lunaire."
            ),
            "after": (
                "L'équipage rapporte près de 22 kg d'échantillons "
                "lunaires et rentre sain et sauf sur Terre après un "
                "amerrissage dans le Pacifique. La mission marque "
                "l'aboutissement du programme Apollo et un tournant "
                "symbolique majeur de la guerre froide."
            ),
            "narrative": [
                "Le 16 juillet 1969, la fusée Saturn V emporte Neil "
                "Armstrong, Buzz Aldrin et Michael Collins depuis le "
                "Centre spatial Kennedy. Quatre jours plus tard, le "
                "module lunaire Eagle se sépare du module de commande et "
                "entame sa descente vers la surface lunaire.",
                "Le 20 juillet, Armstrong pose l'Eagle manuellement sur "
                "la Mer de la Tranquillité, évitant de justesse un champ "
                "de rochers, avec à peine quelques dizaines de secondes "
                "de carburant restant. Le lendemain, à 2h56 (heure de "
                "Paris) le 21 juillet, il pose le pied sur le sol "
                "lunaire.",
                "« C'est un petit pas pour l'homme, un bond de géant "
                "pour l'humanité », déclare-t-il. Buzz Aldrin le rejoint "
                "peu après. Les deux astronautes plantent un drapeau "
                "américain, collectent des roches lunaires et repartent "
                "après environ 21 heures passées sur place.",
            ],
            "why_it_matters": (
                "L'alunissage d'Apollo 11 marque l'aboutissement de la "
                "course à l'espace entre les États-Unis et l'URSS et "
                "reste l'un des exploits techniques et humains les plus "
                "marquants du XXe siècle."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Neil Armstrong devient le premier être humain à marcher "
                "sur la Lune, retransmis en direct devant environ 600 "
                "millions de téléspectateurs, aboutissement du "
                "programme Apollo lancé huit ans plus tôt par Kennedy."
            ),
            "before": (
                "En pleine course à l'espace avec l'URSS — qui a déjà "
                "envoyé le premier satellite (1957) et le premier homme "
                "(1961) en orbite — les États-Unis lancent le programme "
                "Apollo pour poser un équipage sur la Lune avant la fin "
                "de la décennie, objectif fixé par Kennedy dès 1961."
            ),
            "during": (
                "Le module lunaire Eagle se pose sur la Mer de la "
                "Tranquillité après qu'Armstrong a dû reprendre "
                "manuellement les commandes face à un terrain semé de "
                "blocs rocheux ; lui et Aldrin sortent marcher à la "
                "surface pendant environ deux heures et demie, tandis "
                "que Collins reste seul en orbite lunaire à bord du "
                "module de commande."
            ),
            "after": (
                "L'équipage rapporte 21,5 kg d'échantillons lunaires et "
                "rentre sain et sauf sur Terre après un amerrissage "
                "dans le Pacifique, marquant l'apogée du programme "
                "spatial américain et un tournant symbolique de la "
                "guerre froide."
            ),
            "narrative": [
                "Le 16 juillet 1969, la fusée Saturn V emporte Neil "
                "Armstrong, Buzz Aldrin et Michael Collins depuis le "
                "Centre spatial Kennedy, en Floride. Quatre jours plus "
                "tard, le module lunaire Eagle se sépare du module de "
                "commande Columbia et entame sa descente vers la surface "
                "lunaire, guidé par un ordinateur de bord dont la "
                "mémoire ne dépasse pas quelques dizaines de kilo-octets.",
                "Le 20 juillet, alertes d'ordinateur en cascade et "
                "terrain semé de rochers obligent Armstrong à reprendre "
                "les commandes manuellement pour poser l'Eagle sur la "
                "Mer de la Tranquillité, avec à peine 25 secondes de "
                "carburant restant selon les estimations. Le lendemain, "
                "à 2h56 (heure de Paris) le 21 juillet, il pose le "
                "premier pied humain sur un sol extraterrestre.",
                "« C'est un petit pas pour l'homme, un bond de géant "
                "pour l'humanité », déclare-t-il — une phrase dont la "
                "formulation exacte (« a man » ou « man ») reste "
                "débattue faute d'enregistrement parfaitement clair. "
                "Buzz Aldrin le rejoint peu après ; les deux astronautes "
                "plantent un drapeau américain, installent des "
                "instruments scientifiques et collectent des roches "
                "avant de repartir après environ 21 heures passées à la "
                "surface."
            ],
            "why_it_matters": (
                "L'alunissage d'Apollo 11 marque l'aboutissement d'une "
                "course à l'espace de plus d'une décennie entre les "
                "États-Unis et l'URSS, mobilisant à son apogée près de "
                "4 % du budget fédéral américain, et reste l'un des "
                "exploits techniques et humains les plus marquants du "
                "XXe siècle, autant pour sa prouesse scientifique que "
                "pour sa portée symbolique en pleine guerre froide."
            ),
        },
    },
    "chute-de-constantinople": {
        "enfant": {
            "summary": (
                "En 1453, l'armée du sultan Mehmed II prend la ville de "
                "Constantinople après un long siège. C'est la fin d'un "
                "très vieil empire, l'Empire byzantin."
            ),
            "before": (
                "L'Empire byzantin est devenu tout petit. Il ne reste "
                "plus que la ville de Constantinople, entourée par "
                "l'armée du sultan Mehmed II."
            ),
            "during": (
                "Pendant des semaines, les soldats ottomans tirent au "
                "canon sur les murs de la ville. Puis ils réussissent à "
                "entrer dans la ville."
            ),
            "after": (
                "La ville devient la nouvelle capitale de l'Empire "
                "ottoman et change de nom : elle s'appelle maintenant "
                "Istanbul."
            ),
            "narrative": [
                "Constantinople est protégée par de très grands murs "
                "depuis des siècles. Mais en 1453, le sultan Mehmed II "
                "arrive avec une armée énorme et des canons géants faits "
                "spécialement pour casser ces murs.",
                "Le siège commence début avril. Pendant presque deux "
                "mois, la ville résiste, même si les canons tirent sans "
                "arrêt.",
                "Le 29 mai 1453, tôt le matin, les soldats ottomans "
                "réussissent enfin à entrer dans la ville. C'est la fin "
                "de l'Empire byzantin, qui existait depuis plus de mille "
                "ans.",
            ],
            "why_it_matters": (
                "C'est la fin d'un empire très ancien. Beaucoup "
                "d'historiens disent que c'est aussi la fin du Moyen "
                "Âge en Europe."
            ),
        },
        "college": {
            "summary": (
                "Après un siège de près de deux mois, les troupes "
                "ottomanes de Mehmed II s'emparent de Constantinople, "
                "mettant fin à onze siècles d'Empire byzantin."
            ),
            "before": (
                "Réduit depuis des décennies à sa seule capitale et à "
                "quelques territoires isolés, l'Empire byzantin ne peut "
                "compter sur aucun secours occidental significatif "
                "malgré des appels répétés. Il se retrouve encerclé "
                "par l'immense armée du jeune sultan ottoman Mehmed II, "
                "déterminé à s'emparer de la ville."
            ),
            "during": (
                "Le siège débute début avril 1453. Pendant près de deux "
                "mois, la ville résiste aux bombardements d'une "
                "artillerie inédite, dont un canon géant capable de "
                "tirer d'énormes boulets. Mehmed II fait même "
                "transporter une partie de sa flotte par voie terrestre "
                "pour contourner les défenses maritimes de la ville."
            ),
            "after": (
                "Le 29 mai, un assaut général finit par percer les "
                "murailles. L'empereur Constantin XI meurt dans les "
                "combats et la ville tombe. Rebaptisée Istanbul, elle "
                "devient la nouvelle capitale de l'Empire ottoman, "
                "marquant pour beaucoup d'historiens la fin du Moyen "
                "Âge en Europe."
            ),
            "narrative": [
                "Depuis des siècles, Constantinople résiste aux sièges "
                "grâce à ses puissantes murailles théodosiennes. Mais en "
                "1453, le sultan ottoman Mehmed II rassemble une armée "
                "immense et des canons géants conçus pour percer ces "
                "remparts.",
                "Le siège débute début avril. Pendant près de deux mois, "
                "la ville, défendue par l'empereur Constantin XI, "
                "résiste malgré des bombardements incessants.",
                "Le 29 mai 1453 à l'aube, un assaut général finit par "
                "percer les défenses. Constantin XI meurt dans les "
                "combats. La ville est prise, marquant la fin de "
                "l'Empire byzantin.",
            ],
            "why_it_matters": (
                "La chute de Constantinople met fin à l'Empire byzantin "
                "et marque, pour de nombreux historiens, la transition "
                "symbolique entre le Moyen Âge et la Renaissance en "
                "Europe."
            ),
        },
        "lycee": {
            "summary": (
                "Après un siège de près de deux mois, les troupes "
                "ottomanes de Mehmed II s'emparent de Constantinople, "
                "mettant fin à onze siècles d'Empire byzantin."
            ),
            "before": (
                "Réduit depuis des décennies à sa seule capitale, "
                "l'Empire byzantin, diplomatiquement isolé malgré des "
                "appels répétés à l'Occident, se retrouve encerclé par "
                "l'armée immense du jeune sultan ottoman Mehmed II, "
                "déterminé à réussir là où ses prédécesseurs avaient "
                "échoué."
            ),
            "during": (
                "Le siège débute début avril 1453. Pendant près de deux "
                "mois, la ville, défendue par une garnison réduite sous "
                "l'empereur Constantin XI, résiste à des bombardements "
                "incessants menés par une artillerie inédite, dont la "
                "célèbre bombarde d'Orban. Mehmed II fait transporter "
                "une partie de sa flotte par voie terrestre pour "
                "contourner la chaîne bloquant l'accès à la Corne d'Or."
            ),
            "after": (
                "Le 29 mai 1453 à l'aube, un assaut général finit par "
                "percer les défenses théodosiennes, vieilles de mille "
                "ans. Constantin XI meurt dans les combats. Rebaptisée "
                "Istanbul, la ville devient la nouvelle capitale de "
                "l'Empire ottoman, marquant pour de nombreux historiens "
                "la transition symbolique entre Moyen Âge et "
                "Renaissance."
            ),
            "narrative": [
                "Depuis des siècles, Constantinople résiste aux sièges "
                "grâce à ses puissantes murailles théodosiennes. Mais en "
                "1453, le jeune sultan ottoman Mehmed II rassemble une "
                "armée immense et une artillerie de canons géants conçus "
                "spécialement pour percer ces remparts.",
                "Le siège débute début avril. Pendant près de deux mois, "
                "la ville, défendue par une garnison réduite sous "
                "l'empereur Constantin XI, résiste malgré des "
                "bombardements incessants. Mehmed II fait même "
                "transporter une partie de sa flotte par voie terrestre "
                "pour contourner une chaîne bloquant l'accès à la Corne "
                "d'Or.",
                "Le 29 mai 1453 à l'aube, un assaut général finit par "
                "percer les défenses. Constantin XI meurt dans les "
                "combats. La ville est prise, marquant la fin de "
                "l'Empire byzantin, héritier direct de l'Empire romain "
                "d'Orient depuis plus de onze siècles.",
            ],
            "why_it_matters": (
                "La chute de Constantinople met fin à l'Empire byzantin "
                "et marque, pour de nombreux historiens, la transition "
                "symbolique entre le Moyen Âge et la Renaissance en "
                "Europe, notamment par l'exil de savants byzantins qui "
                "contribuera à la diffusion des textes antiques en "
                "Occident."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Après un siège de près de deux mois, les troupes "
                "ottomanes du jeune sultan Mehmed II s'emparent de "
                "Constantinople le 29 mai 1453, mettant fin à onze "
                "siècles d'Empire byzantin et provoquant un choc dans "
                "toute la chrétienté."
            ),
            "before": (
                "Réduit depuis des décennies à sa seule capitale et à "
                "quelques territoires épars, l'Empire byzantin, "
                "diplomatiquement isolé malgré des appels répétés à "
                "l'Occident, ne peut opposer qu'une garnison d'environ "
                "7 000 hommes à l'armée ottomane de Mehmed II, forte de "
                "60 000 à 80 000 combattants."
            ),
            "during": (
                "Après des semaines de siège et de bombardements par une "
                "artillerie inédite — dont le canon géant conçu par "
                "l'ingénieur hongrois Orban —, les troupes ottomanes "
                "finissent par percer les murailles théodosiennes, "
                "vieilles de mille ans, lors de l'assaut général du "
                "29 mai."
            ),
            "after": (
                "Constantinople devient la nouvelle capitale de "
                "l'Empire ottoman sous le nom d'Istanbul ; sa chute, "
                "largement relayée en Occident, est traditionnellement "
                "retenue par l'historiographie comme la fin "
                "conventionnelle du Moyen Âge en Europe."
            ),
            "narrative": [
                "Depuis des siècles, Constantinople résiste aux sièges "
                "grâce à ses puissantes murailles théodosiennes, "
                "triples remparts achevés au Ve siècle. Mais en 1453, le "
                "jeune sultan ottoman Mehmed II, âgé de 21 ans et "
                "déterminé à réussir là où ses prédécesseurs avaient "
                "échoué, rassemble une armée immense et une artillerie "
                "de canons géants conçus spécialement pour percer ces "
                "remparts, notamment la bombarde d'Orban, capable de "
                "tirer des boulets de plus de 500 kg.",
                "Le siège débute début avril 1453. Pendant près de deux "
                "mois, la ville, défendue par une garnison réduite "
                "d'environ 7 000 hommes — dont des mercenaires génois "
                "menés par Giovanni Giustiniani — sous l'autorité de "
                "l'empereur Constantin XI, résiste malgré des "
                "bombardements incessants. Mehmed II fait même "
                "transporter une partie de sa flotte par voie terrestre, "
                "sur des rondins graissés, pour contourner la chaîne "
                "bloquant l'accès à la Corne d'Or.",
                "Le 29 mai 1453 à l'aube, après un assaut d'ampleur "
                "inédite mené en plusieurs vagues successives, les "
                "défenses finissent par céder — une porte secondaire "
                "restée mal fermée, la Kerkoporta, aurait facilité "
                "l'irruption des troupes ottomanes. Constantin XI meurt "
                "dans les combats, son corps ne sera jamais formellement "
                "identifié. La ville est prise et pillée pendant trois "
                "jours, selon la coutume des sièges de l'époque, "
                "marquant la fin de l'Empire byzantin, héritier direct "
                "de l'Empire romain d'Orient depuis plus de onze siècles.",
            ],
            "why_it_matters": (
                "La chute de Constantinople met fin au dernier vestige "
                "de l'Empire romain et marque, pour une large part de "
                "l'historiographie occidentale, la transition "
                "symbolique entre le Moyen Âge et la Renaissance en "
                "Europe — notamment par l'exil de nombreux savants "
                "byzantins vers l'Italie, qui contribuera à la "
                "redécouverte des textes antiques grecs et alimentera "
                "l'humanisme renaissant, tout en provoquant en Europe "
                "occidentale une onde de choc qui relancera la "
                "recherche de routes maritimes vers l'Asie, contournant "
                "un Orient désormais sous contrôle ottoman."
            ),
        },
    },
    "decouverte-tombe-toutankhamon": {
        "enfant": {
            "summary": (
                "En 1922, l'archéologue Howard Carter trouve la tombe "
                "d'un jeune pharaon égyptien, Toutânkhamon. C'est une "
                "découverte incroyable : personne ne l'avait volée !"
            ),
            "before": (
                "Depuis longtemps, Howard Carter cherche dans le désert "
                "égyptien la tombe d'un pharaon dont on ne savait presque "
                "rien : Toutânkhamon."
            ),
            "during": (
                "Les ouvriers de Carter trouvent un escalier caché sous "
                "le sable. Il mène à une porte fermée, avec des marques "
                "montrant qu'elle n'a jamais été ouverte."
            ),
            "after": (
                "Pendant presque dix ans, Carter et son équipe sortent "
                "tous les trésors de la tombe, comme le fameux masque en "
                "or du pharaon."
            ),
            "narrative": [
                "Depuis 1907, l'archéologue Howard Carter fouille le "
                "désert égyptien pour trouver la tombe d'un jeune pharaon "
                "appelé Toutânkhamon.",
                "Le 4 novembre 1922, ses ouvriers trouvent enfin une "
                "marche cachée dans la roche. Elle mène à un escalier, "
                "puis à une porte fermée avec des marques intactes.",
                "Le 26 novembre, Carter fait un petit trou dans la porte "
                "et regarde avec une bougie. Il découvre un trésor "
                "immense, resté caché depuis plus de 3000 ans, avec le "
                "célèbre masque en or du pharaon.",
            ],
            "why_it_matters": (
                "C'est l'une des découvertes les plus incroyables de "
                "l'archéologie. Grâce à elle, on connaît beaucoup mieux "
                "la vie en Égypte il y a très longtemps."
            ),
        },
        "college": {
            "summary": (
                "L'archéologue britannique Howard Carter découvre "
                "l'entrée de la tombe intacte du pharaon Toutânkhamon, "
                "l'une des plus grandes découvertes archéologiques du "
                "XXe siècle."
            ),
            "before": (
                "Depuis 1907, l'archéologue britannique Howard Carter "
                "fouille méthodiquement la Vallée des Rois pour le "
                "compte de son riche mécène, Lord Carnarvon, à la "
                "recherche de la tombe d'un pharaon mineur du Nouvel "
                "Empire dont l'existence n'était encore attestée que "
                "par de rares indices."
            ),
            "during": (
                "Le 4 novembre 1922, alors que le financement de "
                "l'expédition touche à sa fin, les ouvriers de Carter "
                "découvrent une marche taillée dans la roche. Elle mène "
                "à un escalier puis à une porte scellée, dont les "
                "cachets intacts laissent penser que la tombe n'a "
                "jamais été pillée."
            ),
            "after": (
                "Le 26 novembre, Carter perce un trou dans la porte "
                "intérieure et découvre un trésor funéraire "
                "exceptionnel, quasi intact depuis plus de 3 000 ans. "
                "Le dégagement et l'inventaire de plus de 5 000 objets, "
                "dont le célèbre masque en or, dureront près de dix ans "
                "et fascineront le monde entier."
            ),
            "narrative": [
                "Depuis 1907, l'archéologue britannique Howard Carter "
                "fouille la Vallée des Rois pour le compte de son "
                "mécène, Lord Carnarvon, à la recherche de la tombe du "
                "pharaon Toutânkhamon, un souverain mineur dont "
                "l'emplacement du tombeau restait inconnu.",
                "Le 4 novembre 1922, alors que le financement touche à "
                "sa fin, les ouvriers de Carter découvrent une marche "
                "taillée dans la roche, menant à un escalier puis à une "
                "porte scellée portant des cachets encore intacts.",
                "Le 26 novembre, Carter perce un petit trou dans la "
                "porte intérieure et, à la lueur d'une bougie, aperçoit "
                "« des choses merveilleuses » : la tombe, quasi inviolée "
                "depuis plus de 3 000 ans, regorge d'un trésor funéraire "
                "exceptionnel.",
            ],
            "why_it_matters": (
                "La découverte de la tombe de Toutânkhamon reste l'une "
                "des plus importantes de l'archéologie moderne : sa "
                "richesse quasi intacte a beaucoup enrichi la "
                "connaissance de l'Égypte ancienne."
            ),
        },
        "lycee": {
            "summary": (
                "L'archéologue britannique Howard Carter découvre "
                "l'entrée de la tombe intacte du pharaon Toutânkhamon, "
                "l'une des plus grandes découvertes archéologiques du "
                "XXe siècle."
            ),
            "before": (
                "Depuis 1907, l'archéologue britannique Howard Carter "
                "fouille systématiquement la Vallée des Rois pour le "
                "compte de son mécène Lord Carnarvon, à la recherche de "
                "la tombe du pharaon Toutânkhamon, un souverain mineur "
                "mort jeune dont l'emplacement restait inconnu, alors "
                "que la plupart des égyptologues jugeaient déjà la "
                "vallée entièrement explorée."
            ),
            "during": (
                "Le 4 novembre 1922, alors que Carnarvon envisage "
                "d'arrêter le financement de la campagne, les ouvriers "
                "de Carter découvrent une marche taillée dans la roche "
                "menant à un escalier, puis à une porte scellée "
                "portant des cachets encore intacts de la nécropole "
                "royale — signe qu'elle n'a jamais été profanée."
            ),
            "after": (
                "Le 26 novembre 1922, en présence de Lord Carnarvon, "
                "Carter perce un trou dans la porte intérieure et "
                "découvre à la lueur d'une bougie un trésor funéraire "
                "quasi intact depuis plus de 3 000 ans. Le dégagement "
                "méthodique de plus de 5 000 objets, dont le célèbre "
                "masque en or massif, mobilisera toute une équipe "
                "pendant près de dix ans."
            ),
            "narrative": [
                "Depuis 1907, l'archéologue britannique Howard Carter "
                "fouille la Vallée des Rois pour le compte de son "
                "mécène, Lord Carnarvon, à la recherche de la tombe du "
                "pharaon Toutânkhamon, un souverain mineur mort jeune "
                "dont l'emplacement du tombeau restait inconnu.",
                "Le 4 novembre 1922, après des années de recherches "
                "infructueuses et alors que le financement touchait à sa "
                "fin, les ouvriers de Carter découvrent une marche "
                "taillée dans la roche. Elle mène à un escalier, puis à "
                "une porte scellée portant des cachets encore intacts.",
                "Le 26 novembre, Carter perce un petit trou dans la "
                "porte intérieure et, à la lueur d'une bougie, aperçoit "
                "« des choses merveilleuses » : la tombe, quasiment "
                "inviolée depuis plus de 3 000 ans, regorge d'un trésor "
                "funéraire exceptionnel, dont le célèbre masque funéraire "
                "en or du pharaon.",
            ],
            "why_it_matters": (
                "La découverte de la tombe de Toutânkhamon reste l'une "
                "des plus importantes de l'archéologie moderne : sa "
                "richesse quasi intacte a considérablement enrichi la "
                "connaissance de l'Égypte ancienne et déclenché un "
                "engouement mondial pour l'égyptologie."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Après quinze ans de fouilles infructueuses, "
                "l'archéologue britannique Howard Carter découvre "
                "l'entrée de la tombe quasi intacte du pharaon "
                "Toutânkhamon, l'une des plus grandes découvertes "
                "archéologiques du XXe siècle et un jalon fondateur de "
                "l'égyptomanie moderne."
            ),
            "before": (
                "Après des années de fouilles infructueuses financées "
                "par Lord Carnarvon, qui envisage de mettre fin à son "
                "soutien financier, Howard Carter cherche dans la "
                "Vallée des Rois la tombe d'un pharaon mineur du Nouvel "
                "Empire (XVIIIe dynastie) dont l'existence n'était "
                "attestée que par de rares mentions indirectes."
            ),
            "during": (
                "Les ouvriers de Carter dégagent un escalier taillé "
                "dans la roche, menant à une porte scellée portant les "
                "sceaux intacts de la nécropole royale — signe rarissime "
                "qu'aucun pillard n'avait pénétré les lieux depuis "
                "l'Antiquité."
            ),
            "after": (
                "Le dégagement méthodique et l'inventaire du trésor "
                "funéraire, comprenant plus de 5 000 objets dont le "
                "célèbre masque funéraire en or massif, dureront près "
                "de dix ans, mobiliseront toute une équipe "
                "internationale et captiveront le monde entier, "
                "alimentés par la légende d'une « malédiction du "
                "pharaon » née des morts successives de certains "
                "membres de l'expédition."
            ),
            "narrative": [
                "Depuis 1907, l'archéologue britannique Howard Carter "
                "fouille systématiquement la Vallée des Rois pour le "
                "compte de son mécène, Lord Carnarvon, à la recherche de "
                "la tombe du pharaon Toutânkhamon (règne v. 1336-1327 "
                "av. J.-C.), un souverain mineur mort à environ 19 ans "
                "dont l'emplacement du tombeau restait inconnu — la "
                "plupart des égyptologues de l'époque, dont Theodore "
                "Davis, estimaient déjà la Vallée entièrement fouillée.",
                "Le 4 novembre 1922, alors que Carnarvon envisage "
                "d'arrêter le financement de la campagne, les ouvriers "
                "de Carter découvrent une marche taillée dans la roche, "
                "en contrebas de la tombe de Ramsès VI. Elle mène à un "
                "escalier de seize marches, puis à une porte scellée "
                "portant des cachets encore intacts de la nécropole "
                "royale.",
                "Le 26 novembre 1922, en présence de Lord Carnarvon, "
                "Carter perce un petit trou dans la porte intérieure et, "
                "à la lueur d'une bougie, aperçoit « des choses "
                "merveilleuses », selon le mot resté célèbre qu'il "
                "aurait alors prononcé : la tombe, quasiment inviolée "
                "depuis plus de 3 000 ans (seules deux intrusions "
                "mineures et rapidement scellées avaient eu lieu dans "
                "l'Antiquité), regorge d'un trésor funéraire "
                "exceptionnel, dont le célèbre masque funéraire en or "
                "massif du pharaon, aujourd'hui conservé au Musée "
                "égyptien du Caire.",
            ],
            "why_it_matters": (
                "La découverte de la tombe de Toutânkhamon reste l'une "
                "des plus importantes de l'archéologie moderne, non "
                "pour l'importance historique du pharaon lui-même — un "
                "souverain mineur d'une dynastie éphémère — mais parce "
                "que l'intégrité quasi totale de son mobilier funéraire "
                "a offert un instantané sans équivalent du faste "
                "matériel et religieux de l'Égypte du Nouvel Empire, "
                "renouvelant considérablement les connaissances "
                "scientifiques tout en déclenchant, par sa couverture "
                "médiatique mondiale, un engouement populaire durable "
                "pour l'égyptologie qui perdure aujourd'hui."
            ),
        },
    },
    "prise-des-tuileries": {
        "enfant": {
            "summary": (
                "Le 10 août 1792, les Parisiens attaquent le palais où "
                "vit le roi Louis XVI. C'est presque la fin du règne "
                "des rois en France."
            ),
            "before": (
                "La France est en guerre contre l'Autriche et la "
                "Prusse. Les gens ne font plus confiance au roi, qui "
                "avait essayé de fuir le pays."
            ),
            "during": (
                "Une foule marche vers le palais des Tuileries. Louis "
                "XVI part se cacher près de l'Assemblée, laissant ses "
                "gardes suisses se battre seuls."
            ),
            "after": (
                "Le roi perd son pouvoir. Quelques semaines plus tard, "
                "la France devient une République, un pays sans roi."
            ),
            "narrative": [
                "Le matin du 10 août 1792, des soldats venus de "
                "plusieurs villes de France marchent vers le palais des "
                "Tuileries, à Paris, où vit le roi.",
                "Louis XVI a peur et quitte le palais pour se réfugier "
                "près de l'Assemblée. Ses gardes suisses restent seuls "
                "pour défendre le palais et se battent contre la foule.",
                "Le palais est pris. Le roi perd son pouvoir : "
                "l'Assemblée décide de le suspendre. Peu après, la "
                "France devient une République.",
            ],
            "why_it_matters": (
                "Ce jour-là marque la fin du pouvoir des rois en "
                "France depuis mille ans. Peu après, la République est "
                "proclamée."
            ),
        },
        "college": {
            "summary": (
                "L'insurrection parisienne prend d'assaut le palais des "
                "Tuileries, met fin à la monarchie de fait et précipite "
                "la chute de Louis XVI."
            ),
            "before": (
                "La France est en guerre contre l'Autriche et la "
                "Prusse, et la confiance dans le roi s'est effondrée "
                "après sa tentative de fuite manquée à Varennes en "
                "1791."
            ),
            "during": (
                "Des bataillons venus de plusieurs villes de France "
                "marchent avec les Parisiens vers les Tuileries. Louis "
                "XVI se réfugie auprès de l'Assemblée, laissant les "
                "Gardes suisses défendre seuls le palais."
            ),
            "after": (
                "L'Assemblée suspend le roi de ses fonctions. Six "
                "semaines plus tard, une nouvelle assemblée, la "
                "Convention, proclame la première République "
                "française."
            ),
            "narrative": [
                "Au matin du 10 août 1792, des bataillons de gardes "
                "nationaux venus notamment de Marseille et de Bretagne "
                "convergent avec les Parisiens vers le palais des "
                "Tuileries, résidence du roi depuis 1789.",
                "Craignant pour sa vie, Louis XVI quitte le palais avec "
                "sa famille pour se réfugier auprès de l'Assemblée. Les "
                "Gardes suisses restés sur place affrontent seuls "
                "l'assaut : les combats font près d'un millier de "
                "morts.",
                "Le palais est pillé et pris par les insurgés. "
                "L'Assemblée vote la suspension du roi et convoque une "
                "Convention nationale élue au suffrage universel "
                "masculin.",
            ],
            "why_it_matters": (
                "Le 10 août 1792 met fin, dans les faits, à un "
                "millénaire de monarchie en France et ouvre la voie à "
                "la proclamation de la République quelques semaines "
                "plus tard."
            ),
        },
        "lycee": {
            "summary": (
                "L'insurrection parisienne prend d'assaut le palais des "
                "Tuileries, met fin à la monarchie de fait et précipite "
                "la chute de Louis XVI."
            ),
            "before": (
                "La patrie est déclarée en danger face à l'invasion "
                "prussienne et autrichienne annoncée par le manifeste "
                "de Brunswick. La confiance dans la loyauté du roi "
                "s'effondre après sa fuite manquée à Varennes en 1791."
            ),
            "during": (
                "Des sections parisiennes et des fédérés venus de "
                "province marchent sur les Tuileries. Louis XVI se "
                "réfugie auprès de l'Assemblée législative, laissant "
                "les Gardes suisses défendre seuls le palais, sans "
                "ordre clair de se retirer."
            ),
            "after": (
                "L'Assemblée suspend le roi de ses fonctions. Six "
                "semaines plus tard, la Convention nouvellement élue "
                "proclame la première République française, le 21 "
                "septembre 1792."
            ),
            "narrative": [
                "Au matin du 10 août 1792, des bataillons de gardes "
                "nationaux fédérés, venus notamment de Marseille et de "
                "Bretagne, convergent avec les sections révolutionnaires "
                "parisiennes vers le palais des Tuileries, résidence du "
                "roi depuis son retour forcé de Versailles en 1789.",
                "Craignant pour sa vie, Louis XVI quitte le palais avec "
                "sa famille pour se placer sous la protection de "
                "l'Assemblée législative toute proche. Les quelque neuf "
                "cents Gardes suisses restés sur place, sans ordre "
                "clair de se retirer, affrontent seuls l'assaut : les "
                "combats font près d'un millier de morts, pour "
                "l'essentiel des gardes suisses.",
                "Le palais est pillé, les insurgés s'emparent des "
                "lieux. Face au fait accompli, l'Assemblée législative "
                "vote la suspension du roi de ses fonctions et convoque "
                "une Convention nationale élue au suffrage universel "
                "masculin.",
            ],
            "why_it_matters": (
                "Le 10 août 1792 met fin, dans les faits, à un "
                "millénaire de monarchie en France. Il ouvre la voie à "
                "la proclamation de la République le 21 septembre 1792 "
                "et, quelques mois plus tard, au procès et à "
                "l'exécution de Louis XVI."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "L'insurrection parisienne, appuyée par des fédérés "
                "venus de province, prend d'assaut le palais des "
                "Tuileries le 10 août 1792, met fin à la monarchie de "
                "fait et précipite la chute puis l'exécution de Louis "
                "XVI."
            ),
            "before": (
                "La patrie est déclarée en danger le 11 juillet 1792 "
                "face à l'invasion prussienne et autrichienne, "
                "aggravée par le manifeste de Brunswick menaçant Paris "
                "de représailles en cas d'atteinte à la famille royale "
                "— un texte qui produit l'effet inverse de celui "
                "recherché. La confiance dans la loyauté du roi, déjà "
                "ébranlée par sa fuite manquée à Varennes en juin 1791, "
                "s'effondre définitivement."
            ),
            "during": (
                "Des sections parisiennes radicalisées et des "
                "bataillons de fédérés, notamment marseillais, "
                "marchent sur les Tuileries dans la nuit du 9 au 10 "
                "août. Louis XVI, sur les conseils de son entourage, se "
                "réfugie auprès de l'Assemblée législative, laissant "
                "environ neuf cents Gardes suisses défendre seuls le "
                "palais sans ordre clair de se retirer."
            ),
            "after": (
                "L'Assemblée législative, dépassée par les événements, "
                "vote la suspension du roi de ses fonctions et le fait "
                "interner au Temple. Six semaines plus tard, la "
                "Convention nouvellement élue au suffrage universel "
                "masculin proclame la première République française, "
                "le 21 septembre 1792."
            ),
            "narrative": [
                "Au matin du 10 août 1792, des bataillons de gardes "
                "nationaux fédérés, venus notamment de Marseille et de "
                "Bretagne, convergent avec les sections révolutionnaires "
                "parisiennes vers le palais des Tuileries, résidence du "
                "roi depuis son retour forcé de Versailles en octobre "
                "1789.",
                "Craignant pour sa vie, Louis XVI quitte le palais avec "
                "sa famille pour se placer sous la protection de "
                "l'Assemblée législative toute proche. Les quelque neuf "
                "cents Gardes suisses restés sur place, sans ordre "
                "clair de se retirer transmis à temps, affrontent seuls "
                "l'assaut : les combats font près d'un millier de "
                "morts, pour l'essentiel des gardes suisses massacrés "
                "après leur reddition.",
                "Le palais est pillé, les insurgés s'emparent des "
                "lieux. Face au fait accompli, l'Assemblée législative, "
                "désormais sous la pression de la rue, vote la "
                "suspension du roi de ses fonctions et convoque au "
                "suffrage universel masculin une Convention nationale "
                "chargée de doter le pays d'une nouvelle constitution.",
            ],
            "why_it_matters": (
                "Le 10 août 1792 met fin, dans les faits, à un "
                "millénaire de monarchie en France et marque un "
                "tournant vers une phase plus radicale de la "
                "Révolution. Il ouvre la voie à la proclamation de la "
                "République le 21 septembre 1792 et, quelques mois "
                "plus tard, au procès et à l'exécution de Louis XVI en "
                "janvier 1793."
            ),
        },
    },
    "chute-mur-berlin": {
        "enfant": {
            "summary": (
                "Le 9 novembre 1989, le mur qui séparait Berlin en deux "
                "depuis presque 30 ans tombe. Les gens fêtent ça toute "
                "la nuit."
            ),
            "before": (
                "Depuis des mois, des gens manifestent pacifiquement en "
                "Allemagne de l'Est pour demander plus de liberté."
            ),
            "during": (
                "Un porte-parole annonce, un peu par erreur, que les "
                "gens peuvent voyager librement tout de suite. Des "
                "milliers de Berlinois se précipitent vers le mur."
            ),
            "after": (
                "Les gardes laissent passer la foule. Les gens montent "
                "sur le mur et commencent à le casser à coups de "
                "marteau."
            ),
            "narrative": [
                "Le soir du 9 novembre 1989, un porte-parole du "
                "gouvernement est-allemand annonce, un peu par erreur, "
                "que les habitants peuvent désormais voyager librement, "
                "« immédiatement ».",
                "En quelques heures, des milliers de Berlinois de l'Est "
                "se pressent devant le mur. Les gardes, surpris, finissent "
                "par les laisser passer.",
                "Des foules de Berlinois de l'Est et de l'Ouest se "
                "retrouvent enfin. Certains montent sur le mur, d'autres "
                "commencent déjà à le casser.",
            ],
            "why_it_matters": (
                "La chute du mur marque la fin de la séparation de "
                "l'Allemagne en deux pays, et bientôt la fin de la "
                "guerre froide en Europe."
            ),
        },
        "college": {
            "summary": (
                "L'annonce inattendue de l'ouverture des frontières "
                "est-allemandes provoque l'effondrement du mur de "
                "Berlin, symbole de la guerre froide depuis 1961."
            ),
            "before": (
                "Des mois de manifestations pacifiques en Allemagne de "
                "l'Est, et l'assouplissement progressif du bloc "
                "soviétique sous Gorbatchev, fragilisent un régime "
                "est-allemand de plus en plus isolé."
            ),
            "during": (
                "Une annonce gouvernementale mal formulée laisse croire "
                "à une ouverture immédiate des frontières. Des milliers "
                "de Berlinois affluent vers les points de passage, "
                "submergeant des gardes sans instructions claires."
            ),
            "after": (
                "Le mur est ouvert dans la nuit, puis peu à peu "
                "démantelé par la foule à coups de marteau, ouvrant la "
                "voie à la réunification allemande en octobre 1990."
            ),
            "narrative": [
                "Le 9 novembre 1989 au soir, le porte-parole du "
                "gouvernement est-allemand Günter Schabowski annonce en "
                "conférence de presse, de façon confuse, que les "
                "citoyens de RDA peuvent désormais voyager librement "
                "« immédiatement, sans délai ».",
                "En quelques heures, des milliers de Berlinois de l'Est "
                "se pressent aux points de passage du mur. Débordés et "
                "sans instructions claires, les gardes-frontières "
                "finissent par ouvrir les barrières.",
                "Des foules de Berlinois de l'Est et de l'Ouest se "
                "retrouvent, certains montent sur le mur, d'autres "
                "commencent à le fissurer à coups de marteau. Les "
                "scènes de liesse sont retransmises dans le monde "
                "entier.",
            ],
            "why_it_matters": (
                "La chute du mur de Berlin marque symboliquement la fin "
                "de la guerre froide en Europe, et ouvre la voie à la "
                "réunification allemande moins d'un an plus tard."
            ),
        },
        "lycee": {
            "summary": (
                "L'annonce inattendue de l'ouverture des frontières "
                "est-allemandes provoque l'effondrement du mur de "
                "Berlin, symbole de la guerre froide depuis 1961."
            ),
            "before": (
                "Des mois de manifestations pacifiques en Allemagne de "
                "l'Est (mouvement « Wir sind das Volk »), l'ouverture "
                "de la frontière hongroise à l'été 1989 et "
                "l'assouplissement du bloc soviétique sous Gorbatchev "
                "fragilisent gravement le régime est-allemand."
            ),
            "during": (
                "Une annonce gouvernementale mal formulée par Günter "
                "Schabowski laisse croire à une ouverture immédiate des "
                "frontières. Des milliers de Berlinois affluent vers "
                "les points de passage, notamment Bornholmer Straße, "
                "submergeant des gardes sans instructions claires."
            ),
            "after": (
                "Le mur est ouvert vers 23h30 puis peu à peu démantelé "
                "par la foule à coups de marteau et de burin, ouvrant "
                "la voie à la réunification allemande le 3 octobre "
                "1990."
            ),
            "narrative": [
                "Le 9 novembre 1989 au soir, le porte-parole du "
                "gouvernement est-allemand Günter Schabowski annonce en "
                "conférence de presse, de façon confuse, que les "
                "citoyens de RDA peuvent désormais voyager librement "
                "« immédiatement, sans délai ».",
                "En quelques heures, des milliers de Berlinois de l'Est "
                "se pressent aux points de passage du mur, notamment à "
                "Bornholmer Straße. Débordés et sans instructions "
                "claires, les gardes-frontières finissent par ouvrir "
                "les barrières vers 23h30.",
                "Des foules de Berlinois de l'Est et de l'Ouest se "
                "retrouvent, certains montent sur le mur, d'autres "
                "commencent à le fissurer à coups de marteau et de "
                "burin. Les scènes de liesse sont retransmises dans le "
                "monde entier en direct.",
            ],
            "why_it_matters": (
                "La chute du mur de Berlin marque symboliquement la fin "
                "de la guerre froide et du rideau de fer en Europe, et "
                "ouvre la voie à la réunification allemande moins d'un "
                "an plus tard."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "L'annonce mal formulée, en conférence de presse, de "
                "l'ouverture des frontières est-allemandes provoque en "
                "quelques heures l'effondrement du mur de Berlin, "
                "symbole du rideau de fer depuis 1961, dans un des "
                "moments les plus filmés de l'histoire contemporaine."
            ),
            "before": (
                "Des mois de manifestations pacifiques du lundi à "
                "Leipzig, l'ouverture de la frontière hongroise à l'été "
                "1989 qui permet à des milliers d'Est-Allemands de fuir "
                "vers l'Ouest via l'Autriche, et l'assouplissement du "
                "bloc soviétique sous l'impulsion de la Glasnost de "
                "Gorbatchev fragilisent gravement un régime "
                "est-allemand de plus en plus isolé, y compris de son "
                "propre parrain soviétique."
            ),
            "during": (
                "Lors d'une conférence de presse retransmise en "
                "direct, le porte-parole du Politburo Günter "
                "Schabowski, mal informé des modalités exactes d'une "
                "nouvelle réglementation, répond à une question d'un "
                "journaliste italien que la liberté de circulation "
                "entre en vigueur « immédiatement, sans délai ». Des "
                "milliers de Berlinois affluent en quelques heures vers "
                "les points de passage, notamment Bornholmer Straße, "
                "submergeant des gardes-frontières sans instructions "
                "claires de leur hiérarchie."
            ),
            "after": (
                "Face à l'ampleur de la foule et à l'absence d'ordre de "
                "tirer, le commandant du poste de Bornholmer Straße, "
                "Harald Jäger, prend seul la décision d'ouvrir les "
                "barrières vers 23h30. Le mur est ensuite peu à peu "
                "démantelé par des « pics du mur » (Mauerspechte), "
                "ouvrant la voie à la réunification allemande, "
                "officialisée le 3 octobre 1990."
            ),
            "narrative": [
                "Le 9 novembre 1989 au soir, le porte-parole du "
                "gouvernement est-allemand Günter Schabowski annonce en "
                "conférence de presse, de façon confuse et sans avoir "
                "pleinement pris connaissance du texte qu'on venait de "
                "lui remettre, que les citoyens de RDA peuvent "
                "désormais voyager librement « immédiatement, sans "
                "délai ».",
                "En quelques heures, des milliers de Berlinois de l'Est "
                "se pressent aux points de passage du mur, notamment à "
                "Bornholmer Straße. Débordés et sans instructions "
                "claires de Berlin-Est, les gardes-frontières, menés "
                "sur place par le lieutenant-colonel Harald Jäger, "
                "finissent par ouvrir les barrières vers 23h30, faute "
                "d'alternative pour contenir la foule sans recourir à "
                "la force.",
                "Des foules de Berlinois de l'Est et de l'Ouest se "
                "retrouvent, certains montent sur le mur, d'autres "
                "commencent à le fissurer à coups de marteau et de "
                "burin — les « Mauerspechte », ou « pics du mur ». Les "
                "scènes de liesse sont retransmises dans le monde "
                "entier en direct, faisant de cette nuit l'un des "
                "événements les plus filmés du XXe siècle.",
            ],
            "why_it_matters": (
                "La chute du mur de Berlin marque symboliquement la fin "
                "de la guerre froide et du rideau de fer en Europe. "
                "Loin d'être planifiée par les autorités est-allemandes "
                "— qui envisageaient un assouplissement progressif et "
                "encadré des voyages, non une ouverture immédiate — "
                "elle illustre la manière dont un malentendu "
                "bureaucratique, amplifié par la couverture médiatique "
                "en direct, peut précipiter l'effondrement d'un régime, "
                "et ouvre la voie à la réunification allemande moins "
                "d'un an plus tard."
            ),
        },
    },
    "debarquement-normandie": {
        "enfant": {
            "summary": (
                "Le 6 juin 1944, des soldats américains, britanniques "
                "et canadiens débarquent sur les plages de Normandie "
                "pour libérer la France de l'armée allemande."
            ),
            "before": (
                "Depuis des années, les Alliés préparent en secret ce "
                "débarquement, en essayant de tromper les Allemands sur "
                "le lieu exact."
            ),
            "during": (
                "Des dizaines de milliers de soldats débarquent sur "
                "cinq plages, avec l'aide de parachutistes largués la "
                "nuit d'avant."
            ),
            "after": (
                "Malgré de lourdes pertes, les Alliés réussissent à "
                "s'installer en Normandie. C'est le début de la "
                "libération de la France."
            ),
            "narrative": [
                "Dans la nuit du 5 au 6 juin 1944, des milliers de "
                "parachutistes sont largués en Normandie avant "
                "l'attaque principale.",
                "Au matin, des milliers de bateaux amènent des soldats "
                "sur cinq plages. Les combats sont très durs, surtout "
                "à Omaha Beach.",
                "Le soir, les Alliés ont réussi à s'installer sur les "
                "plages. C'est le début de la libération de la France, "
                "occupée par l'Allemagne depuis 1940.",
            ],
            "why_it_matters": (
                "Ce débarquement est un moment clé de la guerre : il "
                "permet aux Alliés de libérer la France puis d'aider à "
                "vaincre l'Allemagne nazie."
            ),
        },
        "college": {
            "summary": (
                "Les forces alliées débarquent sur les côtes "
                "normandes lors de l'opération Overlord, la plus "
                "grande invasion maritime de l'histoire."
            ),
            "before": (
                "Après des années de préparation et de désinformation "
                "pour tromper l'état-major allemand sur le lieu du "
                "débarquement, les Alliés rassemblent une force "
                "amphibie sans précédent."
            ),
            "during": (
                "Près de 156 000 soldats alliés débarquent sur cinq "
                "plages codées Utah, Omaha, Gold, Juno et Sword, "
                "appuyés par des parachutistes largués dans la nuit."
            ),
            "after": (
                "Malgré de lourdes pertes, notamment à Omaha Beach, les "
                "Alliés établissent une tête de pont qui permettra la "
                "libération de la France dans les mois suivants."
            ),
            "narrative": [
                "Dans la nuit du 5 au 6 juin 1944, des milliers de "
                "parachutistes américains et britanniques sont largués "
                "derrière les lignes allemandes en Normandie.",
                "À l'aube, une armada de plus de 5 000 navires appuie "
                "le débarquement de troupes sur cinq plages. Les "
                "combats sont particulièrement meurtriers à Omaha "
                "Beach.",
                "Malgré la résistance allemande, les têtes de pont sont "
                "solidement établies en fin de journée, ouvrant un "
                "second front décisif à l'ouest.",
            ],
            "why_it_matters": (
                "Le débarquement de Normandie constitue un tournant "
                "majeur de la Seconde Guerre mondiale, menant à la "
                "libération de Paris en août 1944."
            ),
        },
        "lycee": {
            "summary": (
                "Les forces alliées débarquent sur les côtes normandes "
                "lors de l'opération Overlord, la plus grande invasion "
                "maritime de l'histoire, ouvrant un second front "
                "décisif contre l'Allemagne nazie."
            ),
            "before": (
                "Après des années de préparation et une vaste campagne "
                "de désinformation (opération Fortitude) pour tromper "
                "l'état-major allemand sur le lieu du débarquement, les "
                "Alliés rassemblent une force amphibie sans précédent."
            ),
            "during": (
                "Près de 156 000 soldats alliés débarquent sur cinq "
                "plages codées Utah, Omaha, Gold, Juno et Sword, "
                "appuyés par des parachutistes largués dans la nuit et "
                "une flotte de plus de 5 000 navires."
            ),
            "after": (
                "Malgré de lourdes pertes, notamment à Omaha Beach, les "
                "Alliés établissent une tête de pont solide qui "
                "permettra la libération de Paris dès le mois d'août "
                "1944."
            ),
            "narrative": [
                "Dans la nuit du 5 au 6 juin 1944, des milliers de "
                "parachutistes américains et britanniques sont largués "
                "derrière les lignes allemandes en Normandie, chargés "
                "de sécuriser des points stratégiques avant l'assaut "
                "principal.",
                "À l'aube, une armada de plus de 5 000 navires appuie "
                "le débarquement de troupes américaines, britanniques, "
                "canadiennes et de la France libre sur cinq plages. Les "
                "combats sont particulièrement meurtriers à Omaha "
                "Beach, où les défenses allemandes infligent de lourdes "
                "pertes.",
                "Malgré la résistance allemande, les têtes de pont sont "
                "solidement établies en fin de journée. Cette opération "
                "Overlord ouvre un second front décisif à l'ouest, "
                "tandis que l'Armée rouge repousse déjà les forces "
                "allemandes à l'est.",
            ],
            "why_it_matters": (
                "Le débarquement de Normandie constitue un tournant "
                "majeur de la Seconde Guerre mondiale en Europe de "
                "l'Ouest, menant à la libération de Paris en août 1944 "
                "et à la capitulation allemande moins d'un an plus "
                "tard."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Les forces alliées débarquent sur les côtes normandes "
                "lors de l'opération Overlord, la plus grande invasion "
                "maritime de l'histoire, ouvrant un second front "
                "décisif à l'ouest alors que l'Armée rouge progresse "
                "déjà à l'est."
            ),
            "before": (
                "Après des années de préparation logistique colossale "
                "et une vaste campagne de désinformation (opération "
                "Fortitude, faisant croire à un débarquement dans le "
                "Pas-de-Calais), les Alliés rassemblent une force "
                "amphibie sans précédent, retardée d'un jour par les "
                "conditions météorologiques."
            ),
            "during": (
                "Près de 156 000 soldats alliés débarquent le 6 juin "
                "sur cinq plages codées Utah, Omaha, Gold, Juno et "
                "Sword, appuyés par plus de 23 000 parachutistes "
                "largués dans la nuit et une flotte de plus de 5 000 "
                "navires — la plus grande armada jamais réunie."
            ),
            "after": (
                "Malgré de très lourdes pertes, notamment à Omaha "
                "Beach où les défenses allemandes tiennent presque "
                "l'assaut en échec, les Alliés établissent une tête de "
                "pont solide qui permettra, après la percée d'Avranches "
                "en juillet, la libération de Paris dès le 25 août "
                "1944."
            ),
            "narrative": [
                "Dans la nuit du 5 au 6 juin 1944, après un report "
                "d'un jour dû à la météo, des milliers de "
                "parachutistes américains et britanniques sont largués "
                "derrière les lignes allemandes en Normandie, chargés "
                "de sécuriser des points stratégiques avant l'assaut "
                "principal.",
                "À l'aube, une armada de plus de 5 000 navires appuie "
                "le débarquement de troupes américaines, britanniques, "
                "canadiennes et de la France libre sur cinq plages. Les "
                "combats sont particulièrement meurtriers à Omaha "
                "Beach, où les défenses allemandes du mur de l'Atlantique "
                "infligent de très lourdes pertes aux premières vagues.",
                "Malgré la résistance allemande, les têtes de pont sont "
                "solidement établies en fin de journée, au prix "
                "d'environ 10 000 pertes alliées. Cette opération "
                "Overlord ouvre un second front décisif à l'ouest, "
                "tandis que l'Armée rouge repousse déjà les forces "
                "allemandes à l'est, prenant le Reich en étau.",
            ],
            "why_it_matters": (
                "Le débarquement de Normandie constitue le tournant "
                "logistique et militaire majeur de la Seconde Guerre "
                "mondiale en Europe de l'Ouest : il force l'Allemagne "
                "nazie à combattre simultanément sur deux fronts "
                "majeurs, menant à la libération de Paris en août 1944 "
                "puis à la capitulation allemande moins d'un an plus "
                "tard, en mai 1945."
            ),
        },
    },
    "armistice-1918": {
        "enfant": {
            "summary": (
                "Le 11 novembre 1918, la guerre entre la France et "
                "l'Allemagne s'arrête enfin, après plus de quatre ans "
                "de combats."
            ),
            "before": (
                "L'Allemagne est épuisée et perd ses alliés les uns "
                "après les autres. Elle doit accepter d'arrêter la "
                "guerre."
            ),
            "during": (
                "Des représentants allemands signent l'arrêt des "
                "combats dans un wagon de train, en France, tôt le "
                "matin."
            ),
            "after": (
                "Les combats s'arrêtent à 11 heures. Cette date devient "
                "un jour de commémoration important en France."
            ),
            "narrative": [
                "À l'automne 1918, l'Allemagne, épuisée par la guerre, "
                "doit demander l'arrêt des combats.",
                "Dans la nuit, des représentants allemands rencontrent "
                "le maréchal Foch dans un wagon de train, en forêt de "
                "Compiègne, pour signer l'armistice.",
                "L'armistice est signé tôt le matin et les combats "
                "s'arrêtent à 11 heures précises, après plus de quatre "
                "ans d'une guerre terrible.",
            ],
            "why_it_matters": (
                "Cette date marque la fin de la Première Guerre "
                "mondiale. Chaque année, le 11 novembre, la France se "
                "souvient de cet événement."
            ),
        },
        "college": {
            "summary": (
                "La signature de l'armistice dans un wagon-restaurant "
                "en forêt de Compiègne met fin aux combats de la "
                "Première Guerre mondiale."
            ),
            "before": (
                "Épuisée, l'Allemagne voit ses alliés austro-hongrois "
                "et ottomans capituler les uns après les autres et fait "
                "face à des troubles révolutionnaires internes."
            ),
            "during": (
                "Une délégation allemande signe l'armistice avec les "
                "Alliés dans le wagon du maréchal Foch, à Rethondes, "
                "tôt le matin du 11 novembre."
            ),
            "after": (
                "Les combats cessent à 11h, heure symbolique du "
                "« onzième jour du onzième mois à la onzième heure ». "
                "Le traité de paix définitif sera signé à Versailles en "
                "1919."
            ),
            "narrative": [
                "À l'automne 1918, l'Allemagne, épuisée et privée du "
                "soutien de ses alliés, doit se résoudre à demander un "
                "armistice face à l'avancée alliée sur le front "
                "occidental.",
                "Dans la nuit du 10 au 11 novembre, une délégation "
                "allemande négocie les conditions de cessation des "
                "hostilités avec le maréchal Ferdinand Foch, dans un "
                "wagon-restaurant en forêt de Compiègne.",
                "L'armistice est signé à 5h15 du matin et entre en "
                "vigueur à 11 heures précises, mettant fin à plus de "
                "quatre années d'une guerre qui a fait environ 10 "
                "millions de morts militaires.",
            ],
            "why_it_matters": (
                "L'armistice du 11 novembre 1918 met fin à la Première "
                "Guerre mondiale et devient une date de commémoration "
                "nationale dans de nombreux pays."
            ),
        },
        "lycee": {
            "summary": (
                "La signature de l'armistice dans un wagon-restaurant "
                "en forêt de Compiègne met fin aux combats de la "
                "Première Guerre mondiale."
            ),
            "before": (
                "Épuisée, l'Allemagne voit ses alliés austro-hongrois "
                "et ottomans capituler les uns après les autres à "
                "l'automne 1918, tandis que des troubles révolutionnaires "
                "éclatent à l'intérieur du pays, notamment la mutinerie "
                "de la flotte à Kiel."
            ),
            "during": (
                "Une délégation allemande, conduite par le politicien "
                "Matthias Erzberger, signe l'armistice avec les Alliés "
                "dans le wagon du maréchal Foch, à Rethondes, tôt le "
                "matin du 11 novembre."
            ),
            "after": (
                "Les combats cessent à 11h, heure symbolique du "
                "« onzième jour du onzième mois à la onzième heure ». "
                "Le traité de paix définitif, qui redessinera la carte "
                "de l'Europe, sera signé à Versailles en juin 1919."
            ),
            "narrative": [
                "À l'automne 1918, l'Allemagne, épuisée et privée du "
                "soutien de ses alliés austro-hongrois et ottomans, "
                "doit se résoudre à demander un armistice face à "
                "l'avancée alliée sur le front occidental.",
                "Dans la nuit du 10 au 11 novembre, une délégation "
                "allemande négocie les conditions de cessation des "
                "hostilités avec le maréchal Ferdinand Foch, dans un "
                "wagon-restaurant aménagé en salle de réunion, en forêt "
                "de Compiègne.",
                "L'armistice est signé à 5h15 du matin et entre en "
                "vigueur à 11 heures précises. Sur tout le front, les "
                "combats cessent progressivement, mettant fin à plus de "
                "quatre années d'une guerre qui a fait environ 10 "
                "millions de morts militaires.",
            ],
            "why_it_matters": (
                "L'armistice du 11 novembre 1918 met fin à la Première "
                "Guerre mondiale et devient une date de commémoration "
                "nationale dans de nombreux pays. Le traité de "
                "Versailles qui suivra en 1919 redessinera la carte de "
                "l'Europe."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "La signature de l'armistice dans un wagon-restaurant "
                "en forêt de Compiègne, à 5h15 du matin, met fin aux "
                "combats de la Première Guerre mondiale après plus de "
                "quatre ans et environ dix millions de morts "
                "militaires."
            ),
            "before": (
                "Épuisée par le blocus naval britannique et privée du "
                "soutien de ses alliés austro-hongrois et ottomans, qui "
                "capitulent successivement à l'automne 1918, l'Allemagne "
                "fait face à des troubles révolutionnaires internes, "
                "déclenchés par la mutinerie de la flotte de guerre à "
                "Kiel début novembre."
            ),
            "during": (
                "Une délégation civile allemande, conduite par le "
                "politicien centriste Matthias Erzberger — un choix "
                "délibéré de l'état-major pour ne pas endosser la "
                "défaite militairement —, négocie et signe l'armistice "
                "avec les Alliés dans le wagon du maréchal Foch, à "
                "Rethondes, tôt le matin du 11 novembre."
            ),
            "after": (
                "Les combats cessent à 11h, heure symbolique du "
                "« onzième jour du onzième mois à la onzième heure ». "
                "Le traité de paix définitif, signé à Versailles en "
                "juin 1919 et imposant à l'Allemagne de lourdes "
                "réparations, redessinera profondément la carte de "
                "l'Europe et alimentera durablement le ressentiment "
                "allemand."
            ),
            "narrative": [
                "À l'automne 1918, l'Allemagne, épuisée par le blocus "
                "naval britannique et privée du soutien de ses alliés "
                "austro-hongrois et ottomans, doit se résoudre à "
                "demander un armistice face à l'avancée alliée sur le "
                "front occidental et à l'effondrement du moral à "
                "l'arrière.",
                "Dans la nuit du 10 au 11 novembre, une délégation "
                "allemande conduite par Matthias Erzberger négocie les "
                "conditions de cessation des hostilités avec le "
                "maréchal Ferdinand Foch, dans un wagon-restaurant "
                "aménagé en salle de réunion, en forêt de Compiègne — "
                "un lieu choisi par Foch pour son isolement et sa "
                "discrétion.",
                "L'armistice est signé à 5h15 du matin et entre en "
                "vigueur à 11 heures précises. Sur tout le front, les "
                "combats cessent progressivement — non sans un dernier "
                "bilan macabre, certains commandants ayant continué "
                "les offensives jusqu'à la dernière minute — mettant "
                "fin à plus de quatre années d'une guerre qui a fait "
                "environ 10 millions de morts militaires et autant de "
                "victimes civiles.",
            ],
            "why_it_matters": (
                "L'armistice du 11 novembre 1918 met fin à la Première "
                "Guerre mondiale et devient une date de commémoration "
                "nationale dans de nombreux pays. Le traité de "
                "Versailles qui suivra en 1919 redessinera la carte de "
                "l'Europe et imposera à l'Allemagne des conditions dont "
                "la dureté nourrira, selon de nombreux historiens, la "
                "montée des ressentiments qui contribuera au "
                "déclenchement de la Seconde Guerre mondiale deux "
                "décennies plus tard."
            ),
        },
    },
}


QUIZ_BY_LEVEL = {
    "bastille-importance": {
        "enfant": {
            "prompt": "Pourquoi les gens de Paris attaquent-ils la Bastille ?",
            "options": [
                "Parce que c'est une prison-forteresse, symbole du pouvoir du roi",
                "Parce que c'est un magasin de bonbons",
                "Parce que c'est l'école du roi",
                "Parce que c'est une ferme abandonnée",
            ],
            "correct_index": 0,
            "fun_fact": (
                "La Bastille ne contenait que sept prisonniers ce jour-là, "
                "mais elle représentait le pouvoir du roi sur le peuple."
            ),
        },
        "college": {
            "prompt": "Que cherchait la foule en se dirigeant vers la Bastille ?",
            "options": [
                "De la poudre à canon, après avoir déjà pris des fusils",
                "De l'or caché par le roi",
                "Des vivres pour la famine",
                "Des documents secrets du gouvernement",
            ],
            "correct_index": 0,
            "fun_fact": (
                "La prise de la Bastille le 14 juillet 1789 est considérée "
                "comme le point de départ de la Révolution française."
            ),
        },
        "lycee": {
            "prompt": (
                "Pourquoi la Bastille était-elle importante, malgré "
                "seulement sept prisonniers présents le 14 juillet 1789 ?"
            ),
            "options": [
                "Elle représentait le symbole de l'arbitraire du pouvoir royal",
                "C'était le principal arsenal militaire du royaume",
                "C'était la résidence d'été de Louis XVI",
                "C'était le siège du Parlement de Paris",
            ],
            "correct_index": 0,
            "fun_fact": (
                "Bien qu'elle ne contenait que sept prisonniers, la "
                "Bastille représentait l'arbitraire du pouvoir absolu du "
                "roi, notamment à travers les lettres de cachet."
            ),
        },
        "etudiant_adulte": {
            "prompt": (
                "Quelle conséquence politique immédiate, le 15 juillet "
                "1789, force Louis XVI à accepter après la prise de la "
                "Bastille ?"
            ),
            "options": [
                "Il rappelle Necker et reconnaît la nouvelle municipalité insurrectionnelle de Paris",
                "Il dissout immédiatement l'Assemblée nationale constituante",
                "Il fait fusiller le gouverneur de Launay pour trahison",
                "Il quitte Versailles pour l'Autriche dès le lendemain",
            ],
            "correct_index": 0,
            "fun_fact": (
                "Militairement modeste, la prise de la Bastille marque "
                "la première intervention violente et décisive du peuple "
                "parisien dans la Révolution."
            ),
        },
    },
    "cesar-assassinat": {
        "enfant": {
            "prompt": "Qui a tué Jules César ?",
            "options": [
                "Un groupe de sénateurs romains",
                "Une armée ennemie venue d'ailleurs",
                "Son propre fils",
                "Des pirates",
            ],
            "correct_index": 0,
            "fun_fact": (
                "César est tué le 15 mars (les Ides de mars) 44 av. J.-C., "
                "par un groupe de sénateurs qui avaient peur qu'il devienne roi."
            ),
        },
        "college": {
            "prompt": "En quelle année Jules César a-t-il été assassiné ?",
            "options": ["44 av. J.-C.", "27 av. J.-C.", "476", "753 av. J.-C."],
            "correct_index": 0,
            "fun_fact": (
                "César est poignardé le 15 mars (les Ides de mars) 44 av. J.-C., "
                "par un groupe de sénateurs menés par Brutus et Cassius."
            ),
        },
        "lycee": {
            "prompt": "Quel événement l'assassinat de César déclenche-t-il, contrairement à l'objectif visé par les conjurés ?",
            "options": [
                "Une nouvelle guerre civile menant à la naissance de l'Empire",
                "Le retour immédiat et pacifique de la République",
                "L'invasion de Rome par les Gaulois",
                "La restauration de la royauté étrusque",
            ],
            "correct_index": 0,
            "fun_fact": (
                "Loin de sauver la République, l'assassinat de César "
                "précipite sa chute : la guerre civile qui suit aboutit "
                "à l'avènement d'Octave-Auguste."
            ),
        },
        "etudiant_adulte": {
            "prompt": (
                "Pourquoi les conjurés, malgré la réussite de leur complot, "
                "perdent-ils rapidement le contrôle des événements après "
                "les Ides de mars ?"
            ),
            "options": [
                "Ils n'avaient préparé aucun plan de gouvernement de l'après-César",
                "Ils avaient épargné tous les proches de César par erreur",
                "Le Sénat les avait immédiatement exilés",
                "Octave avait déjà pris le pouvoir avant l'assassinat",
            ],
            "correct_index": 0,
            "fun_fact": (
                "Persuadés que la seule suppression du « tyran » "
                "suffirait à restaurer les pleins pouvoirs du Sénat, "
                "les conjurés n'avaient préparé aucun plan de "
                "gouvernement de l'après-César."
            ),
        },
    },
    "apollo-11-lune": {
        "enfant": {
            "prompt": "Qui a été le premier homme à marcher sur la Lune ?",
            "options": ["Neil Armstrong", "Buzz Aldrin", "Youri Gagarine", "Michael Collins"],
            "correct_index": 0,
            "fun_fact": (
                "Le 21 juillet 1969, Neil Armstrong pose le pied sur la "
                "Lune et dit : « C'est un petit pas pour l'homme, un "
                "bond de géant pour l'humanité. »"
            ),
        },
        "college": {
            "prompt": "Quel astronaute est resté en orbite lunaire pendant qu'Armstrong et Aldrin marchaient sur la Lune ?",
            "options": ["Michael Collins", "Buzz Aldrin", "John Glenn", "Youri Gagarine"],
            "correct_index": 0,
            "fun_fact": (
                "Michael Collins est resté seul à bord du module de "
                "commande, en orbite autour de la Lune, pendant "
                "qu'Armstrong et Aldrin marchaient à la surface."
            ),
        },
        "lycee": {
            "prompt": "Où le module lunaire Eagle se pose-t-il le 20 juillet 1969 ?",
            "options": [
                "Sur la Mer de la Tranquillité",
                "Sur le cratère Copernic",
                "Sur le pôle Sud lunaire",
                "Sur la face cachée de la Lune",
            ],
            "correct_index": 0,
            "fun_fact": (
                "Armstrong pose l'Eagle manuellement sur la Mer de la "
                "Tranquillité, évitant de justesse un champ de rochers, "
                "avec à peine quelques dizaines de secondes de carburant "
                "restant."
            ),
        },
        "etudiant_adulte": {
            "prompt": (
                "Pourquoi Armstrong doit-il reprendre les commandes "
                "manuellement lors de la descente de l'Eagle vers la "
                "surface lunaire ?"
            ),
            "options": [
                "Des alertes d'ordinateur en cascade et un terrain semé de rochers",
                "Une panne totale de communication avec Houston",
                "Une collision avec un débris en orbite lunaire",
                "Le refus de Buzz Aldrin de continuer la descente",
            ],
            "correct_index": 0,
            "fun_fact": (
                "Face à des alertes d'ordinateur en cascade et un "
                "terrain semé de blocs rocheux, Armstrong pose l'Eagle "
                "avec à peine 25 secondes de carburant restant selon les "
                "estimations."
            ),
        },
    },
    "constantinople-consequence": {
        "enfant": {
            "prompt": "Quel empire prend fin en 1453 ?",
            "options": ["L'Empire byzantin", "L'Empire romain d'Occident", "L'Empire perse", "L'Empire chinois"],
            "correct_index": 0,
            "fun_fact": (
                "La chute de Constantinople met fin à un empire qui "
                "existait depuis plus de mille ans."
            ),
        },
        "college": {
            "prompt": "Quel nouveau nom prend Constantinople après sa conquête par les Ottomans ?",
            "options": ["Istanbul", "Byzance", "Ankara", "Andrinople"],
            "correct_index": 0,
            "fun_fact": (
                "Constantinople devient la capitale de l'Empire ottoman "
                "sous le nom d'Istanbul."
            ),
        },
        "lycee": {
            "prompt": "Quel empire prend fin avec la chute de Constantinople en 1453 ?",
            "options": ["L'Empire byzantin", "L'Empire romain d'Occident", "L'Empire perse", "L'Empire carolingien"],
            "correct_index": 0,
            "fun_fact": (
                "La chute de Constantinople met fin à l'Empire byzantin, "
                "héritier direct de l'Empire romain d'Orient depuis plus "
                "de onze siècles."
            ),
        },
        "etudiant_adulte": {
            "prompt": (
                "Quel effet indirect la chute de Constantinople a-t-elle "
                "eu sur la Renaissance européenne, selon une partie de "
                "l'historiographie ?"
            ),
            "options": [
                "L'exil de savants byzantins vers l'Italie a favorisé la redécouverte de textes antiques",
                "Elle a directement financé les artistes florentins",
                "Elle a mis fin au commerce entre l'Europe et l'Asie",
                "Elle a provoqué l'unification politique de l'Italie",
            ],
            "correct_index": 0,
            "fun_fact": (
                "L'exil de nombreux savants byzantins vers l'Italie après "
                "1453 a contribué à la redécouverte des textes antiques "
                "grecs et alimenté l'humanisme renaissant."
            ),
        },
    },
    "toutankhamon-decouvreur": {
        "enfant": {
            "prompt": "Qui a découvert la tombe de Toutânkhamon en 1922 ?",
            "options": ["Howard Carter", "Jean-François Champollion", "Indiana Jones", "Lord Carnarvon"],
            "correct_index": 0,
            "fun_fact": (
                "Howard Carter cherchait cette tombe depuis très "
                "longtemps avant de la trouver enfin en 1922."
            ),
        },
        "college": {
            "prompt": "Qui finançait les fouilles d'Howard Carter en Égypte ?",
            "options": ["Lord Carnarvon", "Le gouvernement égyptien", "Le British Museum", "Champollion"],
            "correct_index": 0,
            "fun_fact": (
                "Lord Carnarvon, le mécène de Carter, envisageait "
                "d'arrêter le financement des fouilles juste avant la "
                "découverte de la tombe."
            ),
        },
        "lycee": {
            "prompt": "Qu'est-ce qui rendait la tombe de Toutânkhamon si exceptionnelle par rapport aux autres tombes royales trouvées avant elle ?",
            "options": [
                "Elle était quasiment intacte, jamais pillée depuis l'Antiquité",
                "C'était la plus grande pyramide jamais construite",
                "Elle contenait la momie du pharaon le plus célèbre d'Égypte",
                "Elle avait été découverte par hasard par des touristes",
            ],
            "correct_index": 0,
            "fun_fact": (
                "La tombe, quasiment inviolée depuis plus de 3000 ans, "
                "regorgeait d'un trésor funéraire exceptionnel, dont le "
                "célèbre masque en or du pharaon."
            ),
        },
        "etudiant_adulte": {
            "prompt": (
                "Pourquoi la découverte de la tombe de Toutânkhamon a-t-elle "
                "eu un tel retentissement scientifique, alors que ce "
                "pharaon lui-même n'a régné que brièvement et sur une "
                "dynastie éphémère ?"
            ),
            "options": [
                "L'intégrité quasi totale de son mobilier funéraire offrait un instantané inédit du Nouvel Empire",
                "Toutânkhamon avait construit la Grande Pyramide de Gizeh",
                "C'était la première tombe royale égyptienne jamais découverte",
                "Sa momie contenait des inscriptions inconnues jusque-là",
            ],
            "correct_index": 0,
            "fun_fact": (
                "L'intégrité quasi totale du mobilier funéraire de "
                "Toutânkhamon a offert un instantané sans équivalent du "
                "faste matériel et religieux de l'Égypte du Nouvel "
                "Empire, bien plus que l'importance historique du "
                "pharaon lui-même."
            ),
        },
    },
}


def resolve_event_content(event, level):
    """Merge an event dict with its level-specific text, if any.

    Falls back to the event's own (single-level) text for slugs not yet
    covered in CONTENT_BY_LEVEL, and for an unrecognized/missing level.
    """
    level = level if level in STUDY_LEVELS else DEFAULT_LEVEL
    overrides = CONTENT_BY_LEVEL.get(event["slug"], {}).get(level)
    if not overrides:
        return event
    return {**event, **overrides}


def resolve_quiz(question, level):
    """Level-specific variant of a quiz question, or the original."""
    level = level if level in STUDY_LEVELS else DEFAULT_LEVEL
    overrides = QUIZ_BY_LEVEL.get(question["slug"], {}).get(level)
    if not overrides:
        return question
    return {**question, **overrides}
