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
    "declaration-independance-americaine": {
        "enfant": {
            "summary": (
                "Le 4 juillet 1776, les treize colonies américaines "
                "annoncent qu'elles ne veulent plus être gouvernées par "
                "l'Angleterre."
            ),
            "before": (
                "Les colonies américaines sont en guerre contre "
                "l'Angleterre depuis 1775. Elles trouvent injuste de "
                "payer des taxes sans avoir leur mot à dire."
            ),
            "during": (
                "Des représentants des colonies, réunis à Philadelphie, "
                "votent un texte écrit surtout par Thomas Jefferson."
            ),
            "after": (
                "La guerre continue encore plusieurs années, jusqu'à ce "
                "que l'Angleterre accepte enfin l'indépendance des "
                "États-Unis en 1783."
            ),
            "narrative": [
                "Depuis 1775, les treize colonies américaines sont en "
                "guerre contre l'Angleterre.",
                "Réunis à Philadelphie, des représentants des colonies "
                "votent un texte écrit surtout par Thomas Jefferson, le "
                "4 juillet 1776.",
                "Le texte dit que « tous les hommes sont créés égaux » "
                "et ont le droit d'être libres.",
            ],
            "why_it_matters": (
                "Ce texte donne naissance aux États-Unis d'Amérique et "
                "a inspiré d'autres pays, dont la France, quelques "
                "années plus tard."
            ),
        },
        "college": {
            "summary": (
                "Le Congrès continental adopte la déclaration "
                "proclamant l'indépendance des treize colonies "
                "américaines vis-à-vis de la Grande-Bretagne."
            ),
            "before": (
                "Les colonies américaines, en guerre depuis 1775 "
                "contre la couronne britannique, réclament la fin des "
                "taxes imposées sans qu'elles aient de représentants au "
                "Parlement."
            ),
            "during": (
                "Le Congrès continental adopte le texte rédigé "
                "principalement par Thomas Jefferson, proclamant les "
                "treize colonies libres et indépendantes."
            ),
            "after": (
                "La guerre d'indépendance se poursuit jusqu'en 1783, "
                "date à laquelle la Grande-Bretagne reconnaît "
                "officiellement les États-Unis d'Amérique."
            ),
            "narrative": [
                "Depuis 1775, les treize colonies britanniques "
                "d'Amérique du Nord sont en guerre contre la couronne, "
                "exaspérées par des taxes imposées sans représentation "
                "au Parlement de Londres.",
                "Réuni à Philadelphie, le Congrès continental charge un "
                "comité de cinq membres, dont Thomas Jefferson, de "
                "rédiger une déclaration justifiant la rupture. Le "
                "texte est adopté le 4 juillet 1776.",
                "La déclaration proclame que « tous les hommes sont "
                "créés égaux » et dotés de droits inaliénables, dont la "
                "vie, la liberté et la recherche du bonheur.",
            ],
            "why_it_matters": (
                "Ce texte fondateur donne naissance aux États-Unis "
                "d'Amérique et inspirera d'autres déclarations de "
                "droits, dont celle de 1789 en France."
            ),
        },
        "lycee": {
            "summary": (
                "Le Congrès continental adopte la déclaration "
                "proclamant l'indépendance des treize colonies "
                "américaines vis-à-vis de la Grande-Bretagne."
            ),
            "before": (
                "Les colonies américaines, en guerre depuis 1775 "
                "contre la couronne britannique après les batailles de "
                "Lexington et Concord, réclament la fin des taxes "
                "imposées sans qu'elles aient de représentants au "
                "Parlement de Londres — le principe de « no taxation "
                "without representation »."
            ),
            "during": (
                "Le Congrès continental, réuni à Philadelphie, adopte "
                "le texte rédigé principalement par Thomas Jefferson au "
                "sein d'un comité de cinq membres, proclamant les "
                "treize colonies libres et indépendantes."
            ),
            "after": (
                "La guerre d'indépendance se poursuit jusqu'en 1783, "
                "date à laquelle le traité de Paris consacre la "
                "reconnaissance officielle des États-Unis d'Amérique "
                "par la Grande-Bretagne."
            ),
            "narrative": [
                "Depuis 1775, les treize colonies britanniques "
                "d'Amérique du Nord sont en guerre ouverte contre la "
                "couronne, exaspérées par des taxes imposées sans "
                "qu'elles aient de représentants au Parlement de "
                "Londres.",
                "Réuni à Philadelphie, le Congrès continental charge un "
                "comité de cinq membres, dont Thomas Jefferson, John "
                "Adams et Benjamin Franklin, de rédiger une déclaration "
                "justifiant la rupture avec la Grande-Bretagne. Le "
                "texte est adopté le 4 juillet 1776.",
                "La déclaration proclame que « tous les hommes sont "
                "créés égaux » et dotés de droits inaliénables, dont la "
                "vie, la liberté et la recherche du bonheur. Elle "
                "énumère aussi les griefs contre le roi George III pour "
                "justifier la séparation.",
            ],
            "why_it_matters": (
                "Ce texte fondateur donne naissance aux États-Unis "
                "d'Amérique et inspirera par la suite d'autres "
                "déclarations de droits, dont la Déclaration des droits "
                "de l'homme et du citoyen française de 1789."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Le Congrès continental adopte à Philadelphie la "
                "déclaration proclamant l'indépendance des treize "
                "colonies américaines vis-à-vis de la Grande-Bretagne, "
                "texte fondateur dont la portée philosophique dépassera "
                "largement son contexte initial."
            ),
            "before": (
                "Les colonies américaines, en guerre depuis les "
                "batailles de Lexington et Concord en avril 1775, "
                "réclament la fin de taxes imposées sans représentation "
                "au Parlement de Londres — principe résumé par le "
                "slogan « no taxation without representation » — dans "
                "un climat où l'idée d'indépendance, encore minoritaire "
                "en 1775, gagne rapidement du terrain."
            ),
            "during": (
                "Le Congrès continental, réuni à Philadelphie, adopte "
                "le 4 juillet 1776 le texte rédigé principalement par "
                "Thomas Jefferson au sein d'un comité de cinq membres "
                "incluant John Adams et Benjamin Franklin, après "
                "plusieurs jours de débats et d'amendements, dont la "
                "suppression d'un paragraphe de Jefferson condamnant la "
                "traite négrière."
            ),
            "after": (
                "La guerre d'indépendance se poursuit jusqu'en 1783, "
                "année où le traité de Paris consacre la reconnaissance "
                "officielle des États-Unis par la Grande-Bretagne, "
                "avec l'appui décisif de la France à partir de 1778."
            ),
            "narrative": [
                "Depuis 1775, les treize colonies britanniques "
                "d'Amérique du Nord sont en guerre ouverte contre la "
                "couronne, exaspérées par des taxes imposées sans "
                "qu'elles aient de représentants au Parlement de "
                "Londres.",
                "Réuni à Philadelphie, le Congrès continental charge un "
                "comité de cinq membres, dont Thomas Jefferson, John "
                "Adams et Benjamin Franklin, de rédiger une déclaration "
                "justifiant la rupture avec la Grande-Bretagne. Le "
                "texte, débattu et amendé pendant plusieurs jours, est "
                "adopté le 4 juillet 1776.",
                "La déclaration proclame que « tous les hommes sont "
                "créés égaux » et dotés de droits inaliénables, dont la "
                "vie, la liberté et la recherche du bonheur — une "
                "formule qui, malgré la persistance de l'esclavage dans "
                "les colonies signataires, deviendra une référence "
                "universelle. Elle énumère aussi les griefs contre le "
                "roi George III pour justifier la séparation.",
            ],
            "why_it_matters": (
                "Ce texte fondateur donne naissance aux États-Unis "
                "d'Amérique et inspirera par la suite d'autres "
                "déclarations de droits, dont la Déclaration des droits "
                "de l'homme et du citoyen française de 1789, tout en "
                "laissant en suspens la contradiction entre ses "
                "principes d'égalité universelle et le maintien de "
                "l'esclavage, qui ne sera abolie que près d'un siècle "
                "plus tard."
            ),
        },
    },
    "arrivee-christophe-colomb": {
        "enfant": {
            "summary": (
                "En octobre 1492, Christophe Colomb et son équipage "
                "arrivent sur une île, après avoir traversé l'océan "
                "pour trouver une nouvelle route vers l'Asie."
            ),
            "before": (
                "Les rois d'Espagne payent le voyage de Colomb, qui "
                "veut trouver un chemin vers l'Asie en passant par "
                "l'ouest."
            ),
            "during": (
                "Après plus d'un mois de voyage en mer sans voir de "
                "terre, un marin aperçoit enfin une côte."
            ),
            "after": (
                "Colomb explore d'autres îles, pensant être arrivé près "
                "de l'Asie, puis rentre en Espagne annoncer sa "
                "découverte."
            ),
            "narrative": [
                "Le 3 août 1492, Christophe Colomb part d'Espagne avec "
                "trois bateaux pour essayer de rejoindre l'Asie en "
                "passant par l'ouest.",
                "Après plus de deux mois de voyage, un marin aperçoit "
                "enfin la terre, dans la nuit du 11 au 12 octobre 1492. "
                "L'équipage débarque sur une île qu'ils appellent San "
                "Salvador.",
                "Colomb pense avoir atteint l'Asie. Il visite d'autres "
                "îles avant de retourner en Espagne pour annoncer la "
                "nouvelle.",
            ],
            "why_it_matters": (
                "C'est le premier vrai contact entre l'Europe et "
                "l'Amérique. Après cela, beaucoup d'Européens viendront "
                "s'installer sur ce continent."
            ),
        },
        "college": {
            "summary": (
                "Après plus de deux mois de traversée, l'expédition de "
                "Christophe Colomb atteint une île des Bahamas, "
                "marquant le début des grandes découvertes européennes "
                "en Amérique."
            ),
            "before": (
                "Financé par les rois catholiques d'Espagne, Colomb "
                "cherche une route occidentale vers les Indes en "
                "traversant l'Atlantique."
            ),
            "during": (
                "Après 36 jours de traversée sans terre en vue, un "
                "marin de la Pinta aperçoit la côte d'une île qu'ils "
                "nomment San Salvador."
            ),
            "after": (
                "Colomb explore ensuite Cuba et Hispaniola, convaincu "
                "d'avoir atteint les abords de l'Asie, avant de rentrer "
                "en Espagne porter la nouvelle."
            ),
            "narrative": [
                "Le 3 août 1492, Christophe Colomb quitte l'Espagne "
                "avec trois navires — la Santa María, la Pinta et la "
                "Niña — dans l'espoir de rejoindre l'Asie en naviguant "
                "vers l'ouest.",
                "Après plus de deux mois de traversée éprouvante, un "
                "vigie de la Pinta aperçoit la terre dans la nuit du 11 "
                "au 12 octobre 1492. L'expédition débarque sur une île "
                "des Bahamas.",
                "Persuadé d'avoir atteint les Indes orientales, Colomb "
                "nomme les habitants qu'il rencontre « Indiens » et "
                "poursuit son exploration avant de regagner l'Espagne.",
            ],
            "why_it_matters": (
                "Ce premier contact durable entre l'Europe et le "
                "continent américain ouvre l'ère de la colonisation "
                "européenne des Amériques, aux conséquences immenses "
                "pour les populations autochtones."
            ),
        },
        "lycee": {
            "summary": (
                "Après plus de deux mois de traversée, l'expédition de "
                "Christophe Colomb atteint une île des Bahamas, "
                "marquant le début des grandes découvertes européennes "
                "en Amérique."
            ),
            "before": (
                "Financé par les rois catholiques d'Espagne, Isabelle "
                "de Castille et Ferdinand d'Aragon, Colomb cherche une "
                "route occidentale vers les Indes en traversant "
                "l'Atlantique, convaincu — à tort quant à la distance "
                "réelle — de la sphéricité de la Terre."
            ),
            "during": (
                "Après 36 jours de traversée sans terre en vue, "
                "marquée par les doutes croissants de l'équipage, un "
                "marin de la Pinta aperçoit la côte d'une île qu'ils "
                "nomment San Salvador."
            ),
            "after": (
                "Colomb explore ensuite Cuba et Hispaniola, convaincu "
                "d'avoir atteint les abords de l'Asie, avant de rentrer "
                "en Espagne porter la nouvelle de sa découverte."
            ),
            "narrative": [
                "Le 3 août 1492, Christophe Colomb quitte le port de "
                "Palos, en Espagne, avec trois navires — la Santa "
                "María, la Pinta et la Niña — et un équipage d'environ "
                "90 hommes, dans l'espoir de rejoindre l'Asie en "
                "naviguant vers l'ouest.",
                "Après plus de deux mois de traversée éprouvante, "
                "marquée par les doutes de l'équipage, un vigie de la "
                "Pinta aperçoit la terre dans la nuit du 11 au 12 "
                "octobre 1492. L'expédition débarque sur une île des "
                "Bahamas que Colomb baptise San Salvador.",
                "Persuadé d'avoir atteint les Indes orientales, Colomb "
                "nomme les habitants qu'il rencontre « Indiens ». Il "
                "poursuit son exploration vers Cuba et Hispaniola avant "
                "de regagner l'Espagne, où la nouvelle de sa découverte "
                "se répand rapidement en Europe.",
            ],
            "why_it_matters": (
                "Ce premier contact durable entre l'Europe et le "
                "continent américain ouvre l'ère de la colonisation "
                "européenne des Amériques, aux conséquences immenses — "
                "et dévastatrices pour les populations autochtones — "
                "pour les siècles suivants."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Après 36 jours de traversée sans terre en vue, "
                "l'expédition de Christophe Colomb, financée par la "
                "couronne espagnole, atteint une île des Bahamas, "
                "inaugurant sans le savoir un contact durable entre "
                "l'Europe et un continent dont l'existence était "
                "insoupçonnée."
            ),
            "before": (
                "Financé par les rois catholiques d'Espagne, Isabelle "
                "de Castille et Ferdinand d'Aragon, après le refus "
                "initial du Portugal, Colomb cherche une route "
                "occidentale vers les Indes en traversant l'Atlantique, "
                "sur la base d'une sous-estimation majeure de la "
                "circonférence terrestre qui, sans la présence "
                "inattendue d'un continent, aurait rendu le voyage "
                "impossible faute de vivres."
            ),
            "during": (
                "Après 36 jours de traversée sans terre en vue, marquée "
                "par les doutes croissants de l'équipage et une "
                "quasi-mutinerie, un marin de la Pinta, Rodrigo de "
                "Triana, aperçoit le premier la côte d'une île des "
                "Bahamas que Colomb nomme San Salvador, sans jamais "
                "reconnaître de son vivant qu'il ne s'agissait pas de "
                "l'Asie."
            ),
            "after": (
                "Colomb explore ensuite Cuba et Hispaniola, convaincu "
                "d'avoir atteint les abords du Japon puis de la Chine, "
                "avant de rentrer en Espagne porter la nouvelle, "
                "laissant derrière lui un premier comptoir, La Navidad, "
                "qui sera détruit avant son retour lors d'un second "
                "voyage."
            ),
            "narrative": [
                "Le 3 août 1492, Christophe Colomb quitte le port de "
                "Palos, en Espagne, avec trois navires — la Santa "
                "María, la Pinta et la Niña — et un équipage d'environ "
                "90 hommes, dans l'espoir de rejoindre l'Asie en "
                "naviguant vers l'ouest, sur la base de calculs sous-"
                "estimant largement la circonférence de la Terre.",
                "Après plus de deux mois de traversée éprouvante, "
                "marquée par les doutes de l'équipage, un vigie de la "
                "Pinta aperçoit la terre dans la nuit du 11 au 12 "
                "octobre 1492. L'expédition débarque sur une île des "
                "Bahamas que Colomb baptise San Salvador, sans jamais "
                "comprendre qu'il venait de découvrir, pour l'Europe, "
                "un continent jusque-là inconnu.",
                "Persuadé d'avoir atteint les Indes orientales, Colomb "
                "nomme les habitants qu'il rencontre « Indiens », une "
                "appellation qui perdurera des siècles. Il poursuit son "
                "exploration vers Cuba et Hispaniola avant de regagner "
                "l'Espagne, où la nouvelle de sa découverte se répand "
                "rapidement, déclenchant une vague de conquêtes et de "
                "colonisation.",
            ],
            "why_it_matters": (
                "Ce premier contact durable entre l'Europe et le "
                "continent américain ouvre l'ère de la colonisation "
                "européenne des Amériques et du « Grand Échange "
                "colombien » — transferts de plantes, d'animaux, de "
                "maladies et de populations entre les deux hémisphères "
                "— aux conséquences aussi immenses que dévastatrices "
                "pour les populations autochtones, décimées dans les "
                "décennies suivantes principalement par les maladies "
                "importées d'Europe."
            ),
        },
    },
    "nuit-du-4-aout": {
        "enfant": {
            "summary": (
                "Dans la nuit du 4 août 1789, les nobles et l'Église "
                "acceptent d'abandonner leurs privilèges, ce qui met "
                "fin aux droits des seigneurs sur les paysans."
            ),
            "before": (
                "Depuis la prise de la Bastille, des paysans en colère "
                "attaquent des châteaux dans les campagnes."
            ),
            "during": (
                "Pendant une réunion de nuit, des nobles abandonnent "
                "l'un après l'autre leurs droits sur les paysans."
            ),
            "after": (
                "Les impôts payés aux seigneurs et à l'Église sont "
                "supprimés. Tout le monde devient égal devant la loi."
            ),
            "narrative": [
                "Pendant l'été 1789, des paysans en colère attaquent "
                "des châteaux pour détruire les papiers qui les "
                "obligeaient à payer des impôts aux seigneurs.",
                "Le soir du 4 août, à l'Assemblée, deux députés "
                "proposent d'abandonner ces droits féodaux. D'autres "
                "nobles font pareil les uns après les autres.",
                "En une nuit, l'Assemblée vote la fin de nombreux "
                "privilèges et impôts injustes qui existaient depuis "
                "très longtemps.",
            ],
            "why_it_matters": (
                "Cette nuit marque la fin de siècles d'inégalités entre "
                "nobles et paysans, et prépare l'idée que tous les "
                "citoyens sont égaux devant la loi."
            ),
        },
        "college": {
            "summary": (
                "Dans un climat d'émotion collective, l'Assemblée "
                "constituante vote l'abolition des privilèges féodaux, "
                "mettant fin de facto au système seigneurial en "
                "France."
            ),
            "before": (
                "Depuis la prise de la Bastille, des révoltes "
                "paysannes contre les droits seigneuraux se multiplient "
                "dans les campagnes, épisode connu sous le nom de "
                "« Grande Peur »."
            ),
            "during": (
                "Lors d'une séance de nuit, des députés nobles et "
                "ecclésiastiques renoncent tour à tour à leurs "
                "privilèges, dans un mouvement d'entraînement "
                "collectif."
            ),
            "after": (
                "Les décrets qui suivent suppriment la dîme, les "
                "droits féodaux et les privilèges fiscaux, posant les "
                "bases d'une société d'égalité devant la loi."
            ),
            "narrative": [
                "À l'été 1789, la « Grande Peur » s'empare des "
                "campagnes françaises : des rumeurs d'un complot "
                "aristocratique poussent les paysans à attaquer "
                "châteaux et registres seigneuriaux.",
                "Dans la soirée du 4 août 1789, le vicomte de Noailles "
                "et le duc d'Aiguillon proposent l'abolition des droits "
                "féodaux. Nobles et clergé renoncent les uns après les "
                "autres à leurs privilèges.",
                "En quelques heures, l'Assemblée vote l'abolition de la "
                "dîme, des droits seigneuriaux et des privilèges "
                "fiscaux des ordres.",
            ],
            "why_it_matters": (
                "La nuit du 4 août 1789 met fin, en droit, à des "
                "siècles de société d'ordres, posant l'un des "
                "fondements de l'égalité civile proclamée quelques "
                "jours plus tard."
            ),
        },
        "lycee": {
            "summary": (
                "Dans un climat d'émotion collective, l'Assemblée "
                "constituante vote l'abolition des privilèges féodaux, "
                "mettant fin de facto au système seigneurial en "
                "France."
            ),
            "before": (
                "Depuis la prise de la Bastille, des révoltes "
                "paysannes contre les droits seigneuraux se multiplient "
                "dans les campagnes, épisode connu sous le nom de "
                "« Grande Peur », alimenté par la crainte d'un complot "
                "aristocratique."
            ),
            "during": (
                "Lors d'une séance de nuit à l'Assemblée constituante, "
                "des députés nobles et ecclésiastiques renoncent tour à "
                "tour à leurs privilèges, dans un mouvement "
                "d'entraînement collectif largement improvisé."
            ),
            "after": (
                "Les décrets qui suivent dans les jours suivants "
                "suppriment la dîme, les droits féodaux, les privilèges "
                "fiscaux et la vénalité des offices, posant les bases "
                "juridiques d'une société d'égalité devant la loi."
            ),
            "narrative": [
                "À l'été 1789, la « Grande Peur » s'empare des "
                "campagnes françaises : des rumeurs d'un complot "
                "aristocratique poussent les paysans à attaquer "
                "châteaux et registres seigneuriaux pour détruire les "
                "preuves de leurs obligations féodales.",
                "Dans la soirée du 4 août 1789, à l'Assemblée "
                "constituante, le vicomte de Noailles et le duc "
                "d'Aiguillon proposent l'abolition des droits féodaux "
                "pour apaiser les campagnes. Dans un mouvement "
                "d'émulation, nobles et clergé renoncent les uns après "
                "les autres à leurs privilèges.",
                "En quelques heures nocturnes, l'Assemblée vote "
                "l'abolition de la dîme, des droits seigneuriaux, des "
                "privilèges fiscaux des ordres et de la vénalité des "
                "offices. Les décrets définitifs seront rédigés et "
                "votés dans les jours suivants.",
            ],
            "why_it_matters": (
                "La nuit du 4 août 1789 met fin, en droit, à des "
                "siècles de société d'ordres et de privilèges féodaux, "
                "posant l'un des fondements de l'égalité civile "
                "proclamée quelques jours plus tard dans la Déclaration "
                "des droits de l'homme et du citoyen."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Dans un climat d'émotion collective largement "
                "improvisé, l'Assemblée constituante vote en une seule "
                "nuit l'abolition des privilèges féodaux, mettant fin "
                "de facto à des siècles de société d'ordres en France."
            ),
            "before": (
                "Depuis la prise de la Bastille, des révoltes paysannes "
                "contre les droits seigneuraux se multiplient dans les "
                "campagnes lors de la « Grande Peur », alimentée par "
                "des rumeurs de complot aristocratique et par la "
                "disette persistante de l'été 1789."
            ),
            "during": (
                "Lors d'une séance de nuit à l'Assemblée constituante, "
                "initialement convoquée pour traiter du brigandage "
                "rural, des députés nobles et ecclésiastiques renoncent "
                "tour à tour à leurs privilèges dans un mouvement "
                "d'entraînement collectif largement improvisé et "
                "peut-être orchestré en coulisses par certains libéraux."
            ),
            "after": (
                "Les décrets rédigés dans les jours suivants nuancent "
                "cependant la portée du vote initial : certains droits "
                "seront rachetables plutôt qu'abolis sans compensation, "
                "un point qui restera contesté jusqu'à leur suppression "
                "définitive et sans indemnité en 1793."
            ),
            "narrative": [
                "À l'été 1789, la « Grande Peur » s'empare des "
                "campagnes françaises : des rumeurs d'un complot "
                "aristocratique poussent les paysans à attaquer "
                "châteaux et registres seigneuriaux pour détruire les "
                "preuves de leurs obligations féodales.",
                "Dans la soirée du 4 août 1789, à l'Assemblée "
                "constituante, le vicomte de Noailles et le duc "
                "d'Aiguillon proposent l'abolition des droits féodaux "
                "pour apaiser les campagnes. Dans un mouvement "
                "d'émulation qui surprend les députés eux-mêmes, nobles "
                "et clergé renoncent les uns après les autres à leurs "
                "privilèges, certains par conviction, d'autres pour ne "
                "pas paraître en retrait.",
                "En quelques heures nocturnes, l'Assemblée vote "
                "l'abolition de principe de la dîme, des droits "
                "seigneuriaux, des privilèges fiscaux des ordres et de "
                "la vénalité des offices — même si les décrets "
                "définitifs, rédigés dans les jours suivants, "
                "atténueront la portée immédiate de certaines mesures.",
            ],
            "why_it_matters": (
                "La nuit du 4 août 1789 met fin, en droit, à des "
                "siècles de société d'ordres et de privilèges féodaux, "
                "posant l'un des fondements de l'égalité civile "
                "proclamée quelques jours plus tard dans la Déclaration "
                "des droits de l'homme et du citoyen — même si, dans "
                "les faits, l'abolition complète et sans indemnité des "
                "droits seigneuriaux ne sera votée qu'en 1793, sous la "
                "Convention."
            ),
        },
    },
    "bataille-de-waterloo": {
        "enfant": {
            "summary": (
                "Le 18 juin 1815, l'armée de Napoléon perd la bataille "
                "de Waterloo. C'est la fin définitive de son règne "
                "d'empereur."
            ),
            "before": (
                "Napoléon revient au pouvoir en France après avoir été "
                "exilé sur une île. Les autres pays d'Europe s'allient "
                "aussitôt contre lui."
            ),
            "during": (
                "L'armée française combat les Anglais, puis les "
                "Prussiens arrivent en renfort et changent le cours de "
                "la bataille."
            ),
            "after": (
                "Napoléon doit abandonner son titre d'empereur. Il est "
                "envoyé sur une île très loin, Sainte-Hélène, où il "
                "mourra."
            ),
            "narrative": [
                "Après s'être évadé de l'île d'Elbe, Napoléon reprend "
                "le pouvoir en France. Les pays d'Europe s'unissent "
                "aussitôt contre lui.",
                "Le 18 juin 1815, près du village de Waterloo, en "
                "Belgique, l'armée française affronte les Anglais du "
                "duc de Wellington.",
                "En fin de journée, l'armée prussienne arrive en "
                "renfort et l'armée française est vaincue.",
            ],
            "why_it_matters": (
                "Cette défaite met fin pour toujours au règne de "
                "Napoléon comme empereur des Français."
            ),
        },
        "college": {
            "summary": (
                "L'armée de Napoléon est défaite par les forces "
                "coalisées britanniques et prussiennes, mettant fin "
                "définitivement à l'épopée impériale française."
            ),
            "before": (
                "Revenu du bannissement de l'île d'Elbe, Napoléon "
                "reprend le pouvoir en France pendant les Cent-Jours, "
                "provoquant la formation d'une septième coalition "
                "contre lui."
            ),
            "during": (
                "L'armée française affronte les troupes britanniques du "
                "duc de Wellington, puis l'arrivée de l'armée prussienne "
                "de Blücher en fin de journée fait basculer la "
                "bataille."
            ),
            "after": (
                "Napoléon abdique une seconde fois quatre jours plus "
                "tard et est exilé sur l'île de Sainte-Hélène, où il "
                "mourra en 1821."
            ),
            "narrative": [
                "Après son évasion de l'île d'Elbe en février 1815, "
                "Napoléon reprend le pouvoir en France. Les grandes "
                "puissances européennes forment aussitôt une nouvelle "
                "coalition pour l'arrêter.",
                "Le 18 juin 1815, près du village belge de Waterloo, "
                "l'armée française affronte les troupes anglo-alliées "
                "du duc de Wellington, retranchées sur le plateau du "
                "Mont-Saint-Jean.",
                "En fin d'après-midi, l'armée prussienne du maréchal "
                "Blücher, que Napoléon croyait tenue à distance, arrive "
                "sur le flanc droit français. Prise en tenaille, "
                "l'armée française se débande.",
            ],
            "why_it_matters": (
                "Waterloo met un terme définitif à l'épopée "
                "napoléonienne et ouvre en Europe une longue période de "
                "restauration monarchique."
            ),
        },
        "lycee": {
            "summary": (
                "L'armée de Napoléon est défaite par les forces "
                "coalisées britanniques et prussiennes, mettant fin "
                "définitivement à l'épopée impériale française."
            ),
            "before": (
                "Revenu du bannissement de l'île d'Elbe, Napoléon "
                "reprend le pouvoir en France pendant les Cent-Jours, "
                "provoquant la formation d'une septième coalition "
                "réunissant Britanniques, Prussiens, Autrichiens et "
                "Russes contre lui."
            ),
            "during": (
                "L'armée française affronte les troupes britanniques du "
                "duc de Wellington, retranchées sur le plateau du "
                "Mont-Saint-Jean, puis l'arrivée décisive de l'armée "
                "prussienne de Blücher en fin de journée fait basculer "
                "la bataille."
            ),
            "after": (
                "Napoléon abdique une seconde fois quatre jours plus "
                "tard et est exilé par les Britanniques sur l'île "
                "isolée de Sainte-Hélène, dans l'Atlantique Sud, où il "
                "mourra en 1821."
            ),
            "narrative": [
                "Après son évasion de l'île d'Elbe en février 1815, "
                "Napoléon reprend le pouvoir en France sans coup férir. "
                "Les grandes puissances européennes, réunies au congrès "
                "de Vienne, forment aussitôt une nouvelle coalition "
                "pour l'arrêter.",
                "Le 18 juin 1815, près du village belge de Waterloo, "
                "l'armée française affronte les troupes anglo-alliées "
                "du duc de Wellington, retranchées sur le plateau du "
                "Mont-Saint-Jean. Les assauts français, dont la célèbre "
                "charge de cavalerie du maréchal Ney, ne parviennent "
                "pas à percer les lignes ennemies.",
                "En fin d'après-midi, l'armée prussienne du maréchal "
                "Blücher, que Napoléon croyait tenue à distance, arrive "
                "sur le flanc droit français. Prise en tenaille, la "
                "Grande Armée se débande. La Garde impériale, engagée "
                "en dernier recours, est repoussée.",
            ],
            "why_it_matters": (
                "Waterloo met un terme définitif à l'épopée "
                "napoléonienne et ouvre en Europe une longue période de "
                "restauration monarchique et d'équilibre entre grandes "
                "puissances qui durera jusqu'à la Première Guerre "
                "mondiale."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "L'armée française est défaite près du village belge "
                "de Waterloo par les forces coalisées "
                "anglo-néerlandaises et prussiennes, mettant fin en une "
                "seule journée à l'épisode des Cent-Jours et "
                "définitivement à l'épopée impériale napoléonienne."
            ),
            "before": (
                "Revenu du bannissement de l'île d'Elbe en février "
                "1815 et accueilli en libérateur par une partie de la "
                "population, Napoléon reprend le pouvoir en France "
                "pendant les Cent-Jours sans qu'un coup de feu ne soit "
                "tiré, provoquant aussitôt la formation d'une septième "
                "coalition réunissant Britanniques, Prussiens, "
                "Autrichiens et Russes, déterminés à ne négocier avec "
                "lui sous aucun prétexte."
            ),
            "during": (
                "Retardé par un terrain détrempé qui l'oblige à "
                "différer son attaque de plusieurs heures — un délai "
                "qui laissera aux Prussiens le temps d'intervenir — "
                "l'armée française affronte les troupes britanniques et "
                "alliées du duc de Wellington, retranchées sur le "
                "plateau du Mont-Saint-Jean, avant que l'arrivée "
                "décisive de l'armée prussienne de Blücher, que "
                "Napoléon croyait mise hors de combat deux jours plus "
                "tôt à Ligny, ne fasse définitivement basculer la "
                "bataille en fin de journée."
            ),
            "after": (
                "Napoléon abdique une seconde fois quatre jours plus "
                "tard, le 22 juin, en faveur de son fils, avant d'être "
                "capturé et exilé par les Britanniques sur l'île "
                "isolée de Sainte-Hélène, dans l'Atlantique Sud, où il "
                "mourra en 1821, probablement d'un cancer de l'estomac."
            ),
            "narrative": [
                "Après son évasion de l'île d'Elbe en février 1815, "
                "Napoléon reprend le pouvoir en France sans coup férir, "
                "porté par une partie de l'armée et de la population "
                "lasse de la Restauration. Les grandes puissances "
                "européennes, réunies au congrès de Vienne, le "
                "déclarent aussitôt hors-la-loi et forment une nouvelle "
                "coalition pour l'arrêter.",
                "Le 18 juin 1815, près du village belge de Waterloo, "
                "l'armée française, retardée par un sol détrempé, "
                "affronte les troupes anglo-alliées du duc de "
                "Wellington, retranchées sur le plateau du "
                "Mont-Saint-Jean. Les assauts français, dont la célèbre "
                "et coûteuse charge de cavalerie du maréchal Ney contre "
                "des carrés d'infanterie intacts, ne parviennent pas à "
                "percer les lignes ennemies.",
                "En fin d'après-midi, l'armée prussienne du maréchal "
                "Blücher, que Napoléon croyait durablement écartée "
                "après sa victoire à Ligny deux jours plus tôt, arrive "
                "sur le flanc droit français. Prise en tenaille, la "
                "Grande Armée se débande. La Garde impériale, engagée "
                "en dernier recours, est repoussée pour la première "
                "fois de son histoire.",
            ],
            "why_it_matters": (
                "Waterloo met un terme définitif à l'épopée "
                "napoléonienne et à vingt-trois années de guerres "
                "quasi ininterrompues en Europe depuis la Révolution "
                "française, ouvrant une longue période de restauration "
                "monarchique et d'équilibre concerté entre grandes "
                "puissances (le « concert européen ») qui, malgré des "
                "crises ponctuelles, durera jusqu'à la Première Guerre "
                "mondiale."
            ),
        },
    },
    "sacre-napoleon": {
        "enfant": {
            "summary": (
                "Le 2 décembre 1804, Napoléon Bonaparte se couronne "
                "lui-même empereur des Français, dans la cathédrale "
                "Notre-Dame de Paris."
            ),
            "before": (
                "Napoléon dirige déjà la France depuis plusieurs "
                "années. Le peuple vote pour qu'il devienne empereur."
            ),
            "during": (
                "Pendant une grande cérémonie, le pape vient de Rome, "
                "mais c'est Napoléon lui-même qui pose la couronne sur "
                "sa tête."
            ),
            "after": (
                "La France devient un Empire. Napoléon va gouverner "
                "jusqu'en 1814."
            ),
            "narrative": [
                "Après plusieurs années au pouvoir, Napoléon Bonaparte "
                "fait voter le peuple français pour devenir empereur.",
                "Le 2 décembre 1804, à Notre-Dame de Paris, une grande "
                "cérémonie a lieu. Le pape Pie VII vient de Rome, mais "
                "Napoléon se couronne lui-même, puis couronne sa "
                "femme Joséphine.",
                "Ce geste montre que Napoléon tient son pouvoir de "
                "lui-même et du peuple, pas de l'Église.",
            ],
            "why_it_matters": (
                "Ce jour marque la naissance de l'Empire français. "
                "Napoléon devient l'un des hommes les plus puissants "
                "d'Europe."
            ),
        },
        "college": {
            "summary": (
                "Napoléon Bonaparte se couronne empereur des Français "
                "à Notre-Dame de Paris, en présence du pape Pie VII, "
                "marquant la naissance du Premier Empire."
            ),
            "before": (
                "Premier consul depuis 1799 puis consul à vie, "
                "Bonaparte fait approuver par référendum populaire "
                "l'instauration d'un Empire héréditaire."
            ),
            "during": (
                "Lors d'une cérémonie fastueuse à Notre-Dame, Napoléon "
                "se couronne lui-même, puis couronne son épouse "
                "Joséphine, sous le regard du pape venu de Rome."
            ),
            "after": (
                "Le Premier Empire est instauré ; Napoléon règne sur "
                "la France jusqu'à sa première abdication en 1814."
            ),
            "narrative": [
                "Après le coup d'État du 18 brumaire en 1799 et "
                "plusieurs années comme Premier consul, Napoléon "
                "Bonaparte fait plébisciter par le peuple français "
                "l'instauration d'un Empire héréditaire.",
                "Le 2 décembre 1804, Notre-Dame de Paris accueille une "
                "cérémonie de sacre fastueuse. Le pape Pie VII bénit "
                "les insignes impériaux, mais c'est Napoléon lui-même "
                "qui pose la couronne sur sa tête, puis couronne son "
                "épouse Joséphine.",
                "Ce geste, resté célèbre, symbolise la volonté de "
                "Napoléon de tenir son pouvoir du peuple et de "
                "lui-même plutôt que de l'Église.",
            ],
            "why_it_matters": (
                "Le sacre marque la transformation de la République "
                "française en Empire héréditaire et l'apogée politique "
                "de Napoléon."
            ),
        },
        "lycee": {
            "summary": (
                "Napoléon Bonaparte se couronne empereur des Français "
                "à Notre-Dame de Paris, en présence du pape Pie VII, "
                "marquant la naissance du Premier Empire."
            ),
            "before": (
                "Premier consul depuis 1799 puis consul à vie depuis "
                "1802, Bonaparte fait approuver par référendum "
                "populaire l'instauration d'un Empire héréditaire à son "
                "profit, avec l'appui d'un Sénat largement acquis à sa "
                "cause."
            ),
            "during": (
                "Lors d'une cérémonie fastueuse à Notre-Dame, orchestrée "
                "par le peintre Jacques-Louis David, Napoléon se "
                "couronne lui-même, puis couronne son épouse Joséphine, "
                "sous le regard du pape venu spécialement de Rome."
            ),
            "after": (
                "Le Premier Empire est instauré ; Napoléon règne sur la "
                "France et domine militairement l'Europe jusqu'à sa "
                "première abdication en 1814."
            ),
            "narrative": [
                "Après le coup d'État du 18 brumaire en 1799 et "
                "plusieurs années passées comme Premier consul, "
                "Napoléon Bonaparte fait plébisciter par le peuple "
                "français l'instauration d'un Empire héréditaire à son "
                "profit.",
                "Le 2 décembre 1804, la cathédrale Notre-Dame de Paris "
                "accueille une cérémonie de sacre fastueuse, orchestrée "
                "par le peintre Jacques-Louis David. Le pape Pie VII, "
                "venu tout exprès de Rome, bénit les insignes "
                "impériaux, mais c'est Napoléon lui-même qui pose la "
                "couronne sur sa tête, puis couronne son épouse "
                "Joséphine.",
                "Ce geste, resté célèbre, symbolise la volonté de "
                "Napoléon de tenir son pouvoir du peuple et de "
                "lui-même plutôt que de l'Église, tout en s'inscrivant "
                "dans la continuité cérémonielle des sacres royaux "
                "français.",
            ],
            "why_it_matters": (
                "Le sacre marque la transformation de la République "
                "française en Empire héréditaire et l'apogée politique "
                "de Napoléon, qui dominera l'Europe militairement "
                "jusqu'à sa défaite de 1814-1815."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Napoléon Bonaparte se couronne lui-même empereur des "
                "Français à Notre-Dame de Paris, en présence — mais "
                "sans l'intervention directe — du pape Pie VII, geste "
                "hautement symbolique marquant la naissance du Premier "
                "Empire."
            ),
            "before": (
                "Premier consul depuis le coup d'État du 18 brumaire "
                "en 1799, puis consul à vie depuis le plébiscite de "
                "1802, Bonaparte fait approuver par un nouveau "
                "référendum populaire — dont les résultats furent "
                "largement manipulés — l'instauration d'un Empire "
                "héréditaire à son profit."
            ),
            "during": (
                "Lors d'une cérémonie fastueuse à Notre-Dame, dont la "
                "mise en scène est confiée au peintre Jacques-Louis "
                "David, Napoléon se saisit de la couronne des mains du "
                "pape et se couronne lui-même, avant de couronner son "
                "épouse Joséphine — un geste rompant délibérément avec "
                "la tradition du sacre royal où le monarque recevait la "
                "couronne des mains du prélat."
            ),
            "after": (
                "Le Premier Empire est instauré ; Napoléon règne sur "
                "la France et domine militairement l'Europe jusqu'à sa "
                "première abdication en 1814, période marquée par la "
                "création d'une noblesse impériale et d'institutions "
                "durables comme le Code civil."
            ),
            "narrative": [
                "Après le coup d'État du 18 brumaire en 1799 et "
                "plusieurs années passées comme Premier consul, "
                "Napoléon Bonaparte fait plébisciter par le peuple "
                "français l'instauration d'un Empire héréditaire à son "
                "profit, dans un contexte de menace de complots "
                "royalistes qu'il instrumentalise pour justifier une "
                "succession assurée.",
                "Le 2 décembre 1804, la cathédrale Notre-Dame de Paris "
                "accueille une cérémonie de sacre fastueuse, orchestrée "
                "par le peintre Jacques-Louis David, qui en immortalisera "
                "la scène dans un tableau monumental. Le pape Pie VII, "
                "venu tout exprès de Rome dans l'espoir d'obtenir des "
                "concessions religieuses, bénit les insignes impériaux, "
                "mais c'est Napoléon lui-même qui pose la couronne sur "
                "sa tête, puis couronne son épouse Joséphine.",
                "Ce geste, resté célèbre, symbolise la volonté de "
                "Napoléon de tenir son pouvoir du peuple et de "
                "lui-même plutôt que de l'Église, tout en s'inscrivant "
                "dans la continuité cérémonielle des sacres royaux "
                "français qu'il cherche paradoxalement à égaler en "
                "légitimité.",
            ],
            "why_it_matters": (
                "Le sacre marque la transformation de la République "
                "française en Empire héréditaire et l'apogée politique "
                "de Napoléon, qui dominera l'Europe militairement "
                "jusqu'à sa défaite de 1814-1815, tout en laissant un "
                "héritage institutionnel durable — Code civil, Légion "
                "d'honneur, administration centralisée — qui survivra "
                "à sa chute."
            ),
        },
    },
    "signature-magna-carta": {
        "enfant": {
            "summary": (
                "En 1215, le roi d'Angleterre Jean sans Terre accepte "
                "un texte qui limite son pouvoir pour la première fois."
            ),
            "before": (
                "Le roi Jean sans Terre est impopulaire : il a perdu "
                "des guerres et fait payer trop d'impôts."
            ),
            "during": (
                "Des seigneurs (les barons) obligent le roi à signer "
                "un texte qui limite ses pouvoirs."
            ),
            "after": (
                "Ce texte, la Grande Charte, deviendra très important "
                "plus tard pour les droits des gens."
            ),
            "narrative": [
                "Le roi Jean sans Terre fait payer trop d'impôts à ses "
                "seigneurs, qui se révoltent contre lui.",
                "En 1215, les barons obligent le roi à signer un "
                "document appelé la Magna Carta (Grande Charte).",
                "Ce texte dit qu'on ne peut pas mettre quelqu'un en "
                "prison sans un vrai jugement. C'est une grande "
                "nouveauté pour l'époque.",
            ],
            "why_it_matters": (
                "C'est l'un des premiers textes à limiter le pouvoir "
                "d'un roi. Il a inspiré beaucoup d'autres lois plus "
                "tard, partout dans le monde."
            ),
        },
        "college": {
            "summary": (
                "Le roi Jean sans Terre appose son sceau sur la Grande "
                "Charte, un texte limitant pour la première fois le "
                "pouvoir royal anglais face à ses barons."
            ),
            "before": (
                "Impopulaire après des défaites militaires en France "
                "et une fiscalité jugée abusive, le roi Jean sans Terre "
                "fait face à une révolte de ses barons."
            ),
            "during": (
                "Réunis à Runnymede, les barons contraignent le roi à "
                "sceller un document limitant son pouvoir, notamment le "
                "droit d'être jugé par ses pairs."
            ),
            "after": (
                "Bien que rapidement contestée par le roi lui-même, la "
                "Grande Charte sera plusieurs fois réaffirmée et "
                "deviendra un texte fondateur du droit anglais."
            ),
            "narrative": [
                "Au début du XIIIe siècle, le roi Jean sans Terre "
                "s'aliène ses barons par de lourdes taxes destinées à "
                "financer des guerres coûteuses contre le roi de "
                "France.",
                "En 1215, une coalition de barons en révolte s'empare "
                "de Londres et contraint le roi à négocier. Le 15 "
                "juin, à Runnymede, Jean sans Terre appose son sceau "
                "sur la Magna Carta.",
                "Le texte garantit qu'aucun homme libre ne peut être "
                "emprisonné sans jugement légal de ses pairs — une "
                "première limite posée au pouvoir royal absolu.",
            ],
            "why_it_matters": (
                "La Magna Carta est devenue un symbole fondateur de "
                "l'État de droit et a inspiré des principes "
                "constitutionnels repris bien plus tard."
            ),
        },
        "lycee": {
            "summary": (
                "Le roi Jean sans Terre appose son sceau sur la Grande "
                "Charte, un texte limitant pour la première fois le "
                "pouvoir royal anglais face à ses barons."
            ),
            "before": (
                "Impopulaire après des défaites militaires en France "
                "(notamment la perte de la Normandie) et une fiscalité "
                "jugée abusive, le roi Jean sans Terre fait face à une "
                "révolte de ses barons, aggravée par un conflit avec la "
                "papauté."
            ),
            "during": (
                "Réunis à Runnymede, les barons contraignent le roi à "
                "sceller un document en soixante-trois articles "
                "limitant son pouvoir et garantissant certains droits, "
                "notamment celui d'être jugé par ses pairs."
            ),
            "after": (
                "Bien que rapidement contestée par le roi lui-même dès "
                "après sa signature, la Grande Charte sera plusieurs "
                "fois réaffirmée par ses successeurs et deviendra un "
                "texte fondateur du droit constitutionnel anglais."
            ),
            "narrative": [
                "Au début du XIIIe siècle, le roi Jean sans Terre "
                "d'Angleterre s'aliène ses barons par de lourdes taxes "
                "destinées à financer des guerres coûteuses et "
                "infructueuses contre le roi de France, ainsi que par "
                "des conflits avec la papauté.",
                "En 1215, une coalition de barons en révolte s'empare "
                "de Londres et contraint le roi à négocier. Le 15 "
                "juin, dans la prairie de Runnymede au bord de la "
                "Tamise, Jean sans Terre appose son sceau sur la Magna "
                "Carta, un document en soixante-trois articles.",
                "Le texte garantit notamment qu'aucun homme libre ne "
                "peut être emprisonné ou dépossédé sans jugement légal "
                "de ses pairs, et qu'aucune taxe exceptionnelle ne peut "
                "être levée sans l'accord d'un conseil de barons — une "
                "première limite posée au pouvoir royal absolu.",
            ],
            "why_it_matters": (
                "Bien que largement pensée pour protéger les intérêts "
                "des barons plutôt que du peuple, la Magna Carta est "
                "devenue un symbole fondateur de l'État de droit et a "
                "inspiré des principes constitutionnels repris bien "
                "plus tard, jusque dans la Déclaration d'indépendance "
                "américaine."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Le roi Jean sans Terre appose son sceau sur la Grande "
                "Charte, texte transactionnel destiné à apaiser ses "
                "barons mais qui deviendra, par ses réinterprétations "
                "successives, l'un des fondements symboliques du "
                "constitutionnalisme anglo-saxon."
            ),
            "before": (
                "Impopulaire après la perte de la Normandie et "
                "d'autres possessions continentales face à Philippe "
                "Auguste, et après une fiscalité jugée abusive destinée "
                "à financer des reconquêtes infructueuses, le roi Jean "
                "sans Terre fait face à une révolte ouverte de ses "
                "barons, aggravée par un long conflit avec la papauté "
                "qui l'avait excommunié."
            ),
            "during": (
                "Réunis à Runnymede après avoir pris Londres, les "
                "barons contraignent le roi à sceller un document en "
                "soixante-trois articles limitant son pouvoir — un "
                "texte négocié dans l'urgence et dont beaucoup de "
                "clauses répondaient à des griefs très concrets et "
                "temporaires plutôt qu'à des principes abstraits."
            ),
            "after": (
                "Annulée par le pape dès août 1215 à la demande du roi "
                "lui-même, la charte est réémise sous une forme "
                "modifiée après la mort de Jean en 1216, puis "
                "régulièrement réaffirmée par ses successeurs, "
                "processus par lequel elle acquiert progressivement son "
                "statut de texte fondateur."
            ),
            "narrative": [
                "Au début du XIIIe siècle, le roi Jean sans Terre "
                "d'Angleterre s'aliène ses barons par de lourdes taxes "
                "destinées à financer des guerres coûteuses et "
                "infructueuses contre le roi de France, ainsi que par "
                "des conflits avec la papauté qui aboutissent à son "
                "excommunication en 1209.",
                "En 1215, une coalition de barons en révolte s'empare "
                "de Londres et contraint le roi à négocier. Le 15 "
                "juin, dans la prairie de Runnymede au bord de la "
                "Tamise, Jean sans Terre appose son sceau sur la Magna "
                "Carta, un document en soixante-trois articles rédigé "
                "dans l'urgence pour répondre à des griefs très "
                "concrets des barons.",
                "Le texte garantit notamment qu'aucun homme libre ne "
                "peut être emprisonné ou dépossédé sans jugement légal "
                "de ses pairs, et qu'aucune taxe exceptionnelle ne peut "
                "être levée sans l'accord d'un conseil de barons — une "
                "première limite posée au pouvoir royal absolu, même "
                "si le terme « homme libre » exclut alors l'immense "
                "majorité de la population, encore serve.",
            ],
            "why_it_matters": (
                "Bien que largement pensée pour protéger les intérêts "
                "matériels des barons plutôt que ceux du peuple, et "
                "bien qu'annulée puis réémise à plusieurs reprises dans "
                "les décennies suivant sa signature, la Magna Carta est "
                "devenue, par un long processus de réinterprétation "
                "juridique aux XVIIe et XVIIIe siècles, un symbole "
                "fondateur de l'État de droit — inspirant jusqu'à la "
                "Déclaration d'indépendance américaine et le "
                "constitutionnalisme moderne."
            ),
        },
    },
    "eruption-vesuve": {
        "enfant": {
            "summary": (
                "En l'an 79, le volcan Vésuve explose et recouvre la "
                "ville de Pompéi de cendres, tuant beaucoup d'habitants."
            ),
            "before": (
                "Pompéi est une ville romaine au pied du Vésuve, un "
                "volcan que tout le monde croyait endormi pour "
                "toujours."
            ),
            "during": (
                "Le volcan explose et envoie des cendres et des pierres "
                "très haut dans le ciel, pendant des heures."
            ),
            "after": (
                "La ville est recouverte de cendres et disparaît sous "
                "terre pendant plus de 1600 ans."
            ),
            "narrative": [
                "Le Vésuve, un volcan près de Naples en Italie, était "
                "considéré comme éteint. Le 24 août de l'an 79, il "
                "explose brutalement.",
                "Pendant des heures, des cendres et des pierres "
                "tombent sur Pompéi. Puis des nuages de gaz très chauds "
                "dévalent le volcan et tuent les gens restés sur place.",
                "Un écrivain nommé Pline le Jeune a vu la catastrophe "
                "depuis loin et l'a racontée. Son oncle, parti aider "
                "les gens, est mort ce jour-là.",
            ],
            "why_it_matters": (
                "Grâce aux cendres qui l'ont recouverte, on a retrouvé "
                "Pompéi très bien conservée. On peut voir comment "
                "vivaient les Romains il y a 2000 ans."
            ),
        },
        "college": {
            "summary": (
                "L'éruption soudaine du Vésuve ensevelit les villes "
                "romaines de Pompéi et Herculanum sous plusieurs "
                "mètres de cendres."
            ),
            "before": (
                "Pompéi et Herculanum sont des villes romaines "
                "prospères au pied du Vésuve, un volcan considéré "
                "comme endormi depuis des générations."
            ),
            "during": (
                "En quelques heures, le volcan projette une colonne de "
                "cendres sur des kilomètres, avant que des coulées de "
                "gaz brûlants ne recouvrent les villes."
            ),
            "after": (
                "Les cités sont abandonnées et oubliées pendant plus "
                "de seize siècles, avant d'être redécouvertes à partir "
                "du XVIIIe siècle."
            ),
            "narrative": [
                "Le Vésuve, volcan surplombant la baie de Naples, "
                "était considéré comme éteint. Le 24 août de l'an 79, "
                "il entre brutalement en éruption, projetant cendres "
                "et pierre ponce à près de 30 km d'altitude.",
                "Pendant plusieurs heures, cendres et pierres "
                "s'abattent sur Pompéi. Dans la nuit, des coulées "
                "pyroclastiques — nuées de gaz brûlants — surprennent "
                "et tuent ceux restés sur place, notamment à "
                "Herculanum.",
                "L'écrivain romain Pline le Jeune, témoin depuis "
                "l'autre rive du golfe, laisse un récit détaillé de la "
                "catastrophe, au cours de laquelle son oncle Pline "
                "l'Ancien trouve la mort.",
            ],
            "why_it_matters": (
                "L'éruption a paradoxalement permis la conservation "
                "exceptionnelle de Pompéi, offrant depuis le XVIIIe "
                "siècle un instantané unique de la vie romaine."
            ),
        },
        "lycee": {
            "summary": (
                "L'éruption soudaine du Vésuve ensevelit les villes "
                "romaines de Pompéi et Herculanum sous plusieurs "
                "mètres de cendres, figeant leur vie quotidienne pour "
                "deux millénaires."
            ),
            "before": (
                "Pompéi et Herculanum sont des villes romaines "
                "prospères au pied du Vésuve, volcan considéré comme "
                "endormi depuis des générations et dont les habitants "
                "ne perçoivent pas les signes avant-coureurs (séismes "
                "répétés) comme une menace directe."
            ),
            "during": (
                "En quelques heures, le volcan projette une colonne de "
                "cendres et de pierre ponce sur des kilomètres, avant "
                "que des coulées pyroclastiques brûlantes ne recouvrent "
                "les villes."
            ),
            "after": (
                "Les cités sont abandonnées et oubliées pendant plus "
                "de seize siècles, avant d'être redécouvertes par des "
                "fouilles archéologiques à partir du XVIIIe siècle."
            ),
            "narrative": [
                "Le Vésuve, volcan surplombant la baie de Naples, "
                "était considéré comme éteint par les habitants de la "
                "région. Le 24 août de l'an 79, il entre brutalement "
                "en éruption, projetant une immense colonne de cendres "
                "et de pierre ponce à près de 30 kilomètres d'altitude.",
                "Pendant plusieurs heures, cendres et pierres "
                "s'abattent sur Pompéi, poussant une partie de la "
                "population à fuir. Dans la nuit, des coulées "
                "pyroclastiques — des nuées de gaz brûlants et de "
                "débris dévalant les pentes du volcan à grande vitesse "
                "— surprennent et tuent ceux restés sur place, "
                "notamment à Herculanum, ensevelie plus rapidement "
                "encore.",
                "L'écrivain romain Pline le Jeune, témoin depuis "
                "l'autre rive du golfe de Naples, laisse un récit "
                "détaillé de la catastrophe, au cours de laquelle son "
                "oncle Pline l'Ancien, parti porter secours, trouve la "
                "mort.",
            ],
            "why_it_matters": (
                "L'éruption a paradoxalement permis la conservation "
                "exceptionnelle de Pompéi et Herculanum sous les "
                "cendres, offrant aux archéologues depuis le XVIIIe "
                "siècle un instantané unique et détaillé de la vie "
                "quotidienne romaine."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "L'éruption plinienne soudaine du Vésuve ensevelit en "
                "quelques heures les villes romaines de Pompéi et "
                "Herculanum sous cendres et coulées pyroclastiques, "
                "figeant leur vie quotidienne pour près de deux "
                "millénaires et léguant à la postérité le récit "
                "oculaire le plus ancien connu d'une éruption "
                "volcanique."
            ),
            "before": (
                "Pompéi et Herculanum sont des villes romaines "
                "prospères au pied du Vésuve, volcan considéré comme "
                "endormi depuis des générations ; des séismes répétés "
                "dans les jours précédents, dont on sait rétrospectivement "
                "qu'ils annonçaient l'éruption, ne sont pas perçus "
                "comme une menace par une population habituée à "
                "l'activité sismique modérée de la région."
            ),
            "during": (
                "En quelques heures, le volcan projette une colonne "
                "plinienne de cendres et de pierre ponce à près de 30 "
                "km d'altitude, avant qu'une série de coulées "
                "pyroclastiques — nuées ardentes de gaz et de débris "
                "dévalant les pentes à plusieurs centaines de km/h — ne "
                "recouvrent les villes en quelques minutes."
            ),
            "after": (
                "Les cités sont abandonnées et progressivement oubliées "
                "pendant plus de seize siècles, leur emplacement même "
                "disparaissant de la mémoire collective, avant d'être "
                "redécouvertes par des fouilles archéologiques "
                "méthodiques à partir du XVIIIe siècle, sous l'impulsion "
                "des Bourbons de Naples."
            ),
            "narrative": [
                "Le Vésuve, volcan surplombant la baie de Naples, "
                "était considéré comme éteint par les habitants de la "
                "région, malgré des séismes répétés dans les jours "
                "précédant l'éruption. Le 24 août de l'an 79 — une "
                "datation elle-même débattue par les archéologues, qui "
                "penchent parfois pour octobre sur la base de récentes "
                "découvertes —, il entre brutalement en éruption, "
                "projetant une immense colonne de cendres et de pierre "
                "ponce à près de 30 kilomètres d'altitude.",
                "Pendant plusieurs heures, cendres et pierres "
                "s'abattent sur Pompéi, poussant une partie de la "
                "population à fuir. Dans la nuit, des coulées "
                "pyroclastiques — des nuées de gaz brûlants et de "
                "débris dévalant les pentes du volcan à grande vitesse "
                "— surprennent et tuent en quelques instants ceux "
                "restés sur place, notamment à Herculanum, ensevelie "
                "plus rapidement encore sous des dépôts qui carbonisent "
                "instantanément le bois et préservent certains corps.",
                "L'écrivain romain Pline le Jeune, témoin depuis "
                "l'autre rive du golfe de Naples, laisse dans deux "
                "lettres à l'historien Tacite un récit détaillé et "
                "scientifiquement précieux de la catastrophe — le "
                "terme « éruption plinienne » lui rend d'ailleurs "
                "hommage —, au cours de laquelle son oncle Pline "
                "l'Ancien, naturaliste et amiral parti porter secours "
                "par la mer, trouve la mort à Stabies.",
            ],
            "why_it_matters": (
                "L'éruption a paradoxalement permis la conservation "
                "exceptionnelle de Pompéi et Herculanum sous les "
                "cendres, offrant aux archéologues depuis le XVIIIe "
                "siècle un instantané d'une précision inégalée de la "
                "vie quotidienne romaine — architecture, fresques, "
                "graffitis, corps figés dans leurs derniers instants — "
                "tout en fournissant, par le témoignage de Pline le "
                "Jeune, le premier récit scientifique connu d'une "
                "éruption volcanique."
            ),
        },
    },
    "krach-de-1929": {
        "enfant": {
            "summary": (
                "Le 24 octobre 1929, la Bourse de New York s'effondre. "
                "C'est le début d'une très grande crise économique "
                "dans le monde."
            ),
            "before": (
                "Beaucoup de gens achètent des actions (des petits "
                "morceaux d'entreprises) en empruntant de l'argent, "
                "pensant que les prix vont toujours monter."
            ),
            "during": (
                "Un jour, tout le monde veut vendre ses actions en "
                "même temps. Les prix s'effondrent très vite."
            ),
            "after": (
                "Des banques font faillite, beaucoup de gens perdent "
                "leur travail. C'est le début d'une crise mondiale."
            ),
            "narrative": [
                "Dans les années 1920, les prix à la Bourse de New "
                "York montent beaucoup. Des gens empruntent de "
                "l'argent pour acheter encore plus d'actions.",
                "Le 24 octobre 1929, surnommé « jeudi noir », tout le "
                "monde essaie de vendre ses actions en même temps. Les "
                "prix s'effondrent.",
                "Les jours suivants, la panique continue. En quelques "
                "jours, énormément d'argent disparaît, et beaucoup de "
                "gens sont ruinés.",
            ],
            "why_it_matters": (
                "Ce krach boursier déclenche une immense crise "
                "économique, appelée la Grande Dépression, qui touche "
                "le monde entier pendant des années."
            ),
        },
        "college": {
            "summary": (
                "Le « jeudi noir » à la Bourse de New York déclenche "
                "un krach boursier qui précipite le monde dans la "
                "Grande Dépression."
            ),
            "before": (
                "Après des années de spéculation alimentée par l'achat "
                "d'actions à crédit, les cours de la Bourse atteignent "
                "des niveaux jugés intenables."
            ),
            "during": (
                "Le 24 octobre 1929, une vague de ventes paniquées "
                "s'abat sur Wall Street ; malgré une intervention des "
                "grandes banques, la confiance s'effondre les jours "
                "suivants."
            ),
            "after": (
                "Le krach entraîne faillites bancaires et chômage de "
                "masse aux États-Unis, puis se propage à l'économie "
                "mondiale."
            ),
            "narrative": [
                "Durant les « années folles », la Bourse de New York "
                "connaît une hausse spectaculaire, alimentée par des "
                "investisseurs empruntant pour acheter des actions.",
                "Le 24 octobre 1929, surnommé « jeudi noir », une "
                "vague de ventes massives s'abat sur le New York Stock "
                "Exchange. Un consortium de banques tente d'enrayer la "
                "chute, offrant un répit temporaire.",
                "Mais la confiance ne revient pas : les 28 et 29 "
                "octobre voient de nouvelles chutes vertigineuses. Des "
                "milliards de dollars de valeur boursière s'évaporent.",
            ],
            "why_it_matters": (
                "Le krach de 1929 déclenche la Grande Dépression, la "
                "pire crise économique du XXe siècle, marquée par un "
                "chômage massif dans le monde entier."
            ),
        },
        "lycee": {
            "summary": (
                "Le « jeudi noir » à la Bourse de New York déclenche "
                "un krach boursier qui précipite le monde dans la "
                "Grande Dépression des années 1930."
            ),
            "before": (
                "Après des années de spéculation effrénée alimentée "
                "par l'achat d'actions à crédit (« buying on margin »), "
                "les cours de la Bourse de New York atteignent des "
                "niveaux jugés intenables par de nombreux économistes."
            ),
            "during": (
                "Le 24 octobre 1929, une vague de ventes paniquées "
                "s'abat sur Wall Street ; malgré une intervention des "
                "grandes banques, la confiance s'effondre définitivement "
                "les jours suivants."
            ),
            "after": (
                "Le krach entraîne faillites bancaires et chômage de "
                "masse aux États-Unis, puis se propage à l'économie "
                "mondiale, provoquant la Grande Dépression."
            ),
            "narrative": [
                "Durant les « années folles », la Bourse de New York "
                "connaît une hausse spectaculaire, largement alimentée "
                "par des investisseurs empruntant massivement pour "
                "acheter des actions, pariant sur une hausse continue "
                "des cours.",
                "Le 24 octobre 1929, surnommé « jeudi noir », une "
                "vague de ventes massives et paniquées s'abat sur le "
                "New York Stock Exchange. Un consortium de grandes "
                "banques tente d'enrayer la chute en rachetant des "
                "actions, offrant un répit temporaire.",
                "Mais la confiance ne revient pas : les 28 et 29 "
                "octobre, surnommés « lundi noir » et « mardi noir », "
                "voient de nouvelles chutes vertigineuses. En quelques "
                "jours, des milliards de dollars de valeur boursière "
                "s'évaporent, ruinant nombre d'investisseurs.",
            ],
            "why_it_matters": (
                "Le krach de 1929 déclenche la Grande Dépression, la "
                "pire crise économique du XXe siècle, marquée par des "
                "faillites bancaires en série, un chômage massif et des "
                "répercussions économiques et politiques mondiales "
                "durant toute la décennie suivante."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Le « jeudi noir » à la Bourse de New York, aggravé "
                "les jours suivants par le « lundi noir » et le "
                "« mardi noir », déclenche un krach boursier qui "
                "précipite le monde dans la Grande Dépression, la plus "
                "grave crise économique du XXe siècle."
            ),
            "before": (
                "Après des années de spéculation effrénée alimentée "
                "par l'achat d'actions à crédit (« buying on margin », "
                "parfois avec seulement 10 % d'apport personnel), les "
                "cours de la Bourse de New York atteignent des niveaux "
                "largement déconnectés de la valeur réelle des "
                "entreprises, malgré les avertissements de certains "
                "économistes."
            ),
            "during": (
                "Le 24 octobre 1929, une vague de ventes paniquées "
                "s'abat sur Wall Street ; un consortium de grandes "
                "banques menées par la Maison Morgan tente d'enrayer la "
                "chute en rachetant symboliquement des actions, mais la "
                "confiance s'effondre définitivement les jours suivants "
                "malgré ce répit apparent."
            ),
            "after": (
                "Le krach entraîne un effondrement du crédit, des "
                "faillites bancaires en cascade et un chômage de masse "
                "aux États-Unis, puis se propage à l'économie mondiale "
                "via l'effondrement du commerce international, "
                "provoquant la Grande Dépression qui durera jusqu'à la "
                "fin des années 1930."
            ),
            "narrative": [
                "Durant les « années folles », la Bourse de New York "
                "connaît une hausse spectaculaire et largement "
                "déconnectée de l'économie réelle, alimentée par des "
                "investisseurs empruntant massivement pour acheter des "
                "actions, pariant sur une hausse indéfinie des cours.",
                "Le 24 octobre 1929, surnommé « jeudi noir », une "
                "vague de ventes massives et paniquées s'abat sur le "
                "New York Stock Exchange, provoquant la vente de près "
                "de 13 millions de titres en une seule journée. Un "
                "consortium de grandes banques menées par la Maison "
                "Morgan tente d'enrayer la chute en rachetant "
                "publiquement des actions, offrant un répit temporaire.",
                "Mais la confiance ne revient pas : les 28 et 29 "
                "octobre, surnommés « lundi noir » et « mardi noir », "
                "voient de nouvelles chutes vertigineuses, avec près de "
                "16 millions de titres échangés le seul mardi 29. En "
                "quelques jours, des dizaines de milliards de dollars "
                "de valeur boursière s'évaporent, ruinant nombre "
                "d'investisseurs et fragilisant tout le système "
                "bancaire américain.",
            ],
            "why_it_matters": (
                "Le krach de 1929 déclenche la Grande Dépression, la "
                "pire crise économique du XXe siècle : faillites "
                "bancaires en série, chômage touchant jusqu'à un quart "
                "de la population active américaine, effondrement du "
                "commerce mondial aggravé par des mesures "
                "protectionnistes, et répercussions politiques durables "
                "— dont, selon de nombreux historiens, un terreau "
                "favorable à la montée des régimes autoritaires en "
                "Europe."
            ),
        },
    },
    "attaque-pearl-harbor": {
        "enfant": {
            "summary": (
                "Le 7 décembre 1941, des avions japonais attaquent par "
                "surprise la base américaine de Pearl Harbor. Les "
                "États-Unis entrent alors en guerre."
            ),
            "before": (
                "Le Japon et les États-Unis sont fâchés depuis "
                "longtemps à cause de la guerre du Japon en Asie."
            ),
            "during": (
                "Des avions japonais attaquent sans prévenir les "
                "bateaux de guerre américains, à Hawaï."
            ),
            "after": (
                "Le lendemain, les États-Unis déclarent la guerre au "
                "Japon et rejoignent la Seconde Guerre mondiale."
            ),
            "narrative": [
                "Le matin du 7 décembre 1941, des avions japonais "
                "attaquent par surprise la base militaire américaine "
                "de Pearl Harbor, à Hawaï.",
                "En moins de deux heures, l'attaque détruit ou "
                "endommage beaucoup de bateaux de guerre américains et "
                "tue environ 2 400 personnes.",
                "Le président Roosevelt appelle ce jour « une date qui "
                "restera dans l'infamie ». Les États-Unis déclarent la "
                "guerre au Japon dès le lendemain.",
            ],
            "why_it_matters": (
                "Cette attaque fait entrer les États-Unis dans la "
                "Seconde Guerre mondiale, qui devient alors un conflit "
                "vraiment mondial."
            ),
        },
        "college": {
            "summary": (
                "L'aviation japonaise attaque par surprise la flotte "
                "américaine du Pacifique, provoquant l'entrée en "
                "guerre des États-Unis."
            ),
            "before": (
                "Les tensions entre les États-Unis et le Japon "
                "s'aggravent après l'embargo américain sur le pétrole, "
                "imposé en réponse à l'expansion japonaise en Asie."
            ),
            "during": (
                "Des avions japonais lancés depuis des porte-avions "
                "frappent sans avertissement la flotte américaine "
                "ancrée à Pearl Harbor."
            ),
            "after": (
                "Les États-Unis déclarent la guerre au Japon dès le "
                "lendemain, entraînant leur entrée dans le conflit "
                "mondial."
            ),
            "narrative": [
                "Au matin du 7 décembre 1941, des centaines d'avions "
                "japonais décollent de porte-avions et frappent par "
                "surprise la base navale américaine de Pearl Harbor.",
                "En un peu moins de deux heures, l'attaque coule ou "
                "endommage huit cuirassés américains et fait environ "
                "2 400 morts. Les porte-avions américains, absents ce "
                "jour-là, échappent à la destruction.",
                "Le président Roosevelt qualifie le 7 décembre de "
                "« date qui restera dans l'infamie » devant le "
                "Congrès, qui vote la guerre au Japon dès le lendemain.",
            ],
            "why_it_matters": (
                "L'attaque de Pearl Harbor précipite l'entrée en "
                "guerre des États-Unis et transforme le conflit "
                "européen en une guerre véritablement mondiale."
            ),
        },
        "lycee": {
            "summary": (
                "L'aviation japonaise attaque par surprise la flotte "
                "américaine du Pacifique, provoquant l'entrée en "
                "guerre des États-Unis dans la Seconde Guerre "
                "mondiale."
            ),
            "before": (
                "Les tensions entre les États-Unis et le Japon "
                "impérial s'aggravent après l'embargo américain sur le "
                "pétrole imposé en réponse à l'expansion japonaise en "
                "Asie, alors que des négociations diplomatiques se "
                "poursuivent encore officiellement."
            ),
            "during": (
                "Des avions japonais lancés depuis des porte-avions "
                "frappent sans avertissement la flotte américaine "
                "ancrée à Pearl Harbor, détruisant ou endommageant de "
                "nombreux navires de guerre."
            ),
            "after": (
                "Les États-Unis déclarent la guerre au Japon dès le "
                "lendemain, entraînant leur entrée dans le conflit "
                "mondial aux côtés des Alliés."
            ),
            "narrative": [
                "Au matin du 7 décembre 1941, alors que les "
                "négociations diplomatiques se poursuivent officiellement "
                "à Washington, des centaines d'avions japonais "
                "décollent de porte-avions et frappent par surprise la "
                "base navale américaine de Pearl Harbor, à Hawaï.",
                "En un peu moins de deux heures, l'attaque coule ou "
                "endommage huit cuirassés américains et détruit près "
                "de 200 avions, faisant environ 2 400 morts, pour la "
                "plupart des militaires. Les porte-avions américains, "
                "absents ce jour-là, échappent à la destruction.",
                "Le président Franklin D. Roosevelt qualifie le 7 "
                "décembre de « date qui restera dans l'infamie » devant "
                "le Congrès, qui vote la déclaration de guerre au Japon "
                "dès le lendemain.",
            ],
            "why_it_matters": (
                "L'attaque de Pearl Harbor précipite l'entrée en "
                "guerre des États-Unis, jusque-là officiellement "
                "neutres, et transforme définitivement le conflit "
                "européen en une guerre véritablement mondiale."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "L'aviation embarquée japonaise attaque par surprise, "
                "sans déclaration de guerre préalable, la flotte "
                "américaine du Pacifique ancrée à Pearl Harbor, "
                "provoquant l'entrée en guerre immédiate et quasi "
                "unanime des États-Unis."
            ),
            "before": (
                "Les tensions entre les États-Unis et le Japon "
                "impérial s'aggravent après l'embargo américain total "
                "sur le pétrole et l'acier imposé en juillet 1941 en "
                "réponse à l'expansion japonaise en Indochine, alors "
                "que des négociations diplomatiques se poursuivent "
                "encore officiellement à Washington au moment même de "
                "l'attaque."
            ),
            "during": (
                "Des avions japonais lancés depuis six porte-avions "
                "frappent en deux vagues successives, sans avertissement "
                "ni déclaration de guerre préalable, la flotte "
                "américaine ancrée à Pearl Harbor, ciblant "
                "prioritairement les cuirassés — une doctrine navale "
                "bientôt rendue obsolète par l'importance décisive des "
                "porte-avions dans la guerre du Pacifique."
            ),
            "after": (
                "Les États-Unis déclarent la guerre au Japon dès le "
                "lendemain avec une quasi-unanimité au Congrès, mettant "
                "fin à des années de fort courant isolationniste dans "
                "l'opinion publique américaine, et l'Allemagne et "
                "l'Italie déclarent à leur tour la guerre aux États-Unis "
                "quelques jours plus tard."
            ),
            "narrative": [
                "Au matin du 7 décembre 1941, alors que les "
                "négociations diplomatiques se poursuivent officiellement "
                "à Washington, des centaines d'avions japonais "
                "décollent de six porte-avions et frappent par surprise "
                "la base navale américaine de Pearl Harbor, à Hawaï, "
                "en deux vagues successives.",
                "En un peu moins de deux heures, l'attaque coule ou "
                "endommage huit cuirassés américains et détruit près "
                "de 200 avions, faisant environ 2 400 morts, pour la "
                "plupart des militaires du seul cuirassé Arizona. Les "
                "porte-avions américains, absents ce jour-là en "
                "manœuvre, échappent à la destruction — un hasard qui "
                "s'avérera stratégiquement décisif pour la suite de la "
                "guerre du Pacifique.",
                "Le président Franklin D. Roosevelt qualifie le 7 "
                "décembre de « date qui restera dans l'infamie » devant "
                "le Congrès, qui vote la déclaration de guerre au Japon "
                "dès le lendemain à une quasi-unanimité, mettant fin "
                "brutalement à des années de débat isolationniste aux "
                "États-Unis.",
            ],
            "why_it_matters": (
                "L'attaque de Pearl Harbor précipite l'entrée en "
                "guerre des États-Unis, jusque-là officiellement "
                "neutres malgré une aide croissante aux Alliés, et "
                "transforme définitivement le conflit européen en une "
                "guerre véritablement mondiale ; elle constitue aussi, "
                "sur le plan militaire, une victoire tactique japonaise "
                "mais une erreur stratégique majeure, l'industrie "
                "américaine s'avérant capable de reconstruire sa flotte "
                "bien plus vite que le Japon ne pouvait l'anticiper."
            ),
        },
    },
    "bombardement-hiroshima": {
        "enfant": {
            "summary": (
                "Le 6 août 1945, les États-Unis larguent la première "
                "bombe atomique de l'histoire sur la ville japonaise "
                "d'Hiroshima."
            ),
            "before": (
                "Le Japon continue la guerre malgré des bombardements "
                "très destructeurs sur ses villes."
            ),
            "during": (
                "Un avion américain largue une bombe atomique sur "
                "Hiroshima. La ville est détruite en quelques instants."
            ),
            "after": (
                "Trois jours plus tard, une deuxième bombe tombe sur "
                "Nagasaki. Le Japon se rend le 15 août 1945."
            ),
            "narrative": [
                "En 1945, le Japon continue de se battre malgré une "
                "situation très difficile.",
                "Le 6 août 1945, l'avion américain Enola Gay largue "
                "une bombe atomique sur Hiroshima. La ville est "
                "détruite et des dizaines de milliers de personnes "
                "meurent immédiatement.",
                "Le 9 août, une deuxième bombe tombe sur Nagasaki. Le "
                "15 août, le Japon annonce qu'il arrête la guerre.",
            ],
            "why_it_matters": (
                "C'est la première fois qu'une bombe atomique est "
                "utilisée dans une guerre. Cela met fin à la Seconde "
                "Guerre mondiale, mais pose de grandes questions "
                "encore aujourd'hui."
            ),
        },
        "college": {
            "summary": (
                "Les États-Unis larguent la première bombe atomique de "
                "l'histoire militaire sur la ville d'Hiroshima, "
                "provoquant des destructions sans précédent."
            ),
            "before": (
                "Dans les derniers mois de la guerre du Pacifique, le "
                "Japon refuse de capituler malgré des bombardements "
                "dévastateurs sur ses grandes villes."
            ),
            "during": (
                "Le bombardier américain Enola Gay largue la bombe "
                "atomique « Little Boy » sur Hiroshima, détruisant la "
                "majeure partie de la ville en quelques instants."
            ),
            "after": (
                "Une seconde bombe frappe Nagasaki trois jours plus "
                "tard ; le Japon annonce sa capitulation le 15 août "
                "1945."
            ),
            "narrative": [
                "À l'été 1945, malgré une situation militaire "
                "désespérée, le Japon refuse la capitulation sans "
                "conditions exigée par les Alliés.",
                "Le 6 août 1945 à 8h15, le bombardier américain Enola "
                "Gay largue sur Hiroshima la bombe atomique « Little "
                "Boy ». L'explosion détruit instantanément une grande "
                "partie de la ville et tue des dizaines de milliers de "
                "personnes.",
                "Le Japon ne capitule pas immédiatement. Le 9 août, "
                "une seconde bombe frappe Nagasaki. L'empereur Hirohito "
                "annonce la capitulation du Japon le 15 août.",
            ],
            "why_it_matters": (
                "Premier usage militaire de l'arme atomique, le "
                "bombardement d'Hiroshima précipite la fin de la "
                "Seconde Guerre mondiale tout en ouvrant l'ère "
                "nucléaire."
            ),
        },
        "lycee": {
            "summary": (
                "Les États-Unis larguent la première bombe atomique de "
                "l'histoire militaire sur la ville d'Hiroshima, "
                "provoquant des destructions et des pertes humaines "
                "sans précédent."
            ),
            "before": (
                "Dans les derniers mois de la guerre du Pacifique, le "
                "Japon refuse de capituler malgré des bombardements "
                "conventionnels dévastateurs sur ses grandes villes, "
                "les Alliés redoutant par ailleurs le coût humain "
                "d'une invasion terrestre de l'archipel."
            ),
            "during": (
                "Le bombardier américain Enola Gay largue la bombe "
                "atomique « Little Boy » sur Hiroshima, détruisant la "
                "majeure partie de la ville en quelques instants."
            ),
            "after": (
                "Une seconde bombe atomique frappe Nagasaki trois "
                "jours plus tard ; le Japon annonce sa capitulation le "
                "15 août 1945, mettant fin à la Seconde Guerre "
                "mondiale."
            ),
            "narrative": [
                "À l'été 1945, malgré une situation militaire "
                "désespérée, le gouvernement japonais refuse la "
                "capitulation sans conditions exigée par les Alliés, "
                "qui redoutent le coût humain d'une invasion terrestre "
                "du Japon.",
                "Le 6 août 1945 à 8h15 du matin, le bombardier "
                "américain Enola Gay largue sur Hiroshima la bombe "
                "atomique « Little Boy ». L'explosion détruit "
                "instantanément une grande partie de la ville et tue "
                "des dizaines de milliers de personnes sur le coup, un "
                "bilan qui continuera de s'alourdir du fait des "
                "radiations.",
                "Le Japon ne capitule pas immédiatement. Le 9 août, "
                "une seconde bombe atomique frappe la ville de "
                "Nagasaki. L'empereur Hirohito annonce la capitulation "
                "du Japon le 15 août, mettant un terme définitif à la "
                "Seconde Guerre mondiale.",
            ],
            "why_it_matters": (
                "Premier usage militaire de l'arme atomique de "
                "l'histoire, le bombardement d'Hiroshima précipite la "
                "fin de la Seconde Guerre mondiale tout en ouvrant "
                "l'ère nucléaire et ses lourdes questions éthiques et "
                "stratégiques, encore débattues aujourd'hui."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Les États-Unis larguent sur Hiroshima « Little Boy », "
                "la première bombe atomique de l'histoire militaire, "
                "provoquant des destructions et des pertes humaines "
                "sans précédent dans un débat historiographique encore "
                "vif sur la nécessité réelle de son emploi."
            ),
            "before": (
                "Dans les derniers mois de la guerre du Pacifique, le "
                "Japon refuse la capitulation sans conditions exigée "
                "par les Alliés malgré des bombardements incendiaires "
                "conventionnels déjà dévastateurs — celui de Tokyo en "
                "mars 1945 ayant fait plus de morts en une nuit que "
                "Hiroshima —, les stratèges américains redoutant par "
                "ailleurs un coût humain considérable pour une "
                "invasion terrestre."
            ),
            "during": (
                "Le bombardier américain Enola Gay largue à 8h15 la "
                "bombe atomique « Little Boy », d'un type à uranium "
                "jamais testé auparavant, sur Hiroshima, ville choisie "
                "notamment pour son importance militaire et l'absence "
                "de bombardements antérieurs permettant de mesurer les "
                "effets de l'arme."
            ),
            "after": (
                "Une seconde bombe, au plutonium cette fois, frappe "
                "Nagasaki trois jours plus tard ; le Japon annonce sa "
                "capitulation le 15 août 1945, mettant fin à la Seconde "
                "Guerre mondiale, mais laissant ouvert un débat "
                "historiographique durable sur le poids respectif des "
                "bombardements et de l'entrée en guerre soviétique "
                "contre le Japon, survenue entre les deux bombes."
            ),
            "narrative": [
                "À l'été 1945, malgré une situation militaire "
                "désespérée, le gouvernement japonais refuse la "
                "capitulation sans conditions exigée par les Alliés, "
                "qui redoutent le coût humain d'une invasion terrestre "
                "du Japon après les pertes très lourdes subies à "
                "Iwo Jima et Okinawa.",
                "Le 6 août 1945 à 8h15 du matin, le bombardier "
                "américain Enola Gay largue sur Hiroshima la bombe "
                "atomique « Little Boy », d'un type à uranium enrichi "
                "jamais testé au préalable. L'explosion détruit "
                "instantanément une grande partie de la ville et tue "
                "des dizaines de milliers de personnes sur le coup, un "
                "bilan qui continuera de s'alourdir dans les mois "
                "suivants du fait des radiations, pour atteindre "
                "environ 140 000 morts fin 1945.",
                "Le Japon ne capitule pas immédiatement. Le 8 août, "
                "l'URSS déclare la guerre au Japon et envahit la "
                "Mandchourie ; le 9 août, une seconde bombe, au "
                "plutonium, frappe la ville de Nagasaki. L'empereur "
                "Hirohito, dans une intervention radiophonique inédite, "
                "annonce la capitulation du Japon le 15 août, mettant "
                "un terme définitif à la Seconde Guerre mondiale.",
            ],
            "why_it_matters": (
                "Premier usage militaire de l'arme atomique de "
                "l'histoire, le bombardement d'Hiroshima précipite la "
                "fin de la Seconde Guerre mondiale tout en ouvrant "
                "l'ère nucléaire et la dissuasion qui structurera la "
                "guerre froide ; les historiens débattent encore de la "
                "part exacte jouée par les bombardements atomiques "
                "face à l'entrée en guerre soviétique dans la décision "
                "japonaise de capituler, ainsi que des lourdes "
                "questions éthiques posées par l'emploi d'une arme de "
                "destruction massive contre une population "
                "majoritairement civile."
            ),
        },
    },
    "capitulation-allemande-1945": {
        "enfant": {
            "summary": (
                "Le 8 mai 1945, l'Allemagne accepte sa défaite. C'est "
                "la fin de la guerre en Europe."
            ),
            "before": (
                "Hitler se suicide le 30 avril 1945, pendant que "
                "l'armée soviétique encercle Berlin."
            ),
            "during": (
                "Des généraux allemands signent l'arrêt des combats, "
                "d'abord en France, puis une deuxième fois à Berlin."
            ),
            "after": (
                "La guerre continue encore en Asie, mais en Europe, "
                "c'est fini. On fête la victoire le 8 mai."
            ),
            "narrative": [
                "Fin avril 1945, l'armée soviétique encercle Berlin. "
                "Hitler se suicide le 30 avril.",
                "Le 7 mai, des généraux allemands signent la fin des "
                "combats en France. Staline veut une deuxième "
                "signature à Berlin.",
                "Dans la nuit du 8 au 9 mai, une nouvelle cérémonie a "
                "lieu à Berlin. En France, on fête la victoire le 8 "
                "mai.",
            ],
            "why_it_matters": (
                "C'est la fin de la guerre en Europe, après presque "
                "six ans de combats terribles."
            ),
        },
        "college": {
            "summary": (
                "La capitulation sans conditions de l'Allemagne nazie "
                "met fin à la Seconde Guerre mondiale en Europe."
            ),
            "before": (
                "Après le suicide d'Hitler le 30 avril 1945 et la "
                "chute de Berlin encerclée par l'Armée rouge, "
                "l'effondrement militaire allemand est total."
            ),
            "during": (
                "Une première capitulation est signée à Reims le 7 "
                "mai ; une seconde cérémonie, exigée par Staline, se "
                "tient à Berlin dans la nuit du 8 au 9 mai."
            ),
            "after": (
                "La guerre continue en Asie jusqu'en août, mais le 8 "
                "mai reste commémoré comme la fin des combats en "
                "Europe."
            ),
            "narrative": [
                "Fin avril 1945, l'Armée rouge encercle Berlin. "
                "Hitler se suicide dans son bunker le 30 avril.",
                "Le 7 mai, le général Alfred Jodl signe à Reims l'acte "
                "de capitulation. Staline exige une seconde cérémonie "
                "sur le sol allemand.",
                "Dans la nuit du 8 au 9 mai, une nouvelle cérémonie se "
                "tient à Berlin devant les Soviétiques. En France, "
                "c'est le 8 mai qui reste célébré.",
            ],
            "why_it_matters": (
                "La capitulation allemande met fin à près de six ans "
                "de guerre en Europe et ouvre la voie au début de la "
                "guerre froide."
            ),
        },
        "lycee": {
            "summary": (
                "La capitulation sans conditions de l'Allemagne nazie "
                "met fin à la Seconde Guerre mondiale en Europe, "
                "célébrée comme le « Jour de la Victoire »."
            ),
            "before": (
                "Après le suicide d'Hitler le 30 avril 1945 et la "
                "chute de Berlin encerclée par l'Armée rouge, "
                "l'effondrement militaire allemand est total."
            ),
            "during": (
                "Une première capitulation est signée à Reims le 7 "
                "mai ; une seconde cérémonie, exigée par Staline, se "
                "tient à Berlin dans la nuit du 8 au 9 mai."
            ),
            "after": (
                "La guerre continue en Asie jusqu'à la capitulation "
                "du Japon en août, mais le 8 mai reste commémoré comme "
                "la fin des combats en Europe."
            ),
            "narrative": [
                "Fin avril 1945, l'Armée rouge encercle Berlin. Adolf "
                "Hitler se suicide dans son bunker le 30 avril, alors "
                "que les combats font rage dans les rues de la "
                "capitale allemande en ruines.",
                "Le 7 mai, le général Alfred Jodl signe à Reims, au "
                "quartier général du général Eisenhower, l'acte de "
                "capitulation sans conditions de toutes les forces "
                "allemandes. Staline, jugeant la cérémonie insuffisamment "
                "solennelle, exige une seconde signature.",
                "Dans la nuit du 8 au 9 mai, une nouvelle cérémonie se "
                "tient à Berlin-Karlshorst devant les représentants "
                "soviétiques. En France et dans la plupart des pays "
                "occidentaux, c'est le 8 mai qui reste célébré comme le "
                "jour de la victoire en Europe.",
            ],
            "why_it_matters": (
                "La capitulation allemande met fin à près de six ans "
                "de guerre en Europe, ayant fait des dizaines de "
                "millions de morts, et ouvre la voie à la partition de "
                "l'Allemagne et au début de la guerre froide."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "La capitulation sans conditions de l'Allemagne nazie, "
                "signée en deux temps à Reims puis à Berlin sous "
                "l'exigence soviétique, met fin à près de six ans de "
                "guerre en Europe et ouvre immédiatement la question de "
                "l'ordre d'après-guerre entre Alliés occidentaux et "
                "URSS."
            ),
            "before": (
                "Après le suicide d'Hitler dans son bunker le 30 avril "
                "1945, alors que Berlin encerclée par l'Armée rouge est "
                "en grande partie détruite par des combats de rue "
                "acharnés, l'effondrement militaire allemand devient "
                "total et incontestable, y compris pour les derniers "
                "partisans d'une résistance à outrance."
            ),
            "during": (
                "Une première capitulation, négociée par le général "
                "Alfred Jodl au nom du gouvernement Dönitz, est signée "
                "à Reims le 7 mai au quartier général d'Eisenhower ; "
                "jugeant cette cérémonie occidentale insuffisamment "
                "solennelle et voulant que l'acte soit signé sur le sol "
                "allemand face à l'Armée rouge, Staline exige et "
                "obtient une seconde cérémonie."
            ),
            "after": (
                "La guerre continue en Asie jusqu'à la capitulation du "
                "Japon en août, mais en Europe la date retenue pour la "
                "commémoration diverge déjà entre Occident (8 mai) et "
                "URSS puis Russie (9 mai, en raison du décalage "
                "horaire de la signature nocturne), symptôme précoce de "
                "la fracture qui deviendra la guerre froide."
            ),
            "narrative": [
                "Fin avril 1945, l'Armée rouge encercle et prend "
                "d'assaut Berlin au prix de combats de rue "
                "particulièrement meurtriers. Adolf Hitler se suicide "
                "dans son bunker le 30 avril, désignant l'amiral Dönitz "
                "comme son successeur.",
                "Le 7 mai, le général Alfred Jodl signe à Reims, au "
                "quartier général du général Eisenhower, l'acte de "
                "capitulation sans conditions de toutes les forces "
                "allemandes. Staline, jugeant la cérémonie occidentale "
                "insuffisamment solennelle et politiquement risquée "
                "pour la place de l'URSS dans la victoire, exige une "
                "seconde signature sur le sol allemand.",
                "Dans la nuit du 8 au 9 mai, une nouvelle cérémonie se "
                "tient à Berlin-Karlshorst devant les représentants "
                "soviétiques, en présence du maréchal Joukov. En France "
                "et dans la plupart des pays occidentaux, c'est le 8 "
                "mai qui reste célébré comme le jour de la victoire en "
                "Europe, tandis que l'URSS puis la Russie commémorent "
                "le 9 mai.",
            ],
            "why_it_matters": (
                "La capitulation allemande met fin à près de six ans "
                "de guerre en Europe, ayant fait des dizaines de "
                "millions de morts, et ouvre immédiatement la question "
                "de l'occupation et du partage de l'Allemagne entre "
                "quatre zones alliées — prélude direct à la partition "
                "du pays et au début de la guerre froide entre les "
                "Alliés occidentaux et l'URSS dès les mois suivants."
            ),
        },
    },
    "vol-de-gagarine": {
        "enfant": {
            "summary": (
                "Le 12 avril 1961, le Russe Youri Gagarine devient le "
                "premier être humain à voyager dans l'espace."
            ),
            "before": (
                "L'URSS et les États-Unis font la course pour être les "
                "premiers dans l'espace."
            ),
            "during": (
                "Gagarine fait un tour complet de la Terre à bord d'un "
                "vaisseau spatial, en moins de deux heures."
            ),
            "after": (
                "Il atterrit en parachute et devient un héros célébré "
                "dans le monde entier."
            ),
            "narrative": [
                "Le 12 avril 1961, le cosmonaute russe Youri Gagarine "
                "décolle à bord du vaisseau Vostok 1.",
                "En 108 minutes, il fait un tour complet de la Terre, "
                "à environ 300 km de hauteur. Il voit la Terre ronde de "
                "ses propres yeux, une première pour un humain.",
                "Il revient sur Terre en parachute et devient "
                "immédiatement un héros dans le monde entier.",
            ],
            "why_it_matters": (
                "Gagarine est le premier humain à aller dans l'espace. "
                "Cela relance la course vers la Lune, que les "
                "Américains atteindront huit ans plus tard."
            ),
        },
        "college": {
            "summary": (
                "Le cosmonaute soviétique Youri Gagarine devient le "
                "premier être humain à voyager dans l'espace, à bord "
                "du vaisseau Vostok 1."
            ),
            "before": (
                "En pleine guerre froide, l'URSS et les États-Unis se "
                "livrent à une course à l'espace acharnée depuis le "
                "lancement du satellite Spoutnik en 1957."
            ),
            "during": (
                "Gagarine effectue une orbite complète autour de la "
                "Terre à bord de Vostok 1, un vol d'un peu moins de "
                "deux heures, avant d'atterrir en parachute."
            ),
            "after": (
                "Gagarine devient un héros mondial, relançant la "
                "course à l'espace qui mènera les Américains sur la "
                "Lune huit ans plus tard."
            ),
            "narrative": [
                "Le 12 avril 1961, le cosmonaute soviétique Youri "
                "Gagarine, pilote de chasse de 27 ans, décolle de "
                "Baïkonour à bord du vaisseau Vostok 1.",
                "En 108 minutes, Gagarine effectue une orbite complète "
                "autour de la Terre à environ 300 km d'altitude, "
                "observant la courbure de la Terre, une vision alors "
                "inédite.",
                "Le vaisseau redescend et Gagarine s'éjecte pour "
                "atterrir en parachute. Il est immédiatement célébré "
                "comme un héros national.",
            ],
            "why_it_matters": (
                "Le vol de Gagarine constitue une victoire majeure de "
                "l'URSS dans la course à l'espace et pousse les "
                "États-Unis à accélérer leur propre programme spatial."
            ),
        },
        "lycee": {
            "summary": (
                "Le cosmonaute soviétique Youri Gagarine devient le "
                "premier être humain à voyager dans l'espace, à bord "
                "du vaisseau Vostok 1."
            ),
            "before": (
                "En pleine guerre froide, l'URSS et les États-Unis se "
                "livrent à une course à l'espace acharnée depuis le "
                "lancement du satellite Spoutnik en 1957."
            ),
            "during": (
                "Gagarine effectue une orbite complète autour de la "
                "Terre à bord de Vostok 1, un vol d'un peu moins de "
                "deux heures, avant d'atterrir en parachute en Russie."
            ),
            "after": (
                "Gagarine devient un héros mondial et un symbole de la "
                "propagande soviétique, relançant la course à l'espace "
                "qui mènera les Américains sur la Lune huit ans plus "
                "tard."
            ),
            "narrative": [
                "Le 12 avril 1961, le cosmonaute soviétique Youri "
                "Gagarine, un pilote de chasse de 27 ans, décolle du "
                "cosmodrome de Baïkonour à bord du vaisseau Vostok 1 "
                "pour devenir le premier être humain à quitter "
                "l'atmosphère terrestre.",
                "En 108 minutes, Gagarine effectue une orbite complète "
                "autour de la Terre à une altitude d'environ 300 "
                "kilomètres. Durant le vol, largement automatisé, il "
                "observe et décrit la courbure de la Terre, une vision "
                "alors inédite pour un être humain.",
                "Le vaisseau redescend et Gagarine s'éjecte pour "
                "atterrir en parachute près de la Volga, comme prévu "
                "par la procédure soviétique. Il est immédiatement "
                "célébré comme un héros national et devient une figure "
                "mondiale de la conquête spatiale.",
            ],
            "why_it_matters": (
                "Le vol de Gagarine constitue une victoire majeure de "
                "l'URSS dans la course à l'espace et pousse les "
                "États-Unis à accélérer leur propre programme spatial, "
                "qui aboutira à l'alunissage d'Apollo 11 en 1969."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Le cosmonaute soviétique Youri Gagarine devient, à "
                "bord de Vostok 1, le premier être humain à voyager "
                "dans l'espace, exploit largement automatisé par "
                "prudence médicale mais présenté par la propagande "
                "soviétique comme la démonstration éclatante de la "
                "supériorité du système communiste."
            ),
            "before": (
                "En pleine guerre froide, l'URSS et les États-Unis se "
                "livrent à une course à l'espace acharnée depuis le "
                "lancement du satellite Spoutnik en 1957, l'URSS "
                "conservant jusque-là une avance technologique que le "
                "programme Mercury américain, encore non habité, "
                "n'était pas parvenu à combler."
            ),
            "during": (
                "Gagarine effectue une orbite complète autour de la "
                "Terre à bord de Vostok 1, un vol d'un peu moins de "
                "deux heures dont les commandes de vol, par prudence "
                "médicale face à l'inconnu de l'apesanteur, restent "
                "verrouillées et ne peuvent être débloquées que par un "
                "code transmis depuis le sol, avant un atterrissage en "
                "parachute distinct de celui de la capsule."
            ),
            "after": (
                "Gagarine devient un héros mondial et un symbole "
                "diplomatique de premier plan pour l'URSS, relançant "
                "une course à l'espace qui mènera les Américains sur la "
                "Lune huit ans plus tard, en partie en réaction directe "
                "à ce succès soviétique."
            ),
            "narrative": [
                "Le 12 avril 1961, le cosmonaute soviétique Youri "
                "Gagarine, un pilote de chasse de 27 ans sélectionné "
                "parmi vingt candidats notamment pour sa petite taille "
                "adaptée à l'exiguïté de la capsule, décolle du "
                "cosmodrome de Baïkonour à bord du vaisseau Vostok 1 "
                "pour devenir le premier être humain à quitter "
                "l'atmosphère terrestre.",
                "En 108 minutes, Gagarine effectue une orbite complète "
                "autour de la Terre à une altitude d'environ 300 "
                "kilomètres. Durant le vol, entièrement automatisé par "
                "prudence médicale — les effets de l'apesanteur sur le "
                "jugement humain étant alors inconnus —, il observe et "
                "décrit la courbure de la Terre, une vision alors "
                "inédite pour un être humain.",
                "Le vaisseau redescend et Gagarine s'éjecte, comme "
                "prévu par la procédure soviétique, pour atterrir en "
                "parachute séparément de la capsule près de la Volga — "
                "un détail dissimulé pendant des années pour préserver "
                "l'homologation internationale du vol comme premier "
                "'atterrissage habité'. Il est immédiatement célébré "
                "comme un héros national et devient une figure mondiale "
                "de la conquête spatiale.",
            ],
            "why_it_matters": (
                "Le vol de Gagarine constitue une victoire majeure de "
                "l'URSS dans la course à l'espace, renforçant "
                "durablement son prestige diplomatique en pleine guerre "
                "froide, et pousse le président Kennedy, un mois plus "
                "tard, à fixer l'objectif d'un alunissage américain "
                "avant la fin de la décennie — objectif atteint avec "
                "Apollo 11 en 1969."
            ),
        },
    },
    "discours-i-have-a-dream": {
        "enfant": {
            "summary": (
                "Le 28 août 1963, Martin Luther King fait un discours "
                "très célèbre pour demander la fin du racisme aux "
                "États-Unis."
            ),
            "before": (
                "Aux États-Unis, les personnes noires n'ont pas les "
                "mêmes droits que les personnes blanches. Beaucoup de "
                "gens se battent contre cette injustice."
            ),
            "during": (
                "Devant plus de 200 000 personnes, Martin Luther King "
                "dit qu'il rêve d'un pays où tout le monde est traité "
                "pareil."
            ),
            "after": (
                "Ce discours aide à faire changer les lois contre le "
                "racisme aux États-Unis, quelques années plus tard."
            ),
            "narrative": [
                "Le 28 août 1963, plus de 200 000 personnes se "
                "rassemblent à Washington pour demander la fin du "
                "racisme.",
                "Devant le Lincoln Memorial, Martin Luther King fait un "
                "discours célèbre. Il dit qu'il rêve que ses enfants "
                "soient jugés sur leur caractère, pas sur la couleur de "
                "leur peau.",
                "Ce discours, vu à la télévision par des millions de "
                "gens, marque un grand moment pour les droits civiques "
                "aux États-Unis.",
            ],
            "why_it_matters": (
                "Ce discours reste un symbole très important de la "
                "lutte contre le racisme. Il a aidé à faire changer les "
                "lois l'année suivante."
            ),
        },
        "college": {
            "summary": (
                "Martin Luther King prononce son discours emblématique "
                "devant plus de 200 000 personnes, lors de la Marche "
                "sur Washington pour l'emploi et la liberté."
            ),
            "before": (
                "Le mouvement pour les droits civiques prend de "
                "l'ampleur aux États-Unis face à la ségrégation "
                "raciale persistante, notamment dans les États du Sud."
            ),
            "during": (
                "Devant le Lincoln Memorial, Martin Luther King "
                "prononce un discours appelant à la fin du racisme, "
                "culminant sur la formule « I have a dream »."
            ),
            "after": (
                "Le discours contribue à l'adoption du Civil Rights "
                "Act en 1964, interdisant la discrimination raciale "
                "légale aux États-Unis."
            ),
            "narrative": [
                "Le 28 août 1963, plus de 200 000 personnes se "
                "rassemblent à Washington pour la « Marche sur "
                "Washington », réclamant la fin de la ségrégation et "
                "l'égalité économique.",
                "Devant le Lincoln Memorial, le pasteur Martin Luther "
                "King prononce un discours qui restera l'un des plus "
                "célèbres du XXe siècle, développant une vision d'une "
                "Amérique sans discrimination raciale.",
                "Le discours, retransmis à la télévision devant des "
                "millions de téléspectateurs, marque un tournant dans "
                "la prise de conscience nationale sur les droits "
                "civiques.",
            ],
            "why_it_matters": (
                "Ce discours reste un symbole majeur du mouvement "
                "américain pour les droits civiques, qui aboutira au "
                "Civil Rights Act de 1964."
            ),
        },
        "lycee": {
            "summary": (
                "Martin Luther King prononce son discours emblématique "
                "devant plus de 200 000 personnes, lors de la Marche "
                "sur Washington pour l'emploi et la liberté."
            ),
            "before": (
                "Le mouvement pour les droits civiques prend de "
                "l'ampleur aux États-Unis face à la ségrégation "
                "raciale persistante, notamment dans les États du Sud "
                "où les lois « Jim Crow » restent en vigueur."
            ),
            "during": (
                "Devant le Lincoln Memorial, Martin Luther King "
                "prononce un discours appelant à la fin du racisme et "
                "à l'égalité entre Américains, culminant sur la "
                "formule « I have a dream »."
            ),
            "after": (
                "Le discours contribue à l'adoption du Civil Rights "
                "Act en 1964 et du Voting Rights Act en 1965, "
                "interdisant la discrimination raciale légale aux "
                "États-Unis."
            ),
            "narrative": [
                "Le 28 août 1963, plus de 200 000 personnes se "
                "rassemblent à Washington pour la « Marche sur "
                "Washington pour l'emploi et la liberté », réclamant "
                "la fin de la ségrégation raciale et l'égalité "
                "économique pour les Afro-Américains.",
                "Devant le Lincoln Memorial, le pasteur Martin Luther "
                "King prononce un discours qui restera l'un des plus "
                "célèbres du XXe siècle. S'écartant en partie de son "
                "texte préparé, il développe une vision d'une Amérique "
                "où ses enfants « ne seront pas jugés sur la couleur "
                "de leur peau mais sur le contenu de leur caractère ».",
                "Le discours, retransmis à la télévision devant des "
                "millions de téléspectateurs, marque un tournant dans "
                "la prise de conscience nationale sur les droits "
                "civiques aux États-Unis.",
            ],
            "why_it_matters": (
                "Ce discours reste un symbole majeur du mouvement "
                "américain pour les droits civiques, qui aboutira "
                "l'année suivante au Civil Rights Act de 1964 "
                "interdisant la discrimination raciale dans de "
                "nombreux domaines de la vie publique."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Martin Luther King prononce, en s'écartant largement "
                "de son texte préparé, son discours « I Have a Dream » "
                "devant plus de 200 000 personnes lors de la Marche sur "
                "Washington pour l'emploi et la liberté, moment fondateur "
                "de la mémoire collective du mouvement des droits "
                "civiques."
            ),
            "before": (
                "Le mouvement pour les droits civiques, structuré "
                "depuis le boycott des bus de Montgomery en 1955-56, "
                "prend une ampleur nationale face à la ségrégation "
                "raciale persistante dans les États du Sud sous le "
                "régime des lois « Jim Crow », et face à des violences "
                "policières de plus en plus médiatisées."
            ),
            "during": (
                "Devant le Lincoln Memorial, Martin Luther King "
                "prononce un discours dont la seconde partie, "
                "improvisée sur l'encouragement de la chanteuse Mahalia "
                "Jackson (« Tell them about the dream, Martin ! »), "
                "s'écarte du texte préparé pour culminer sur l'anaphore "
                "« I have a dream »."
            ),
            "after": (
                "Le discours, largement salué mais aussi critiqué par "
                "certains militants plus radicaux comme insuffisamment "
                "offensif, contribue néanmoins à l'adoption du Civil "
                "Rights Act en 1964 et du Voting Rights Act en 1965."
            ),
            "narrative": [
                "Le 28 août 1963, plus de 200 000 personnes se "
                "rassemblent à Washington pour la « Marche sur "
                "Washington pour l'emploi et la liberté », mobilisation "
                "organisée notamment par Bayard Rustin et A. Philip "
                "Randolph, réclamant la fin de la ségrégation raciale "
                "et l'égalité économique pour les Afro-Américains.",
                "Devant le Lincoln Memorial, le pasteur Martin Luther "
                "King prononce un discours qui restera l'un des plus "
                "célèbres du XXe siècle. Encouragé par la chanteuse "
                "gospel Mahalia Jackson à improviser, il s'écarte de "
                "son texte préparé pour développer, par l'anaphore « I "
                "have a dream », une vision d'une Amérique où ses "
                "enfants « ne seront pas jugés sur la couleur de leur "
                "peau mais sur le contenu de leur caractère ».",
                "Le discours, retransmis à la télévision devant des "
                "millions de téléspectateurs, marque un tournant dans "
                "la prise de conscience nationale, même si sa portée "
                "réelle sur l'administration Kennedy, alors hésitante, "
                "reste débattue par les historiens.",
            ],
            "why_it_matters": (
                "Ce discours reste un symbole majeur du mouvement "
                "américain pour les droits civiques, qui aboutira "
                "l'année suivante au Civil Rights Act de 1964 puis au "
                "Voting Rights Act de 1965, tout en illustrant les "
                "tensions internes du mouvement entre stratégie "
                "non-violente et appels à une action plus radicale, "
                "portés notamment par Malcolm X."
            ),
        },
    },
    "revolution-doctobre": {
        "enfant": {
            "summary": (
                "En novembre 1917, un groupe appelé les bolcheviks "
                "prend le pouvoir en Russie. C'est le début de l'Union "
                "soviétique."
            ),
            "before": (
                "La Russie est épuisée par la guerre. Le tsar (le roi "
                "russe) a déjà été renversé quelques mois avant."
            ),
            "during": (
                "Des soldats bolcheviks, menés par Lénine, prennent le "
                "palais où siège le gouvernement, presque sans "
                "combattre."
            ),
            "after": (
                "Lénine prend le pouvoir. Une guerre civile commence "
                "bientôt en Russie."
            ),
            "narrative": [
                "En 1917, la Russie est épuisée par la guerre et la "
                "famine. Le tsar a déjà été renversé quelques mois "
                "avant.",
                "Dans la nuit du 6 au 7 novembre 1917, des soldats "
                "bolcheviks, dirigés par Lénine, prennent facilement le "
                "contrôle de la ville de Petrograd, puis le Palais "
                "d'Hiver.",
                "Le lendemain, Lénine annonce la formation d'un nouveau "
                "gouvernement, dirigé par son parti.",
            ],
            "why_it_matters": (
                "Cette révolution crée le premier pays communiste du "
                "monde, l'URSS, qui va exister jusqu'en 1991."
            ),
        },
        "college": {
            "summary": (
                "Les bolcheviks de Lénine renversent le gouvernement "
                "provisoire russe lors d'une insurrection presque sans "
                "effusion de sang, ouvrant la voie au premier État "
                "communiste du monde."
            ),
            "before": (
                "Affaibli par la Première Guerre mondiale et la "
                "révolution de février 1917 qui a renversé le tsar, le "
                "gouvernement provisoire russe perd le soutien "
                "populaire."
            ),
            "during": (
                "Des gardes rouges bolcheviks s'emparent des points "
                "stratégiques de Petrograd puis prennent d'assaut le "
                "Palais d'Hiver, siège du gouvernement provisoire."
            ),
            "after": (
                "Lénine proclame un gouvernement soviétique ; une "
                "guerre civile éclate bientôt, menant à la fondation "
                "de l'URSS en 1922."
            ),
            "narrative": [
                "Après l'abdication du tsar Nicolas II en février "
                "1917, un gouvernement provisoire peine à s'imposer "
                "face à une population épuisée par la guerre, tandis "
                "que les bolcheviks de Lénine gagnent en influence.",
                "Dans la nuit du 6 au 7 novembre 1917 (« révolution "
                "d'Octobre » selon l'ancien calendrier russe), des "
                "gardes rouges occupent sans grande résistance les "
                "points stratégiques de Petrograd avant de prendre le "
                "Palais d'Hiver.",
                "Le lendemain, Lénine proclame la formation d'un "
                "gouvernement soviétique et annonce des décrets sur la "
                "paix et sur la terre.",
            ],
            "why_it_matters": (
                "La révolution d'Octobre installe le premier État "
                "communiste de l'histoire, qui deviendra l'URSS en "
                "1922."
            ),
        },
        "lycee": {
            "summary": (
                "Les bolcheviks de Lénine renversent le gouvernement "
                "provisoire russe lors d'une insurrection presque sans "
                "effusion de sang, ouvrant la voie au premier État "
                "communiste du monde."
            ),
            "before": (
                "Affaibli par la Première Guerre mondiale et la "
                "révolution de février 1917 qui a renversé le tsar, le "
                "gouvernement provisoire russe perd le soutien "
                "populaire face à la montée en influence des soviets."
            ),
            "during": (
                "Des gardes rouges bolcheviks s'emparent des points "
                "stratégiques de Petrograd puis prennent d'assaut le "
                "Palais d'Hiver, siège du gouvernement provisoire."
            ),
            "after": (
                "Lénine proclame un gouvernement soviétique ; une "
                "guerre civile éclate bientôt en Russie, menant à la "
                "fondation de l'URSS en 1922."
            ),
            "narrative": [
                "Après l'abdication du tsar Nicolas II en février "
                "1917, un gouvernement provisoire peine à s'imposer "
                "face à une population russe épuisée par la guerre et "
                "la famine, tandis que les soviets — conseils "
                "d'ouvriers et de soldats — gagnent en influence, "
                "notamment sous l'impulsion des bolcheviks de Vladimir "
                "Lénine.",
                "Dans la nuit du 6 au 7 novembre 1917 (24-25 octobre "
                "selon le calendrier julien alors en vigueur en "
                "Russie, d'où le nom de « révolution d'Octobre »), des "
                "gardes rouges bolcheviks occupent sans grande "
                "résistance les points stratégiques de Petrograd — "
                "gares, ponts, centrale téléphonique — avant de "
                "prendre d'assaut le Palais d'Hiver, siège du "
                "gouvernement provisoire.",
                "Le lendemain, Lénine proclame la formation d'un "
                "gouvernement soviétique et annonce des décrets "
                "immédiats sur la paix et sur la terre, cherchant à "
                "s'assurer le soutien des soldats et des paysans.",
            ],
            "why_it_matters": (
                "La révolution d'Octobre installe le premier État "
                "communiste de l'histoire, qui deviendra l'URSS en "
                "1922 et façonnera une grande partie de la géopolitique "
                "mondiale du XXe siècle, jusqu'à sa dissolution en "
                "1991."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Les bolcheviks de Lénine renversent, lors d'une "
                "insurrection soigneusement préparée mais presque sans "
                "effusion de sang, le gouvernement provisoire russe "
                "issu de la révolution de février, ouvrant la voie au "
                "premier État communiste de l'histoire."
            ),
            "before": (
                "Affaibli par la Première Guerre mondiale, une famine "
                "persistante et son incapacité à répondre aux "
                "revendications de paix, de terre et de pain, le "
                "gouvernement provisoire dirigé par Kerenski perd tout "
                "soutien populaire au profit des soviets, où les "
                "bolcheviks obtiennent la majorité à l'automne 1917."
            ),
            "during": (
                "Des gardes rouges bolcheviks, sur ordre d'un comité "
                "militaire révolutionnaire dirigé en coulisses par "
                "Trotski, s'emparent sans grande résistance des points "
                "stratégiques de Petrograd avant de prendre d'assaut le "
                "Palais d'Hiver, défendu par une garnison symbolique."
            ),
            "after": (
                "Lénine proclame un gouvernement soviétique et fait "
                "adopter dans la foulée les décrets sur la paix et sur "
                "la terre ; la dissolution de l'Assemblée constituante "
                "élue peu après, où les bolcheviks sont minoritaires, "
                "signale rapidement la nature autoritaire du nouveau "
                "régime, et une guerre civile éclate dès 1918."
            ),
            "narrative": [
                "Après l'abdication du tsar Nicolas II en février "
                "1917, un gouvernement provisoire dirigé par Kerenski "
                "peine à s'imposer face à une population russe épuisée "
                "par la guerre et la famine, tandis que les soviets — "
                "conseils d'ouvriers et de soldats — gagnent en "
                "influence, notamment sous l'impulsion des bolcheviks "
                "de Vladimir Lénine, de retour d'exil en avril.",
                "Dans la nuit du 6 au 7 novembre 1917 (24-25 octobre "
                "selon le calendrier julien alors en vigueur en "
                "Russie, d'où le nom de « révolution d'Octobre »), des "
                "gardes rouges bolcheviks, coordonnés par un comité "
                "militaire révolutionnaire que dirige en coulisses "
                "Léon Trotski, occupent sans grande résistance les "
                "points stratégiques de Petrograd avant de prendre "
                "d'assaut le Palais d'Hiver, faiblement défendu.",
                "Le lendemain, Lénine proclame la formation d'un "
                "gouvernement soviétique et annonce des décrets "
                "immédiats sur la paix et sur la terre. Quelques "
                "semaines plus tard, la dissolution manu militari de "
                "l'Assemblée constituante, où les bolcheviks n'obtiennent "
                "qu'une minorité des sièges lors des seules élections "
                "réellement libres de l'histoire soviétique, révèle "
                "d'emblée la nature autoritaire du nouveau pouvoir.",
            ],
            "why_it_matters": (
                "La révolution d'Octobre installe le premier État "
                "communiste de l'histoire, qui deviendra l'URSS en "
                "1922 et façonnera une grande partie de la géopolitique "
                "mondiale du XXe siècle — guerre froide, décolonisation, "
                "mouvements communistes internationaux — jusqu'à sa "
                "dissolution en 1991."
            ),
        },
    },
    "these-de-luther": {
        "enfant": {
            "summary": (
                "Le 31 octobre 1517, le moine Martin Luther affiche un "
                "texte critiquant l'Église catholique. C'est le début "
                "d'un grand changement religieux."
            ),
            "before": (
                "L'Église catholique vend des documents qui promettent "
                "de réduire les péchés des gens, en échange d'argent."
            ),
            "during": (
                "Martin Luther écrit 95 critiques contre cette "
                "pratique et les affiche sur la porte d'une église."
            ),
            "after": (
                "Son texte se répand très vite grâce à l'imprimerie et "
                "provoque une grande division dans l'Église."
            ),
            "narrative": [
                "Au XVIe siècle, l'Église catholique vend des "
                "« indulgences », des documents censés réduire les "
                "péchés en échange d'argent.",
                "Le 31 octobre 1517, le moine Martin Luther écrit 95 "
                "critiques contre cette pratique et les affiche, selon "
                "la légende, sur la porte d'une église à Wittenberg.",
                "Grâce à l'imprimerie, son texte se répand très vite en "
                "Allemagne et déclenche un grand débat religieux.",
            ],
            "why_it_matters": (
                "Cet événement est considéré comme le début de la "
                "Réforme protestante, qui va diviser la religion "
                "chrétienne en Europe."
            ),
        },
        "college": {
            "summary": (
                "Le moine Martin Luther affiche ses 95 thèses "
                "critiquant la vente des indulgences, un geste "
                "considéré comme le point de départ de la Réforme "
                "protestante."
            ),
            "before": (
                "L'Église catholique finance notamment la basilique "
                "Saint-Pierre de Rome par la vente d'indulgences, "
                "promettant la réduction des peines des péchés en "
                "échange d'argent."
            ),
            "during": (
                "Le moine augustin Martin Luther rédige 95 thèses "
                "contestant cette pratique et les affiche sur la porte "
                "de l'église du château de Wittenberg."
            ),
            "after": (
                "Le texte se diffuse rapidement grâce à l'imprimerie "
                "et déclenche une rupture religieuse majeure, menant à "
                "la naissance du protestantisme."
            ),
            "narrative": [
                "Au début du XVIe siècle, l'Église catholique autorise "
                "la vente d'indulgences pour financer notamment la "
                "basilique Saint-Pierre de Rome, ce qui scandalise le "
                "moine Martin Luther, professeur à Wittenberg.",
                "Le 31 octobre 1517, Luther rédige 95 thèses "
                "contestant la théologie des indulgences et les "
                "affiche, selon la tradition, sur la porte de l'église "
                "du château de Wittenberg.",
                "Grâce à l'imprimerie récemment développée par "
                "Gutenberg, le texte est rapidement diffusé dans tout "
                "le Saint-Empire, déclenchant un débat qui échappe vite "
                "au contrôle de l'Église romaine.",
            ],
            "why_it_matters": (
                "Cet acte est traditionnellement considéré comme le "
                "point de départ de la Réforme protestante, qui va "
                "diviser durablement le christianisme occidental."
            ),
        },
        "lycee": {
            "summary": (
                "Le moine Martin Luther affiche ses 95 thèses "
                "critiquant la vente des indulgences, un geste "
                "considéré comme le point de départ de la Réforme "
                "protestante."
            ),
            "before": (
                "L'Église catholique finance notamment la basilique "
                "Saint-Pierre de Rome par la vente d'indulgences, "
                "promettant la réduction des peines des péchés en "
                "échange d'argent, une pratique promue en Allemagne "
                "par le prédicateur Johann Tetzel."
            ),
            "during": (
                "Le moine augustin Martin Luther rédige 95 thèses "
                "théologiques contestant cette pratique et, selon la "
                "tradition, les affiche sur la porte de l'église du "
                "château de Wittenberg."
            ),
            "after": (
                "Le texte se diffuse rapidement grâce à l'imprimerie "
                "et déclenche une rupture religieuse majeure, menant à "
                "la naissance du protestantisme."
            ),
            "narrative": [
                "Au début du XVIe siècle, l'Église catholique autorise "
                "la vente d'indulgences pour financer notamment la "
                "construction de la basilique Saint-Pierre de Rome. Le "
                "prédicateur Johann Tetzel promeut cette pratique en "
                "Allemagne avec un zèle qui scandalise le moine "
                "augustin Martin Luther, professeur de théologie à "
                "Wittenberg.",
                "Le 31 octobre 1517, Luther rédige 95 thèses en latin "
                "contestant la théologie des indulgences et, selon la "
                "tradition la plus répandue, les affiche sur la porte "
                "de l'église du château de Wittenberg — un lieu qui "
                "servait aussi de tableau d'affichage universitaire.",
                "Grâce à l'imprimerie récemment développée par "
                "Gutenberg, le texte est rapidement traduit en allemand "
                "et diffusé dans tout le Saint-Empire, déclenchant un "
                "débat théologique qui échappe vite au contrôle de "
                "l'Église romaine.",
            ],
            "why_it_matters": (
                "Cet acte est traditionnellement considéré comme le "
                "point de départ de la Réforme protestante, qui va "
                "diviser durablement le christianisme occidental et "
                "bouleverser la carte religieuse et politique de "
                "l'Europe pour les siècles suivants."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Le moine augustin Martin Luther rédige et diffuse ses "
                "95 thèses critiquant la théologie des indulgences, "
                "geste devenu — non sans une part de reconstruction "
                "légendaire ultérieure — le symbole fondateur de la "
                "Réforme protestante."
            ),
            "before": (
                "L'Église catholique autorise la vente d'indulgences "
                "pour financer notamment la construction de la "
                "basilique Saint-Pierre de Rome, pratique que le "
                "prédicateur dominicain Johann Tetzel promeut en "
                "Allemagne avec un zèle commercial qui scandalise "
                "Luther, déjà engagé dans une réflexion théologique sur "
                "la justification par la foi seule."
            ),
            "during": (
                "Le 31 octobre 1517, Luther rédige en latin, à "
                "destination initiale d'un cercle académique et non du "
                "grand public, 95 thèses contestant la théologie des "
                "indulgences ; l'affichage sur la porte de l'église du "
                "château de Wittenberg, s'il correspond à un usage "
                "universitaire courant de l'époque, n'est attesté avec "
                "certitude que par un témoignage tardif de son "
                "collaborateur Melanchthon."
            ),
            "after": (
                "Traduit en allemand sans l'accord initial de Luther, "
                "le texte se diffuse en quelques semaines dans tout le "
                "Saint-Empire grâce à l'imprimerie, échappant "
                "rapidement au cadre du débat académique pour devenir "
                "une contestation ouverte de l'autorité pontificale, "
                "menant à l'excommunication de Luther en 1521."
            ),
            "narrative": [
                "Au début du XVIe siècle, l'Église catholique autorise "
                "la vente d'indulgences pour financer notamment la "
                "construction de la basilique Saint-Pierre de Rome. Le "
                "prédicateur dominicain Johann Tetzel promeut cette "
                "pratique en Allemagne avec un zèle commercial qui "
                "scandalise le moine augustin Martin Luther, professeur "
                "de théologie à Wittenberg, déjà engagé dans une "
                "réflexion sur la justification par la foi seule.",
                "Le 31 octobre 1517, Luther rédige en latin 95 thèses "
                "contestant la théologie des indulgences, initialement "
                "destinées à un débat académique plutôt qu'à une "
                "provocation publique. L'affichage sur la porte de "
                "l'église du château de Wittenberg, devenu l'image "
                "d'Épinal de l'événement, n'est en réalité attesté avec "
                "certitude que par un témoignage tardif de son "
                "collègue Melanchthon.",
                "Traduit en allemand sans l'accord initial de Luther, "
                "grâce à l'imprimerie récemment développée par "
                "Gutenberg, le texte se diffuse en quelques semaines "
                "dans tout le Saint-Empire, déclenchant un débat "
                "théologique qui échappe vite au contrôle de l'Église "
                "romaine et se transforme en contestation ouverte de "
                "l'autorité pontificale.",
            ],
            "why_it_matters": (
                "Cet acte est traditionnellement considéré comme le "
                "point de départ de la Réforme protestante, qui va "
                "diviser durablement le christianisme occidental et "
                "bouleverser la carte religieuse et politique de "
                "l'Europe pour les siècles suivants, des guerres de "
                "religion françaises à la guerre de Trente Ans."
            ),
        },
    },
    "liberation-mandela": {
        "enfant": {
            "summary": (
                "Le 11 février 1990, Nelson Mandela sort de prison "
                "après 27 ans. C'est le début de la fin de l'apartheid "
                "en Afrique du Sud."
            ),
            "before": (
                "Mandela est en prison depuis 1962 parce qu'il "
                "combattait l'apartheid, un système qui séparait les "
                "gens noirs et blancs."
            ),
            "during": (
                "Le président sud-africain de Klerk décide de libérer "
                "Mandela, qui sort de prison sous les applaudissements "
                "de la foule."
            ),
            "after": (
                "Mandela discute avec de Klerk pour mettre fin à "
                "l'apartheid. En 1994, il devient président."
            ),
            "narrative": [
                "Nelson Mandela est en prison depuis 1964 pour avoir "
                "combattu l'apartheid, un système injuste qui séparait "
                "les Noirs et les Blancs en Afrique du Sud.",
                "Le président Frederik de Klerk décide de changer les "
                "choses et de libérer Mandela.",
                "Le 11 février 1990, Mandela sort enfin de prison, "
                "acclamé par une foule immense et regardé par le monde "
                "entier.",
            ],
            "why_it_matters": (
                "Sa libération ouvre la voie à la fin de l'apartheid. "
                "En 1994, Mandela devient le premier président noir "
                "d'Afrique du Sud."
            ),
        },
        "college": {
            "summary": (
                "Après 27 ans d'emprisonnement, Nelson Mandela est "
                "libéré, marquant le début du démantèlement officiel "
                "du régime d'apartheid en Afrique du Sud."
            ),
            "before": (
                "Emprisonné depuis 1962 pour son opposition au régime "
                "ségrégationniste de l'apartheid, Mandela est devenu le "
                "symbole mondial de la lutte contre la discrimination "
                "raciale."
            ),
            "during": (
                "Sous la pression internationale croissante, le "
                "président Frederik de Klerk annonce la libération de "
                "Mandela, qui sort de prison le 11 février 1990."
            ),
            "after": (
                "Mandela négocie avec de Klerk la fin de l'apartheid, "
                "avant d'être élu premier président noir d'Afrique du "
                "Sud en 1994."
            ),
            "narrative": [
                "Condamné à la prison à vie en 1964, Nelson Mandela, "
                "dirigeant du Congrès national africain (ANC), devient "
                "pendant ses 27 années de détention le symbole mondial "
                "de la résistance à l'apartheid.",
                "Face à des sanctions internationales croissantes, le "
                "président Frederik de Klerk, arrivé au pouvoir en "
                "1989, amorce une politique de réformes.",
                "Le 11 février 1990, Nelson Mandela sort de prison sous "
                "les acclamations et une couverture médiatique "
                "mondiale, puis entame des négociations avec de Klerk.",
            ],
            "why_it_matters": (
                "La libération de Mandela ouvre la voie aux "
                "négociations qui mettront fin à l'apartheid et aux "
                "premières élections multiraciales de 1994."
            ),
        },
        "lycee": {
            "summary": (
                "Après 27 ans d'emprisonnement, Nelson Mandela est "
                "libéré, marquant le début du démantèlement officiel "
                "du régime d'apartheid en Afrique du Sud."
            ),
            "before": (
                "Emprisonné depuis 1962 pour son opposition au régime "
                "ségrégationniste de l'apartheid, Mandela est devenu le "
                "symbole mondial de la lutte contre la discrimination "
                "raciale en Afrique du Sud."
            ),
            "during": (
                "Sous la pression internationale croissante, le "
                "président sud-africain Frederik de Klerk annonce la "
                "libération de Mandela, qui sort de prison le 11 "
                "février 1990 sous les acclamations."
            ),
            "after": (
                "Mandela négocie avec de Klerk la fin de l'apartheid, "
                "avant d'être élu premier président noir d'Afrique du "
                "Sud lors des premières élections multiraciales de "
                "1994."
            ),
            "narrative": [
                "Condamné à la prison à vie en 1964 pour sabotage et "
                "complot contre l'État sud-africain, Nelson Mandela, "
                "dirigeant du Congrès national africain (ANC), devient "
                "pendant ses 27 années de détention le symbole mondial "
                "de la résistance au régime d'apartheid.",
                "Face à des sanctions économiques internationales "
                "croissantes et à une contestation interne grandissante, "
                "le président Frederik de Klerk, arrivé au pouvoir en "
                "1989, amorce une politique de réformes et lève "
                "l'interdiction frappant l'ANC.",
                "Le 11 février 1990, Nelson Mandela sort de la prison "
                "de Victor Verster, près du Cap, sous les acclamations "
                "de la foule et une couverture médiatique mondiale. Il "
                "entame aussitôt des négociations avec de Klerk pour "
                "démanteler l'apartheid.",
            ],
            "why_it_matters": (
                "La libération de Mandela ouvre la voie aux "
                "négociations qui mettront fin à l'apartheid et aux "
                "premières élections multiraciales de 1994, lors "
                "desquelles Mandela est élu président, devenant un "
                "symbole mondial de réconciliation."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Après 27 ans de détention, dont 18 sur l'île-bagne de "
                "Robben Island, Nelson Mandela est libéré à la suite de "
                "négociations secrètes entamées dès 1985, marquant le "
                "début du démantèlement officiel et négocié du régime "
                "d'apartheid."
            ),
            "before": (
                "Emprisonné depuis 1962 puis condamné à perpétuité en "
                "1964 pour son opposition au régime ségrégationniste de "
                "l'apartheid, Mandela devient, malgré son absence "
                "presque totale de représentation publique pendant "
                "près de trois décennies, le symbole mondial de la "
                "lutte contre la discrimination raciale."
            ),
            "during": (
                "Sous la pression conjuguée des sanctions économiques "
                "internationales, d'une contestation interne "
                "grandissante et de négociations secrètes déjà entamées "
                "avec Mandela lui-même depuis 1985, le président "
                "Frederik de Klerk, arrivé au pouvoir en 1989, lève "
                "l'interdiction frappant l'ANC et annonce la libération "
                "de Mandela sans conditions."
            ),
            "after": (
                "Mandela négocie avec de Klerk le démantèlement "
                "progressif de l'apartheid, aboutissant en 1993 au "
                "partage du prix Nobel de la paix entre les deux hommes "
                "puis, en 1994, à son élection comme premier président "
                "noir d'Afrique du Sud lors des premières élections "
                "multiraciales."
            ),
            "narrative": [
                "Condamné à la prison à vie en 1964 pour sabotage et "
                "complot contre l'État sud-africain, Nelson Mandela, "
                "dirigeant du Congrès national africain (ANC), devient "
                "pendant ses 27 années de détention — dont 18 passées "
                "sur l'île-bagne de Robben Island — le symbole mondial "
                "de la résistance au régime d'apartheid, malgré une "
                "quasi-absence d'image ou de parole publique pendant "
                "cette période.",
                "Face à des sanctions économiques internationales "
                "croissantes et à une contestation interne "
                "grandissante, le président Frederik de Klerk, arrivé "
                "au pouvoir en 1989 et déjà engagé dans des discussions "
                "confidentielles avec Mandela depuis plusieurs années, "
                "lève l'interdiction frappant l'ANC et le parti "
                "communiste sud-africain début février 1990.",
                "Le 11 février 1990, Nelson Mandela sort de la prison "
                "de Victor Verster, près du Cap, sous les acclamations "
                "de la foule et une couverture médiatique mondiale sans "
                "précédent. Il entame aussitôt des négociations "
                "complexes et souvent tendues avec de Klerk pour "
                "démanteler l'apartheid par voie légale.",
            ],
            "why_it_matters": (
                "La libération de Mandela ouvre la voie à quatre "
                "années de négociations souvent périlleuses — marquées "
                "par des violences politiques considérables — qui "
                "mettront fin à l'apartheid et aux premières élections "
                "multiraciales de 1994, lors desquelles Mandela est élu "
                "président, devenant un symbole mondial de "
                "réconciliation malgré les tensions économiques et "
                "sociales que l'apartheid laissera durablement en "
                "héritage."
            ),
        },
    },
    "lancement-spoutnik": {
        "enfant": {
            "summary": (
                "Le 4 octobre 1957, l'URSS envoie dans l'espace le "
                "premier satellite du monde, Spoutnik 1."
            ),
            "before": (
                "L'URSS et les États-Unis sont en compétition pour "
                "construire des fusées."
            ),
            "during": (
                "Une fusée soviétique envoie dans l'espace une boule "
                "de métal qui émet un petit signal radio."
            ),
            "after": (
                "Les Américains ont très peur d'être en retard. Ils "
                "créent la NASA l'année suivante."
            ),
            "narrative": [
                "Le 4 octobre 1957, l'URSS lance Spoutnik 1, une "
                "petite boule de métal de 58 centimètres avec quatre "
                "antennes.",
                "Une fois dans l'espace, le satellite envoie juste un "
                "petit signal radio, un « bip-bip » que des gens du "
                "monde entier peuvent entendre.",
                "Aux États-Unis, c'est un choc énorme : ils ont peur "
                "d'être en retard sur les Soviétiques.",
            ],
            "why_it_matters": (
                "Spoutnik marque le début de la conquête spatiale, qui "
                "mènera plus tard les hommes sur la Lune."
            ),
        },
        "college": {
            "summary": (
                "L'URSS met sur orbite Spoutnik 1, premier satellite "
                "artificiel de l'histoire, déclenchant la course à "
                "l'espace avec les États-Unis."
            ),
            "before": (
                "En pleine guerre froide, l'URSS et les États-Unis "
                "développent chacun des programmes de fusées, "
                "initialement à but militaire."
            ),
            "during": (
                "Une fusée soviétique R-7 place en orbite Spoutnik 1, "
                "une sphère métallique de 58 centimètres émettant un "
                "simple signal radio."
            ),
            "after": (
                "La nouvelle provoque un choc aux États-Unis, qui "
                "créent la NASA l'année suivante."
            ),
            "narrative": [
                "Le 4 octobre 1957, l'URSS lance depuis Baïkonour une "
                "fusée R-7 emportant Spoutnik 1, une sphère métallique "
                "polie de 58 centimètres équipée de quatre antennes.",
                "Une fois en orbite, le satellite émet un simple signal "
                "radio régulier, captable par des radioamateurs du "
                "monde entier.",
                "Aux États-Unis, la nouvelle provoque une onde de choc "
                "connue sous le nom de « moment Spoutnik » : le pays "
                "craint d'avoir pris du retard technologique.",
            ],
            "why_it_matters": (
                "Spoutnik 1 marque le début de l'ère spatiale, qui "
                "aboutira à la création de la NASA en 1958 et à "
                "l'alunissage d'Apollo 11 en 1969."
            ),
        },
        "lycee": {
            "summary": (
                "L'URSS met sur orbite Spoutnik 1, premier satellite "
                "artificiel de l'histoire, déclenchant la course à "
                "l'espace avec les États-Unis."
            ),
            "before": (
                "En pleine guerre froide, l'URSS et les États-Unis "
                "développent chacun des programmes de fusées, "
                "initialement à but militaire, capables d'atteindre "
                "l'espace."
            ),
            "during": (
                "Une fusée soviétique R-7 place en orbite Spoutnik 1, "
                "une sphère métallique de 58 centimètres émettant un "
                "simple signal radio régulier."
            ),
            "after": (
                "La nouvelle provoque un choc aux États-Unis, qui "
                "créent la NASA l'année suivante et accélèrent leur "
                "propre programme spatial."
            ),
            "narrative": [
                "Le 4 octobre 1957, l'Union soviétique lance depuis le "
                "cosmodrome de Baïkonour une fusée R-7 emportant "
                "Spoutnik 1, une sphère métallique polie d'à peine 58 "
                "centimètres de diamètre équipée de quatre antennes "
                "radio.",
                "Une fois en orbite, le satellite se contente d'émettre "
                "un signal radio simple et régulier, un « bip-bip » "
                "captable par des radioamateurs du monde entier, "
                "preuve manifeste de la réussite soviétique.",
                "Aux États-Unis, la nouvelle provoque une onde de choc "
                "connue sous le nom de « moment Spoutnik » : l'opinion "
                "publique et le gouvernement américains, pris de "
                "court, craignent d'avoir pris du retard technologique "
                "et militaire sur l'URSS.",
            ],
            "why_it_matters": (
                "Spoutnik 1 marque le début de l'ère spatiale et de la "
                "course à l'espace entre les États-Unis et l'URSS, qui "
                "aboutira notamment à la création de la NASA en 1958 "
                "et, onze ans plus tard, à l'alunissage d'Apollo 11."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "L'URSS met sur orbite Spoutnik 1, premier objet "
                "artificiel de l'histoire humaine à quitter "
                "l'atmosphère terrestre, déclenchant un « moment "
                "Spoutnik » qui redéfinit durablement la perception "
                "américaine de son avance technologique."
            ),
            "before": (
                "En pleine guerre froide, l'URSS et les États-Unis "
                "développent chacun, sur la base de technologies de "
                "missiles balistiques intercontinentaux à visée "
                "militaire, des programmes capables d'atteindre "
                "l'espace, dans un contexte d'Année géophysique "
                "internationale (1957-58) que les deux camps "
                "cherchaient à marquer scientifiquement."
            ),
            "during": (
                "Une fusée soviétique R-7 — initialement conçue comme "
                "missile balistique intercontinental — place en orbite "
                "Spoutnik 1, sphère métallique de 58 centimètres dont "
                "la simplicité technique délibérée (un simple émetteur "
                "radio) permettait une mise au point rapide."
            ),
            "after": (
                "La nouvelle provoque un choc politique et culturel "
                "considérable aux États-Unis, qui créent la NASA "
                "l'année suivante, réforment leur enseignement "
                "scientifique via le National Defense Education Act, "
                "et accélèrent leur propre programme spatial jusqu'à "
                "l'objectif lunaire fixé par Kennedy en 1961."
            ),
            "narrative": [
                "Le 4 octobre 1957, l'Union soviétique lance depuis le "
                "cosmodrome de Baïkonour une fusée R-7 — à l'origine "
                "conçue comme missile balistique intercontinental — "
                "emportant Spoutnik 1, une sphère métallique polie "
                "d'à peine 58 centimètres de diamètre équipée de "
                "quatre antennes radio.",
                "Une fois en orbite, le satellite se contente d'émettre "
                "un signal radio simple et régulier, un « bip-bip » "
                "captable par des radioamateurs du monde entier — une "
                "simplicité technique délibérée, gage de rapidité de "
                "développement plus que de sophistication scientifique.",
                "Aux États-Unis, la nouvelle provoque une onde de choc "
                "connue sous le nom de « moment Spoutnik » : l'opinion "
                "publique et le gouvernement américains, pris de "
                "court, craignent d'avoir pris du retard technologique "
                "et militaire sur l'URSS, un choc amplifié par l'échec "
                "retentissant et télévisé du lancement du satellite "
                "américain Vanguard TV3 deux mois plus tard.",
            ],
            "why_it_matters": (
                "Spoutnik 1 marque le début de l'ère spatiale et de la "
                "course à l'espace entre les États-Unis et l'URSS, "
                "provoquant une refonte en profondeur de la politique "
                "scientifique et éducative américaine et aboutissant "
                "notamment à la création de la NASA en 1958 puis, onze "
                "ans plus tard, à l'alunissage d'Apollo 11."
            ),
        },
    },
    "chute-empire-romain-occident": {
        "enfant": {
            "summary": (
                "En 476, un chef appelé Odoacre renverse le dernier "
                "empereur romain d'Occident. C'est souvent considéré "
                "comme la fin de l'Antiquité."
            ),
            "before": (
                "L'Empire romain d'Occident est très affaibli depuis "
                "longtemps, à cause de nombreuses invasions."
            ),
            "during": (
                "Odoacre, un chef militaire, renverse le jeune "
                "empereur Romulus Augustule sans grande bataille."
            ),
            "after": (
                "Odoacre devient roi d'Italie. Il n'y aura plus "
                "d'empereur romain en Occident."
            ),
            "narrative": [
                "Au Ve siècle, l'Empire romain d'Occident est très "
                "affaibli par des invasions répétées.",
                "En 476, Odoacre, un chef militaire d'origine "
                "germanique, renverse le jeune empereur Romulus "
                "Augustule et se proclame roi d'Italie.",
                "Odoacre ne se déclare pas empereur lui-même. C'est la "
                "fin de la lignée des empereurs romains d'Occident.",
            ],
            "why_it_matters": (
                "Cet événement est souvent considéré comme la fin de "
                "l'Antiquité et le début du Moyen Âge en Europe."
            ),
        },
        "college": {
            "summary": (
                "Le chef germanique Odoacre dépose le dernier empereur "
                "romain d'Occident, Romulus Augustule, marquant "
                "traditionnellement la fin de l'Antiquité en Europe."
            ),
            "before": (
                "Affaibli par des décennies d'invasions et de crises, "
                "l'Empire romain d'Occident ne contrôle plus qu'une "
                "fraction de son territoire d'origine."
            ),
            "during": (
                "Le chef militaire germanique Odoacre renverse le "
                "jeune empereur Romulus Augustule et se proclame roi "
                "d'Italie, sans nommer de nouvel empereur."
            ),
            "after": (
                "Odoacre renvoie les insignes impériaux à "
                "Constantinople, laissant l'empereur d'Orient seul "
                "héritier officiel du titre impérial."
            ),
            "narrative": [
                "Au Ve siècle, l'Empire romain d'Occident est exsangue "
                ": invasions germaniques répétées, généraux qui font et "
                "défont les empereurs à leur guise.",
                "En 476, Odoacre, chef militaire d'origine germanique, "
                "se retourne contre le pouvoir impérial. Il dépose "
                "Romulus Augustule sans effusion de sang notable et se "
                "proclame roi d'Italie.",
                "Plutôt que de se proclamer empereur, Odoacre renvoie "
                "les insignes impériaux à Constantinople, reconnaissant "
                "l'empereur d'Orient comme seul souverain légitime.",
            ],
            "why_it_matters": (
                "Cet événement est conventionnellement retenu comme la "
                "date de la fin de l'Empire romain d'Occident et de "
                "l'Antiquité."
            ),
        },
        "lycee": {
            "summary": (
                "Le chef germanique Odoacre dépose le dernier empereur "
                "romain d'Occident, Romulus Augustule, marquant "
                "traditionnellement la fin de l'Antiquité en Europe."
            ),
            "before": (
                "Affaibli par des décennies d'invasions, de crises "
                "économiques et de coups d'État militaires, l'Empire "
                "romain d'Occident ne contrôle plus qu'une fraction de "
                "son territoire d'origine."
            ),
            "during": (
                "Le chef militaire germanique Odoacre renverse le "
                "jeune empereur Romulus Augustule et se proclame roi "
                "d'Italie, sans nommer de nouvel empereur."
            ),
            "after": (
                "Odoacre renvoie les insignes impériaux à "
                "Constantinople, laissant l'empereur d'Orient seul "
                "héritier officiel du titre impérial romain."
            ),
            "narrative": [
                "Au Ve siècle, l'Empire romain d'Occident est exsangue "
                ": invasions germaniques répétées, généraux qui font et "
                "défont les empereurs à leur guise, économie exsangue. "
                "Le dernier empereur, Romulus Augustule, n'a que "
                "quelques mois de règne, porté au pouvoir enfant par "
                "son propre père.",
                "En 476, Odoacre, chef militaire d'origine germanique "
                "à la tête de troupes fédérées au service de Rome, se "
                "retourne contre le pouvoir impérial après le refus de "
                "lui accorder des terres en Italie. Il dépose Romulus "
                "Augustule sans effusion de sang notable et se "
                "proclame roi d'Italie.",
                "Plutôt que de se faire proclamer empereur à son tour, "
                "Odoacre renvoie les insignes impériaux à "
                "Constantinople, reconnaissant symboliquement "
                "l'empereur d'Orient, Zénon, comme seul souverain "
                "légitime — mettant ainsi fin à la lignée des "
                "empereurs d'Occident.",
            ],
            "why_it_matters": (
                "Cet événement est conventionnellement retenu par les "
                "historiens comme la date de la fin de l'Empire romain "
                "d'Occident et de l'Antiquité, ouvrant la période du "
                "Moyen Âge en Europe occidentale."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Le chef militaire germanique Odoacre dépose le "
                "dernier empereur romain d'Occident, Romulus Augustule "
                "— un événement que l'historiographie moderne nuance "
                "de plus en plus, y voyant davantage une transition "
                "administrative progressive qu'une rupture brutale."
            ),
            "before": (
                "Affaibli par des décennies d'invasions germaniques, "
                "de crises économiques et de coups d'État militaires "
                "récurrents depuis le début du Ve siècle, l'Empire "
                "romain d'Occident ne contrôle plus, en 476, qu'une "
                "fraction de son territoire d'origine, essentiellement "
                "l'Italie."
            ),
            "during": (
                "Le chef militaire germanique Odoacre, à la tête de "
                "troupes fédérées mécontentes de ne pas recevoir les "
                "terres promises, renverse le jeune empereur Romulus "
                "Augustule — lui-même usurpateur installé quelques "
                "mois plus tôt par son père — et se proclame roi "
                "d'Italie sans nommer de nouvel empereur."
            ),
            "after": (
                "Odoacre renvoie les insignes impériaux à "
                "Constantinople et se fait reconnaître comme patrice "
                "par l'empereur d'Orient Zénon, gouvernant de facto "
                "l'Italie en position de souverain autonome tout en "
                "maintenant une fiction de continuité administrative "
                "romaine."
            ),
            "narrative": [
                "Au Ve siècle, l'Empire romain d'Occident est exsangue "
                ": invasions germaniques répétées, généraux qui font et "
                "défont les empereurs à leur guise, économie exsangue. "
                "Le dernier empereur, Romulus Augustule, usurpateur "
                "jamais reconnu par Constantinople, n'a que quelques "
                "mois de règne, porté au pouvoir enfant par son propre "
                "père, le général Oreste.",
                "En 476, Odoacre, chef militaire d'origine germanique "
                "à la tête de troupes fédérées au service de Rome, se "
                "retourne contre le pouvoir impérial après le refus "
                "d'Oreste de lui accorder des terres en Italie promises "
                "en échange de services militaires. Il dépose Romulus "
                "Augustule sans effusion de sang notable et se proclame "
                "roi d'Italie.",
                "Plutôt que de se faire proclamer empereur à son tour, "
                "Odoacre renvoie les insignes impériaux à "
                "Constantinople, reconnaissant symboliquement "
                "l'empereur d'Orient, Zénon, comme seul souverain "
                "légitime, tout en obtenant de lui le titre de patrice "
                "— une manœuvre politique qui préserve une continuité "
                "institutionnelle formelle malgré la rupture de fait.",
            ],
            "why_it_matters": (
                "Cet événement est conventionnellement retenu par "
                "l'historiographie traditionnelle comme la date de la "
                "fin de l'Empire romain d'Occident et de l'Antiquité, "
                "bien que les historiens contemporains, à la suite "
                "notamment de Peter Brown, tendent à y voir davantage "
                "une étape d'un long processus de transformation "
                "romano-germanique que la rupture brutale longtemps "
                "enseignée."
            ),
        },
    },
    "invention-machine-vapeur-watt": {
        "enfant": {
            "summary": (
                "En 1769, l'ingénieur écossais James Watt invente une "
                "machine à vapeur bien meilleure. C'est le début de "
                "grandes usines en Europe."
            ),
            "before": (
                "Les machines à vapeur qui existaient déjà gaspillaient "
                "beaucoup d'énergie."
            ),
            "during": (
                "James Watt trouve un moyen d'améliorer beaucoup la "
                "machine à vapeur."
            ),
            "after": (
                "Ses machines sont utilisées dans les mines puis dans "
                "les usines, partout en Angleterre."
            ),
            "narrative": [
                "Dans les années 1760, l'ingénieur écossais James Watt "
                "répare une vieille machine à vapeur utilisée pour "
                "pomper l'eau des mines.",
                "Il remarque qu'elle gaspille beaucoup d'énergie. Il "
                "invente une nouvelle pièce qui améliore beaucoup son "
                "efficacité.",
                "Le 5 janvier 1769, il dépose le brevet de son "
                "invention. Plus tard, ses machines se répandent dans "
                "les usines.",
            ],
            "why_it_matters": (
                "L'invention de Watt aide à démarrer la révolution "
                "industrielle, qui change complètement la façon de "
                "travailler et de vivre."
            ),
        },
        "college": {
            "summary": (
                "L'ingénieur écossais James Watt dépose le brevet de "
                "sa machine à vapeur perfectionnée, une innovation "
                "décisive pour la révolution industrielle."
            ),
            "before": (
                "Les machines à vapeur existantes, comme celle de "
                "Newcomen, sont peu efficaces énergétiquement et "
                "limitées au pompage de l'eau dans les mines."
            ),
            "during": (
                "James Watt met au point un condenseur séparé qui "
                "améliore radicalement le rendement de la machine à "
                "vapeur, et en dépose le brevet."
            ),
            "after": (
                "Associé à l'industriel Matthew Boulton, Watt "
                "commercialise ses machines, qui se répandent dans les "
                "mines puis les usines textiles."
            ),
            "narrative": [
                "Dans les années 1760, James Watt travaille comme "
                "réparateur d'instruments à Glasgow, où on lui confie "
                "une machine à vapeur de Newcomen.",
                "Watt remarque qu'elle gaspille énormément d'énergie. "
                "Il conçoit un condenseur séparé, qui améliore "
                "considérablement le rendement.",
                "Le 5 janvier 1769, Watt dépose son brevet. Associé à "
                "Matthew Boulton, ses machines se répandent rapidement "
                "dans les mines puis les usines britanniques.",
            ],
            "why_it_matters": (
                "L'amélioration de la machine à vapeur par Watt est "
                "considérée comme l'un des déclencheurs majeurs de la "
                "révolution industrielle."
            ),
        },
        "lycee": {
            "summary": (
                "L'ingénieur écossais James Watt dépose le brevet de "
                "sa machine à vapeur perfectionnée, une innovation "
                "décisive qui va déclencher la révolution industrielle."
            ),
            "before": (
                "Les machines à vapeur existantes, comme celle de "
                "Newcomen, sont peu efficaces énergétiquement et "
                "limitées au pompage de l'eau dans les mines."
            ),
            "during": (
                "James Watt met au point un condenseur séparé qui "
                "améliore radicalement le rendement de la machine à "
                "vapeur, et en dépose le brevet."
            ),
            "after": (
                "Associé à l'industriel Matthew Boulton, Watt "
                "commercialise ses machines, qui se répandent dans les "
                "mines puis les usines textiles, propulsant la "
                "révolution industrielle britannique."
            ),
            "narrative": [
                "Dans les années 1760, l'ingénieur écossais James Watt "
                "travaille comme réparateur d'instruments à "
                "l'université de Glasgow, où on lui confie la "
                "réparation d'un modèle de machine à vapeur de "
                "Newcomen, utilisée pour pomper l'eau des mines.",
                "Watt remarque que la machine gaspille énormément "
                "d'énergie en refroidissant puis en réchauffant sans "
                "cesse le même cylindre. Il conçoit un condenseur "
                "séparé, permettant de maintenir le cylindre principal "
                "chaud en permanence, ce qui améliore considérablement "
                "le rendement énergétique.",
                "Le 5 janvier 1769, Watt dépose le brevet de son "
                "invention. Faute de moyens pour l'exploiter seul, il "
                "s'associe quelques années plus tard à l'industriel "
                "Matthew Boulton, et leurs machines à vapeur "
                "perfectionnées se répandent rapidement dans les mines "
                "puis les usines textiles britanniques.",
            ],
            "why_it_matters": (
                "L'amélioration de la machine à vapeur par Watt est "
                "considérée comme l'un des déclencheurs majeurs de la "
                "révolution industrielle, en fournissant une source "
                "d'énergie mécanique fiable qui transformera profondément "
                "l'économie et la société des XVIIIe et XIXe siècles."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "L'ingénieur écossais James Watt dépose le brevet de "
                "sa machine à vapeur à condenseur séparé, innovation "
                "qui ne prend son plein essor économique qu'une "
                "quinzaine d'années plus tard grâce à son association "
                "avec l'industriel Matthew Boulton, et qui devient l'un "
                "des symboles de la révolution industrielle."
            ),
            "before": (
                "Les machines à vapeur existantes, notamment celle de "
                "Newcomen inventée en 1712, sont peu efficaces "
                "énergétiquement et limitées au pompage de l'eau dans "
                "les mines de charbon, leur rendement thermique "
                "dépassant à peine 1 %."
            ),
            "during": (
                "James Watt, ayant identifié lors de la réparation "
                "d'un modèle de Newcomen que l'essentiel de l'énergie "
                "se perdait à réchauffer puis refroidir sans cesse le "
                "même cylindre, met au point un condenseur séparé "
                "maintenu froid en permanence tandis que le cylindre "
                "principal reste chaud, et en dépose le brevet."
            ),
            "after": (
                "Faute de capital pour exploiter seul son invention, "
                "Watt ne parvient à la commercialiser efficacement "
                "qu'après son association avec l'industriel Matthew "
                "Boulton à Birmingham en 1775 ; leurs machines "
                "perfectionnées, capables ensuite de produire un "
                "mouvement rotatif et non plus seulement un pompage, se "
                "répandent dans les mines puis les usines textiles."
            ),
            "narrative": [
                "Dans les années 1760, l'ingénieur écossais James Watt "
                "travaille comme réparateur d'instruments à "
                "l'université de Glasgow, où on lui confie la "
                "réparation d'un modèle de machine à vapeur de "
                "Newcomen, utilisée depuis 1712 pour pomper l'eau des "
                "mines mais au rendement thermique dérisoire.",
                "Watt remarque que la machine gaspille énormément "
                "d'énergie en refroidissant puis en réchauffant sans "
                "cesse le même cylindre. Il conçoit un condenseur "
                "séparé, maintenu froid en permanence pendant que le "
                "cylindre principal reste chaud, ce qui améliore "
                "considérablement le rendement énergétique — une idée "
                "qui lui serait venue, selon la légende, lors d'une "
                "promenade dominicale.",
                "Le 5 janvier 1769, Watt dépose le brevet de son "
                "invention, mais faute de moyens financiers pour "
                "l'exploiter, il lui faudra attendre 1775 et son "
                "association avec l'industriel Matthew Boulton à "
                "Birmingham pour commercialiser à grande échelle des "
                "machines à vapeur perfectionnées, bientôt capables "
                "d'entraîner un mouvement rotatif utilisable dans les "
                "usines textiles.",
            ],
            "why_it_matters": (
                "L'amélioration de la machine à vapeur par Watt est "
                "considérée comme l'un des déclencheurs majeurs de la "
                "révolution industrielle, en fournissant une source "
                "d'énergie mécanique fiable et transportable qui "
                "affranchira la production industrielle de sa "
                "dépendance aux cours d'eau, transformant profondément "
                "l'économie, l'urbanisation et la société des XVIIIe "
                "et XIXe siècles."
            ),
        },
    },
    "siege-de-bagdad-1258": {
        "enfant": {
            "summary": (
                "En 1258, l'armée mongole détruit la ville de Bagdad, "
                "qui était un grand centre du savoir dans le monde "
                "musulman."
            ),
            "before": (
                "Bagdad est depuis très longtemps une ville pleine de "
                "savants, de livres et de bibliothèques."
            ),
            "during": (
                "L'armée mongole d'Hulagu Khan attaque et détruit la "
                "ville en moins de deux semaines."
            ),
            "after": (
                "Les bibliothèques sont brûlées, beaucoup d'habitants "
                "sont tués. C'est un grand coup pour le savoir dans le "
                "monde musulman."
            ),
            "narrative": [
                "Bagdad est depuis longtemps une grande ville de "
                "savants, avec d'immenses bibliothèques.",
                "En 1258, l'armée mongole d'Hulagu Khan attaque la "
                "ville. Après moins de deux semaines, les défenses "
                "tombent.",
                "La destruction est terrible : les bibliothèques sont "
                "brûlées, beaucoup d'habitants meurent, et le chef de "
                "la ville est tué.",
            ],
            "why_it_matters": (
                "Cette destruction met fin à une longue période où "
                "Bagdad était un des plus grands centres du savoir au "
                "monde."
            ),
        },
        "college": {
            "summary": (
                "L'armée mongole d'Hulagu Khan met à sac Bagdad, "
                "capitale du califat abbasside, mettant fin à cinq "
                "siècles d'âge d'or intellectuel du monde musulman."
            ),
            "before": (
                "Bagdad est depuis le VIIIe siècle le cœur "
                "intellectuel du monde musulman, abritant la Maison de "
                "la Sagesse et d'immenses bibliothèques."
            ),
            "during": (
                "Après un siège de moins de deux semaines, les troupes "
                "mongoles d'Hulagu Khan, petit-fils de Gengis Khan, "
                "percent les défenses et pillent la ville."
            ),
            "after": (
                "Le dernier calife abbasside est exécuté, la ville "
                "est largement détruite, marquant la fin du califat "
                "abbasside."
            ),
            "narrative": [
                "Depuis sa fondation au VIIIe siècle, Bagdad est la "
                "capitale du califat abbasside et l'un des plus grands "
                "centres intellectuels du monde, abritant la Maison de "
                "la Sagesse.",
                "En 1258, Hulagu Khan, petit-fils de Gengis Khan, mène "
                "une armée mongole jusqu'aux portes de Bagdad. Le "
                "siège dure moins de deux semaines : le 10 février, "
                "les défenses cèdent.",
                "Le sac de Bagdad qui suit est d'une violence extrême "
                ": des centaines de milliers d'habitants sont tués, les "
                "bibliothèques incendiées. Le calife est exécuté "
                "quelques jours plus tard.",
            ],
            "why_it_matters": (
                "La destruction de Bagdad met fin à cinq siècles d'âge "
                "d'or intellectuel abbasside et marque un tournant "
                "dans le déclin scientifique du monde musulman "
                "médiéval."
            ),
        },
        "lycee": {
            "summary": (
                "L'armée mongole d'Hulagu Khan met à sac Bagdad, "
                "capitale du califat abbasside, mettant fin à cinq "
                "siècles d'âge d'or intellectuel du monde musulman."
            ),
            "before": (
                "Bagdad est depuis le VIIIe siècle le cœur "
                "intellectuel et culturel du monde musulman, abritant "
                "la Maison de la Sagesse et d'immenses bibliothèques."
            ),
            "during": (
                "Après un siège de moins de deux semaines, les troupes "
                "mongoles d'Hulagu Khan, petit-fils de Gengis Khan, "
                "percent les défenses et pillent systématiquement la "
                "ville."
            ),
            "after": (
                "Le dernier calife abbasside est exécuté, la ville "
                "est largement détruite et sa population décimée, "
                "marquant la fin du califat abbasside."
            ),
            "narrative": [
                "Depuis sa fondation au VIIIe siècle, Bagdad est la "
                "capitale du califat abbasside et l'un des plus grands "
                "centres intellectuels du monde, abritant la Maison de "
                "la Sagesse où savants et traducteurs préservent et "
                "enrichissent le savoir grec, perse et indien.",
                "En 1258, Hulagu Khan, petit-fils de Gengis Khan, mène "
                "une armée mongole jusqu'aux portes de Bagdad après que "
                "le calife Al-Musta'sim a refusé de se soumettre. Le "
                "siège dure moins de deux semaines : le 10 février, "
                "les défenses de la ville cèdent et les troupes "
                "mongoles s'y répandent.",
                "Le sac de Bagdad qui suit est d'une violence extrême "
                ": des centaines de milliers d'habitants sont tués, les "
                "bibliothèques incendiées, leurs manuscrits jetés dans "
                "le Tigre au point, selon la légende, de teinter le "
                "fleuve d'encre. Le calife Al-Musta'sim est exécuté "
                "quelques jours plus tard.",
            ],
            "why_it_matters": (
                "La destruction de Bagdad met fin à cinq siècles d'âge "
                "d'or intellectuel abbasside et marque, pour de "
                "nombreux historiens, un tournant dans le déclin "
                "scientifique et culturel du monde musulman médiéval, "
                "dont les effets se feront sentir pendant des siècles."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "L'armée mongole d'Hulagu Khan met à sac Bagdad, "
                "capitale du califat abbasside depuis plus de cinq "
                "siècles, dans l'un des massacres urbains les plus "
                "documentés du Moyen Âge, mettant fin à un âge d'or "
                "intellectuel dont l'ampleur des pertes reste débattue "
                "par les historiens."
            ),
            "before": (
                "Bagdad est depuis le VIIIe siècle le cœur "
                "intellectuel du monde musulman, abritant la Maison de "
                "la Sagesse, où savants et traducteurs préservent et "
                "enrichissent le savoir grec, perse et indien, même si "
                "le califat abbasside a déjà perdu l'essentiel de son "
                "autorité politique réelle au profit de dynasties "
                "locales bien avant 1258."
            ),
            "during": (
                "Après un siège de moins de deux semaines, les troupes "
                "mongoles d'Hulagu Khan, petit-fils de Gengis Khan et "
                "conseillé par des ministres perses hostiles au "
                "califat, percent les défenses et pillent "
                "systématiquement la ville, épargnant toutefois les "
                "chrétiens et certains savants sur intercession de "
                "conseillers proches du khan."
            ),
            "after": (
                "Le dernier calife abbasside, Al-Musta'sim, est "
                "exécuté selon la tradition mongole sans effusion de "
                "sang royal — roulé dans un tapis puis piétiné par des "
                "chevaux —, la ville est largement détruite et sa "
                "population décimée, marquant la fin institutionnelle "
                "du califat abbasside, dont une branche symbolique "
                "survivra néanmoins au Caire sous protection mamelouke."
            ),
            "narrative": [
                "Depuis sa fondation au VIIIe siècle, Bagdad est la "
                "capitale du califat abbasside et l'un des plus grands "
                "centres intellectuels du monde, abritant la Maison de "
                "la Sagesse où savants et traducteurs préservent et "
                "enrichissent le savoir grec, perse et indien, même si "
                "le pouvoir politique réel du calife s'était largement "
                "délité au profit de dynasties locales bien avant "
                "l'arrivée des Mongols.",
                "En 1258, Hulagu Khan, petit-fils de Gengis Khan, mène "
                "une armée mongole jusqu'aux portes de Bagdad après que "
                "le calife Al-Musta'sim, mal conseillé, a refusé de se "
                "soumettre. Le siège dure moins de deux semaines : le "
                "10 février, les défenses de la ville cèdent et les "
                "troupes mongoles s'y répandent, épargnant néanmoins, "
                "sur intercession de certains conseillers, les "
                "communautés chrétiennes et quelques savants.",
                "Le sac de Bagdad qui suit est d'une violence extrême, "
                "documentée par plusieurs chroniqueurs contemporains : "
                "des centaines de milliers d'habitants sont tués — un "
                "chiffre que l'historiographie moderne tend toutefois à "
                "revoir à la baisse par rapport aux estimations "
                "médiévales —, les bibliothèques incendiées, leurs "
                "manuscrits jetés dans le Tigre au point, selon la "
                "légende, de teinter le fleuve d'encre. Le calife est "
                "exécuté quelques jours plus tard.",
            ],
            "why_it_matters": (
                "La destruction de Bagdad met fin à cinq siècles d'âge "
                "d'or intellectuel abbasside et marque, pour de "
                "nombreux historiens, un tournant dans le déclin "
                "scientifique et culturel du monde musulman médiéval, "
                "même si certains chercheurs contemporains nuancent "
                "l'ampleur de cette rupture en soulignant le déclin "
                "politique déjà bien engagé du califat avant 1258."
            ),
        },
    },
    "mort-de-barbe-noire": {
        "enfant": {
            "summary": (
                "Le 22 novembre 1718, le pirate Barbe Noire est tué "
                "pendant un combat naval. Sa mort marque la fin de "
                "l'époque des grands pirates."
            ),
            "before": (
                "Barbe Noire était un pirate très célèbre et effrayant "
                "dans les Caraïbes."
            ),
            "during": (
                "Un officier britannique, Robert Maynard, attaque le "
                "bateau de Barbe Noire. Un combat éclate sur le pont."
            ),
            "after": (
                "Barbe Noire est tué au combat. Sa tête est coupée et "
                "montrée sur le bateau de son vainqueur."
            ),
            "narrative": [
                "Edward Teach, surnommé « Barbe Noire », est l'un des "
                "pirates les plus célèbres et effrayants des Caraïbes.",
                "En 1718, un officier britannique nommé Robert Maynard "
                "est envoyé pour le capturer.",
                "Le 22 novembre 1718, un combat éclate entre les deux "
                "hommes. Barbe Noire est tué après un combat très "
                "violent.",
            ],
            "why_it_matters": (
                "La mort de Barbe Noire marque la fin d'une époque où "
                "les pirates faisaient très peur sur les mers."
            ),
        },
        "college": {
            "summary": (
                "Le célèbre pirate Edward Teach, dit « Barbe Noire », "
                "est tué lors d'un abordage naval, marquant le déclin "
                "de l'âge d'or de la piraterie."
            ),
            "before": (
                "Après avoir terrorisé le commerce dans les Caraïbes, "
                "Barbe Noire s'est retiré en Caroline du Nord, où il "
                "négocie discrètement avec les autorités locales."
            ),
            "during": (
                "Le lieutenant Robert Maynard, envoyé par le "
                "gouverneur de Virginie, surprend Barbe Noire à "
                "Ocracoke ; un combat s'ensuit sur le pont du navire."
            ),
            "after": (
                "Barbe Noire est tué au terme du combat, décapité, et "
                "sa tête exposée à la proue du navire de Maynard."
            ),
            "narrative": [
                "Edward Teach, surnommé « Barbe Noire », devient l'un "
                "des pirates les plus redoutés des Caraïbes au début du "
                "XVIIIe siècle.",
                "En 1718, il se retire à Ocracoke, en Caroline du "
                "Nord. Le gouverneur de Virginie envoie une expédition "
                "sous le commandement du lieutenant Robert Maynard pour "
                "le capturer.",
                "Le 22 novembre 1718, un combat au sabre s'engage sur "
                "le pont. Barbe Noire, blessé à de multiples reprises, "
                "finit par être tué.",
            ],
            "why_it_matters": (
                "La mort de Barbe Noire marque symboliquement le "
                "déclin de l'âge d'or de la piraterie caribéenne."
            ),
        },
        "lycee": {
            "summary": (
                "Le célèbre pirate Edward Teach, dit « Barbe Noire », "
                "est tué lors d'un abordage naval, marquant le déclin "
                "de l'âge d'or de la piraterie dans les Caraïbes et "
                "l'Atlantique."
            ),
            "before": (
                "Après avoir terrorisé le commerce dans les Caraïbes "
                "et jusqu'à bloquer le port de Charleston avec son "
                "navire amiral, Barbe Noire s'est retiré en Caroline du "
                "Nord, où il négocie discrètement avec les autorités "
                "locales."
            ),
            "during": (
                "Le lieutenant Robert Maynard, envoyé par le "
                "gouverneur de Virginie, surprend Barbe Noire à "
                "Ocracoke ; un combat au corps à corps s'ensuit sur le "
                "pont du navire."
            ),
            "after": (
                "Barbe Noire est tué au terme du combat, décapité, et "
                "sa tête exposée à la proue du navire de Maynard en "
                "guise d'avertissement aux autres pirates."
            ),
            "narrative": [
                "Edward Teach, surnommé « Barbe Noire » pour son "
                "épaisse barbe noire qu'il tressait et enflammait "
                "parfois au combat pour effrayer ses adversaires, "
                "devient l'un des pirates les plus redoutés des "
                "Caraïbes et de la côte atlantique américaine au début "
                "du XVIIIe siècle, période connue comme l'âge d'or de "
                "la piraterie.",
                "En 1718, après avoir bloqué le port de Charleston "
                "avec son navire amiral le Queen Anne's Revenge, il se "
                "retire à Ocracoke, en Caroline du Nord, où il profite "
                "d'une amnistie tout en poursuivant discrètement ses "
                "activités. Le gouverneur de Virginie, inquiet, envoie "
                "une expédition navale sous le commandement du "
                "lieutenant Robert Maynard pour le capturer.",
                "Le 22 novembre 1718, les navires de Maynard rejoignent "
                "Barbe Noire à Ocracoke. Après un échange de tirs, un "
                "combat au sabre s'engage sur le pont. Barbe Noire, "
                "blessé à de multiples reprises, finit par être tué. Sa "
                "tête est tranchée et suspendue à la proue du navire de "
                "Maynard.",
            ],
            "why_it_matters": (
                "La mort de Barbe Noire marque symboliquement le "
                "déclin de l'âge d'or de la piraterie caribéenne, alors "
                "que les grandes puissances européennes intensifient "
                "leur répression navale contre les pirates dans les "
                "décennies suivantes."
            ),
        },
        "etudiant_adulte": {
            "summary": (
                "Le pirate Edward Teach, dit « Barbe Noire », dont la "
                "réputation terrifiante devait davantage à sa mise en "
                "scène théâtrale qu'à une violence documentée envers "
                "ses victimes, est tué lors d'un abordage naval qui "
                "devient l'un des épisodes les plus mythifiés de l'âge "
                "d'or de la piraterie."
            ),
            "before": (
                "Après avoir terrorisé le commerce dans les Caraïbes "
                "et bloqué le port de Charleston avec son navire "
                "amiral le Queen Anne's Revenge, Barbe Noire s'est "
                "retiré à Ocracoke, en Caroline du Nord, où il "
                "bénéficie d'une amnistie royale tout en poursuivant "
                "discrètement ses activités, probablement avec la "
                "complicité tacite du gouverneur local."
            ),
            "during": (
                "Le lieutenant Robert Maynard, envoyé par le "
                "gouverneur de Virginie soucieux de préserver le "
                "commerce colonial, surprend Barbe Noire à Ocracoke à "
                "l'aide d'un stratagème dissimulant l'essentiel de son "
                "équipage sous le pont ; un combat au corps à corps "
                "particulièrement acharné s'ensuit, Barbe Noire "
                "recevant selon les récits une vingtaine de blessures "
                "avant de succomber."
            ),
            "after": (
                "Barbe Noire est tué au terme du combat, décapité, et "
                "sa tête exposée à la proue du navire de Maynard en "
                "guise d'avertissement, tandis que les fouilles menées "
                "depuis 1996 sur l'épave présumée du Queen Anne's "
                "Revenge continuent d'alimenter la documentation "
                "historique de sa légende."
            ),
            "narrative": [
                "Edward Teach, surnommé « Barbe Noire » pour son "
                "épaisse barbe noire qu'il tressait et enflammait "
                "parfois au combat pour effrayer ses adversaires, "
                "devient l'un des pirates les plus redoutés des "
                "Caraïbes et de la côte atlantique américaine au début "
                "du XVIIIe siècle — sa réputation de cruauté, notent "
                "les historiens, reposant davantage sur cette mise en "
                "scène intimidante que sur des actes de violence "
                "avérés envers ses prisonniers.",
                "En 1718, après avoir bloqué le port de Charleston "
                "avec son navire amiral le Queen Anne's Revenge, il se "
                "retire à Ocracoke, en Caroline du Nord, où il profite "
                "d'une amnistie royale tout en poursuivant discrètement "
                "ses activités. Le gouverneur de Virginie, inquiet pour "
                "le commerce colonial, envoie une expédition navale "
                "sous le commandement du lieutenant Robert Maynard.",
                "Le 22 novembre 1718, les navires de Maynard rejoignent "
                "Barbe Noire à Ocracoke à l'aide d'un stratagème "
                "dissimulant l'essentiel de l'équipage sous le pont. "
                "Après un échange de tirs, un combat au sabre "
                "particulièrement acharné s'engage ; Barbe Noire, "
                "blessé à une vingtaine de reprises selon les récits, "
                "finit par être tué. Sa tête est tranchée et suspendue "
                "à la proue du navire de Maynard.",
            ],
            "why_it_matters": (
                "La mort de Barbe Noire marque symboliquement le "
                "déclin de l'âge d'or de la piraterie caribéenne, alors "
                "que les grandes puissances européennes intensifient "
                "leur répression navale dans les décennies suivantes, "
                "tout en léguant à la postérité l'une des figures les "
                "plus mythifiées — et sans doute les plus "
                "surestimées dans sa cruauté réelle — de l'imaginaire "
                "collectif de la piraterie."
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
    "tuileries-consequence": {
        "enfant": {
            "prompt": "Que fait Louis XVI pendant l'attaque des Tuileries ?",
            "options": [
                "Il part se réfugier près de l'Assemblée",
                "Il combat avec ses gardes",
                "Il s'enfuit à l'étranger",
                "Il négocie avec la foule",
            ],
            "correct_index": 0,
            "fun_fact": "Louis XVI quitte le palais pour se réfugier près de l'Assemblée, laissant ses gardes suisses se battre seuls.",
        },
        "college": {
            "prompt": "Quelle a été la conséquence directe de la prise des Tuileries le 10 août 1792 ?",
            "options": [
                "Le couronnement de Louis XVI",
                "La suspension du roi et la fin de la monarchie de fait",
                "La signature de la paix avec la Prusse",
                "La construction d'un nouveau palais royal",
            ],
            "correct_index": 1,
            "fun_fact": "Après le 10 août 1792, l'Assemblée législative suspend Louis XVI. Six semaines plus tard, la Convention proclame la première République.",
        },
        "lycee": {
            "prompt": "Qui défend seul le palais des Tuileries après le départ de Louis XVI vers l'Assemblée ?",
            "options": [
                "Les Gardes suisses",
                "La Garde nationale",
                "L'armée régulière française",
                "Des volontaires parisiens royalistes",
            ],
            "correct_index": 0,
            "fun_fact": "Les quelque neuf cents Gardes suisses, sans ordre clair de se retirer, affrontent seuls l'assaut : les combats font près d'un millier de morts.",
        },
        "etudiant_adulte": {
            "prompt": "Pourquoi le manifeste de Brunswick a-t-il aggravé la situation de Louis XVI plutôt que de le protéger ?",
            "options": [
                "En menaçant Paris de représailles, il a radicalisé l'opinion contre le roi soupçonné de complicité",
                "Il annonçait l'abdication immédiate du roi",
                "Il proposait une alliance militaire entre la France et la Prusse",
                "Il a été rédigé par Louis XVI lui-même",
            ],
            "correct_index": 0,
            "fun_fact": "Le manifeste de Brunswick, menaçant Paris de représailles en cas d'atteinte à la famille royale, produit l'effet inverse de celui recherché.",
        },
    },
    "mur-berlin-annee": {
        "enfant": {
            "prompt": "Pourquoi les Berlinois se précipitent-ils vers le mur le 9 novembre 1989 ?",
            "options": [
                "Un porte-parole annonce qu'ils peuvent voyager librement",
                "Le mur prend feu",
                "Une fête est organisée sur place",
                "Le président ouest-allemand donne l'ordre de le détruire",
            ],
            "correct_index": 0,
            "fun_fact": "L'annonce confuse d'un porte-parole a poussé des milliers de Berlinois vers les points de passage du mur.",
        },
        "college": {
            "prompt": "En quelle année le mur de Berlin est-il tombé ?",
            "options": ["1961", "1975", "1989", "1991"],
            "correct_index": 2,
            "fun_fact": "Le mur de Berlin, érigé en 1961, est tombé le 9 novembre 1989 après une annonce gouvernementale confuse.",
        },
        "lycee": {
            "prompt": "Qui est le porte-parole dont l'annonce confuse déclenche l'ouverture du mur le 9 novembre 1989 ?",
            "options": ["Günter Schabowski", "Helmut Kohl", "Mikhaïl Gorbatchev", "Erich Honecker"],
            "correct_index": 0,
            "fun_fact": "Günter Schabowski annonce en conférence de presse, de façon confuse, que les citoyens de RDA peuvent voyager librement « immédiatement ».",
        },
        "etudiant_adulte": {
            "prompt": "Pourquoi les gardes-frontières finissent-ils par ouvrir les barrières du mur, sans ordre officiel de le faire ?",
            "options": [
                "Débordés par la foule et sans instructions claires, ils n'ont pas d'autre option pour éviter un drame",
                "Ils avaient reçu l'ordre secret de Gorbatchev",
                "Le mur s'est effondré tout seul sous la pression",
                "L'armée ouest-allemande a franchi la frontière",
            ],
            "correct_index": 0,
            "fun_fact": "Le lieutenant-colonel Harald Jäger, à Bornholmer Straße, ouvre les barrières faute d'alternative pour contenir la foule sans recourir à la force.",
        },
    },
    "debarquement-date": {
        "enfant": {
            "prompt": "Que font des milliers de parachutistes la nuit avant le débarquement ?",
            "options": [
                "Ils sont largués en Normandie pour sécuriser des points stratégiques",
                "Ils bombardent Paris",
                "Ils attendent en Angleterre",
                "Ils négocient avec les Allemands",
            ],
            "correct_index": 0,
            "fun_fact": "Dans la nuit du 5 au 6 juin 1944, des milliers de parachutistes sont largués en Normandie avant l'assaut principal.",
        },
        "college": {
            "prompt": "Sur combien de plages les troupes alliées ont-elles débarqué le 6 juin 1944 ?",
            "options": ["Deux", "Trois", "Cinq", "Sept"],
            "correct_index": 2,
            "fun_fact": "Les Alliés ont débarqué sur cinq plages normandes codées Utah, Omaha, Gold, Juno et Sword.",
        },
        "lycee": {
            "prompt": "Sur quelle plage les défenses allemandes infligent-elles les pertes les plus lourdes aux Alliés ?",
            "options": ["Omaha Beach", "Utah Beach", "Sword Beach", "Juno Beach"],
            "correct_index": 0,
            "fun_fact": "Les combats sont particulièrement meurtriers à Omaha Beach, où les défenses allemandes infligent de très lourdes pertes.",
        },
        "etudiant_adulte": {
            "prompt": "Quel est l'objectif de l'opération Fortitude, menée en parallèle du débarquement ?",
            "options": [
                "Tromper l'état-major allemand en lui faisant croire à un débarquement dans le Pas-de-Calais",
                "Bombarder les usines d'armement allemandes",
                "Négocier une reddition anticipée de l'Allemagne",
                "Évacuer les civils normands avant l'assaut",
            ],
            "correct_index": 0,
            "fun_fact": "L'opération Fortitude, vaste campagne de désinformation, a fait croire aux Allemands à un débarquement dans le Pas-de-Calais.",
        },
    },
    "armistice-heure": {
        "enfant": {
            "prompt": "Où l'armistice de 1918 est-il signé ?",
            "options": [
                "Dans un wagon de train, en forêt de Compiègne",
                "Au château de Versailles",
                "À Berlin",
                "Sur un bateau"
            ],
            "correct_index": 0,
            "fun_fact": "L'armistice est signé dans un wagon-restaurant aménagé, en forêt de Compiègne.",
        },
        "college": {
            "prompt": "À quelle heure les combats ont-ils officiellement cessé le 11 novembre 1918 ?",
            "options": ["6 heures", "9 heures", "11 heures", "Minuit"],
            "correct_index": 2,
            "fun_fact": "L'armistice, signé à 5h15, est entré en vigueur à 11 heures précises — le « onzième jour du onzième mois à la onzième heure ».",
        },
        "lycee": {
            "prompt": "Qui négocie et signe l'armistice avec le maréchal Foch le 11 novembre 1918 ?",
            "options": [
                "Une délégation allemande menée par Matthias Erzberger",
                "Le Kaiser Guillaume II en personne",
                "Le chancelier Bismarck",
                "Un général austro-hongrois",
            ],
            "correct_index": 0,
            "fun_fact": "La délégation allemande, conduite par le politicien Matthias Erzberger, signe l'armistice dans le wagon du maréchal Foch.",
        },
        "etudiant_adulte": {
            "prompt": "Pourquoi l'état-major allemand confie-t-il la signature de l'armistice à une délégation civile plutôt que militaire ?",
            "options": [
                "Pour ne pas endosser militairement la responsabilité de la défaite",
                "Parce qu'aucun général n'était disponible",
                "Sur exigence des Alliés",
                "Parce que l'armée avait déjà capitulé séparément",
            ],
            "correct_index": 0,
            "fun_fact": "Le choix du civil Matthias Erzberger pour signer l'armistice est un choix délibéré de l'état-major pour ne pas endosser la défaite militairement.",
        },
    },
    "independance-americaine-annee": {
        "enfant": {
            "prompt": "Qui a écrit le texte de la déclaration d'indépendance américaine ?",
            "options": ["Thomas Jefferson", "George Washington", "Benjamin Franklin", "John Adams"],
            "correct_index": 0,
            "fun_fact": "Le texte a été écrit surtout par Thomas Jefferson et voté le 4 juillet 1776.",
        },
        "college": {
            "prompt": "Qui a principalement rédigé la déclaration d'indépendance américaine de 1776 ?",
            "options": ["George Washington", "Thomas Jefferson", "Benjamin Franklin", "John Adams"],
            "correct_index": 1,
            "fun_fact": "Thomas Jefferson a rédigé l'essentiel du texte, adopté à Philadelphie le 4 juillet 1776.",
        },
        "lycee": {
            "prompt": "Sur quel principe repose la contestation des colonies américaines contre la couronne britannique ?",
            "options": [
                "« No taxation without representation »",
                "Le droit divin des rois",
                "La liberté de culte",
                "Le droit à l'autodétermination des peuples",
            ],
            "correct_index": 0,
            "fun_fact": "Les colonies réclament la fin des taxes imposées sans qu'elles aient de représentants au Parlement de Londres.",
        },
        "etudiant_adulte": {
            "prompt": "Quelle contradiction majeure la déclaration d'indépendance laisse-t-elle en suspens ?",
            "options": [
                "La proclamation de l'égalité universelle alors que l'esclavage perdure dans les colonies signataires",
                "L'absence de toute référence à la liberté individuelle",
                "Le refus d'accorder le droit de vote aux hommes propriétaires",
                "L'interdiction du commerce avec la France",
            ],
            "correct_index": 0,
            "fun_fact": "Un paragraphe de Jefferson condamnant la traite négrière est supprimé du texte final ; l'esclavage ne sera aboli que près d'un siècle plus tard.",
        },
    },
    "colomb-annee": {
        "enfant": {
            "prompt": "Comment s'appelle l'île où Christophe Colomb débarque en 1492 ?",
            "options": ["San Salvador", "Cuba", "Hispaniola", "La Jamaïque"],
            "correct_index": 0,
            "fun_fact": "Colomb débarque sur une île des Bahamas qu'il baptise San Salvador.",
        },
        "college": {
            "prompt": "En quelle année l'expédition de Christophe Colomb atteint-elle les Amériques ?",
            "options": ["1453", "1492", "1517", "1534"],
            "correct_index": 1,
            "fun_fact": "Le 12 octobre 1492, après 36 jours de traversée, l'expédition de Colomb débarque sur une île des Bahamas.",
        },
        "lycee": {
            "prompt": "Quel nom Colomb donne-t-il aux habitants qu'il rencontre, persuadé d'avoir atteint l'Asie ?",
            "options": ["Indiens", "Américains", "Antillais", "Caraïbes"],
            "correct_index": 0,
            "fun_fact": "Persuadé d'avoir atteint les Indes orientales, Colomb nomme les habitants qu'il rencontre « Indiens ».",
        },
        "etudiant_adulte": {
            "prompt": "Pourquoi la traversée de Colomb aurait-elle probablement échoué sans la présence imprévue d'un continent ?",
            "options": [
                "Il avait largement sous-estimé la circonférence réelle de la Terre",
                "Ses navires n'avaient pas assez de voiles",
                "L'équipage refusait de naviguer de nuit",
                "Il naviguait sans carte du tout",
            ],
            "correct_index": 0,
            "fun_fact": "Les calculs de Colomb sous-estimaient largement la distance à parcourir ; sans continent américain sur la route, le voyage aurait été impossible faute de vivres.",
        },
    },
    "nuit-4-aout-consequence": {
        "enfant": {
            "prompt": "Qu'abandonnent les nobles dans la nuit du 4 août 1789 ?",
            "options": [
                "Leurs droits et privilèges sur les paysans",
                "Leurs terres au roi",
                "Leurs titres de noblesse",
                "Leurs châteaux à l'Église",
            ],
            "correct_index": 0,
            "fun_fact": "Des nobles renoncent l'un après l'autre à leurs droits féodaux sur les paysans, pendant une réunion de nuit.",
        },
        "college": {
            "prompt": "Qu'a aboli l'Assemblée constituante dans la nuit du 4 août 1789 ?",
            "options": ["La monarchie", "Les privilèges féodaux", "L'esclavage dans les colonies", "La peine de mort"],
            "correct_index": 1,
            "fun_fact": "Dans un mouvement d'entraînement collectif, nobles et clergé renoncent tour à tour à leurs privilèges féodaux et fiscaux.",
        },
        "lycee": {
            "prompt": "Quels sont les deux députés à l'origine de la proposition d'abolition des droits féodaux ?",
            "options": [
                "Le vicomte de Noailles et le duc d'Aiguillon",
                "Robespierre et Danton",
                "Mirabeau et Sieyès",
                "La Fayette et Necker",
            ],
            "correct_index": 0,
            "fun_fact": "Le vicomte de Noailles et le duc d'Aiguillon proposent l'abolition des droits féodaux pour apaiser les campagnes en révolte.",
        },
        "etudiant_adulte": {
            "prompt": "Pourquoi l'abolition votée dans la nuit du 4 août 1789 est-elle en réalité plus nuancée qu'il n'y paraît ?",
            "options": [
                "Les décrets rédigés ensuite rendent certains droits rachetables plutôt qu'abolis sans compensation",
                "Le roi a immédiatement annulé le vote",
                "Seuls les droits religieux ont finalement été supprimés",
                "L'Assemblée s'est rétractée dès le lendemain",
            ],
            "correct_index": 0,
            "fun_fact": "L'abolition complète et sans indemnité des droits seigneuriaux ne sera votée qu'en 1793, sous la Convention.",
        },
    },
    "waterloo-consequence": {
        "enfant": {
            "prompt": "Qu'est-il arrivé à Napoléon après sa défaite à Waterloo ?",
            "options": [
                "Il a été exilé sur l'île de Sainte-Hélène",
                "Il a repris le pouvoir en France",
                "Il a été exécuté",
                "Il est devenu roi d'Espagne",
            ],
            "correct_index": 0,
            "fun_fact": "Napoléon est exilé par les Britanniques sur l'île isolée de Sainte-Hélène, où il mourra en 1821.",
        },
        "college": {
            "prompt": "Quelle armée arrive en renfort en fin de journée et fait basculer la bataille de Waterloo ?",
            "options": ["L'armée prussienne de Blücher", "L'armée autrichienne", "L'armée russe", "L'armée espagnole"],
            "correct_index": 0,
            "fun_fact": "L'arrivée de l'armée prussienne de Blücher en fin de journée fait basculer la bataille en faveur des coalisés.",
        },
        "lycee": {
            "prompt": "Sur quel plateau les troupes de Wellington sont-elles retranchées à Waterloo ?",
            "options": ["Le Mont-Saint-Jean", "Les hauteurs de Ligny", "Le plateau d'Austerlitz", "Le mont Valérien"],
            "correct_index": 0,
            "fun_fact": "Les troupes anglo-alliées de Wellington sont retranchées sur le plateau du Mont-Saint-Jean, près du village de Waterloo.",
        },
        "etudiant_adulte": {
            "prompt": "Pourquoi Napoléon est-il pris par surprise par l'arrivée de l'armée prussienne à Waterloo ?",
            "options": [
                "Il la croyait hors de combat après sa victoire à Ligny deux jours plus tôt",
                "Elle n'était pas censée exister",
                "Elle combattait officiellement aux côtés de la France",
                "Elle arrivait d'Espagne et non d'Allemagne",
            ],
            "correct_index": 0,
            "fun_fact": "Napoléon croyait l'armée prussienne durablement écartée après sa victoire à Ligny deux jours plus tôt — une erreur d'appréciation décisive.",
        },
    },
    "sacre-napoleon-lieu": {
        "enfant": {
            "prompt": "Qui pose la couronne sur la tête de Napoléon le jour de son sacre ?",
            "options": ["Napoléon lui-même", "Le pape", "Le roi d'Espagne", "Joséphine"],
            "correct_index": 0,
            "fun_fact": "Même si le pape est venu de Rome, c'est Napoléon lui-même qui se couronne, un geste très symbolique.",
        },
        "college": {
            "prompt": "Qui a couronné Napoléon Ier lors de son sacre en 1804 ?",
            "options": ["Le pape Pie VII", "Napoléon s'est couronné lui-même", "Le roi d'Espagne", "L'archevêque de Paris"],
            "correct_index": 1,
            "fun_fact": "Bien que le pape Pie VII ait fait le déplacement de Rome, c'est Napoléon lui-même qui a posé la couronne sur sa tête.",
        },
        "lycee": {
            "prompt": "Qui a peint et orchestré la mise en scène du sacre de Napoléon ?",
            "options": ["Jacques-Louis David", "Eugène Delacroix", "Jean-Auguste-Dominique Ingres", "Antoine-Jean Gros"],
            "correct_index": 0,
            "fun_fact": "Jacques-Louis David a orchestré la cérémonie et en a immortalisé la scène dans un tableau monumental.",
        },
        "etudiant_adulte": {
            "prompt": "En quoi le geste de Napoléon se couronnant lui-même rompt-il avec la tradition du sacre royal ?",
            "options": [
                "Le monarque recevait traditionnellement la couronne des mains du prélat, symbolisant le pouvoir venu de Dieu",
                "Aucun roi de France n'avait jamais été couronné à Notre-Dame auparavant",
                "La tradition voulait que ce soit la reine qui couronne le roi",
                "Les sacres royaux ne se déroulaient jamais en présence du pape",
            ],
            "correct_index": 0,
            "fun_fact": "En se couronnant lui-même, Napoléon affirme tenir son pouvoir du peuple et de lui-même plutôt que de l'Église.",
        },
    },
    "magna-carta-principe": {
        "enfant": {
            "prompt": "Que dit la Magna Carta sur la prison ?",
            "options": [
                "On ne peut pas mettre quelqu'un en prison sans un vrai jugement",
                "Tout le monde doit aller en prison une fois dans sa vie",
                "Le roi ne peut jamais aller en prison",
                "Les prisons sont interdites en Angleterre",
            ],
            "correct_index": 0,
            "fun_fact": "C'est une grande nouveauté pour l'époque : même le roi doit respecter des règles.",
        },
        "college": {
            "prompt": "Quel principe la Magna Carta de 1215 a-t-elle établi ?",
            "options": ["Le suffrage universel", "La limitation du pouvoir royal face aux barons", "L'abolition de l'esclavage", "La liberté de la presse"],
            "correct_index": 1,
            "fun_fact": "La Magna Carta garantit qu'aucun homme libre ne peut être emprisonné sans jugement légal, une limite inédite au pouvoir royal.",
        },
        "lycee": {
            "prompt": "Où le roi Jean sans Terre appose-t-il son sceau sur la Magna Carta ?",
            "options": ["À Runnymede, au bord de la Tamise", "À Londres, à la Tour", "À Cantorbéry", "À Westminster"],
            "correct_index": 0,
            "fun_fact": "Le 15 juin 1215, dans la prairie de Runnymede au bord de la Tamise, Jean sans Terre appose son sceau sur la Magna Carta.",
        },
        "etudiant_adulte": {
            "prompt": "Pourquoi la Magna Carta est-elle rapidement annulée après sa signature en 1215 ?",
            "options": [
                "Le pape l'annule dès août 1215 à la demande du roi lui-même",
                "Les barons l'ont eux-mêmes rejetée",
                "Elle n'a jamais été officiellement scellée",
                "Le roi de France l'a déclarée illégale",
            ],
            "correct_index": 0,
            "fun_fact": "Annulée par le pape dès août 1215, la charte n'est réémise sous une forme modifiée qu'après la mort de Jean sans Terre en 1216.",
        },
    },
    "vesuve-consequence": {
        "enfant": {
            "prompt": "Que devient la ville de Pompéi après l'éruption du Vésuve ?",
            "options": [
                "Elle est recouverte de cendres et oubliée pendant très longtemps",
                "Elle est reconstruite immédiatement",
                "Elle devient la capitale de l'Italie",
                "Les habitants la déplacent ailleurs",
            ],
            "correct_index": 0,
            "fun_fact": "Pompéi a été retrouvée très bien conservée sous les cendres, plus de 1600 ans après l'éruption.",
        },
        "college": {
            "prompt": "Qu'est-il arrivé à Pompéi après l'éruption du Vésuve en l'an 79 ?",
            "options": ["La ville a été reconstruite immédiatement", "La ville a été ensevelie et oubliée pendant des siècles", "La ville a été déplacée", "La ville est devenue une nouvelle capitale romaine"],
            "correct_index": 1,
            "fun_fact": "Ensevelie sous plusieurs mètres de cendres, Pompéi a été oubliée pendant plus de seize siècles avant d'être redécouverte au XVIIIe siècle.",
        },
        "lycee": {
            "prompt": "Qui a laissé un témoignage écrit détaillé de l'éruption du Vésuve ?",
            "options": ["Pline le Jeune", "Cicéron", "Suétone", "Tacite lui-même, sur place"],
            "correct_index": 0,
            "fun_fact": "Pline le Jeune, témoin depuis l'autre rive du golfe de Naples, laisse un récit détaillé de la catastrophe dans deux lettres à Tacite.",
        },
        "etudiant_adulte": {
            "prompt": "Pourquoi le terme « éruption plinienne » est-il utilisé pour ce type d'éruption volcanique ?",
            "options": [
                "En hommage au récit scientifique précis laissé par Pline le Jeune",
                "Parce que le volcan s'appelait le Plinius",
                "Parce que Pline l'Ancien a inventé ce type d'éruption",
                "C'est le nom de la région où se trouve le Vésuve",
            ],
            "correct_index": 0,
            "fun_fact": "Le récit de Pline le Jeune est si précis scientifiquement que ce type d'éruption porte aujourd'hui son nom.",
        },
    },
    "krach-1929-consequence": {
        "enfant": {
            "prompt": "Que se passe-t-il après le krach de 1929 ?",
            "options": [
                "Beaucoup de gens perdent leur travail",
                "Tout redevient normal en une semaine",
                "Les prix des actions montent encore plus",
                "Les banques deviennent plus riches",
            ],
            "correct_index": 0,
            "fun_fact": "Le krach de 1929 déclenche une immense crise économique mondiale : la Grande Dépression.",
        },
        "college": {
            "prompt": "Quelle crise économique majeure le krach de 1929 a-t-il déclenchée ?",
            "options": ["La Grande Dépression", "La crise du pétrole", "L'hyperinflation allemande", "La crise des subprimes"],
            "correct_index": 0,
            "fun_fact": "Le krach de Wall Street en octobre 1929 précipite la Grande Dépression, la pire crise économique du XXe siècle.",
        },
        "lycee": {
            "prompt": "Comment appelle-t-on les deux jours de chute vertigineuse qui suivent le « jeudi noir » ?",
            "options": ["« Lundi noir » et « mardi noir »", "« Vendredi rouge » et « samedi rouge »", "Les « jours de panique »", "Le « grand effondrement »"],
            "correct_index": 0,
            "fun_fact": "Les 28 et 29 octobre 1929, surnommés « lundi noir » et « mardi noir », voient de nouvelles chutes vertigineuses.",
        },
        "etudiant_adulte": {
            "prompt": "Quel rôle joue le crédit boursier (« buying on margin ») dans l'ampleur du krach de 1929 ?",
            "options": [
                "Il a amplifié la spéculation et la chute, les investisseurs empruntant pour acheter des actions",
                "Il a protégé les petits investisseurs de la chute",
                "Il n'existait pas encore en 1929",
                "Il concernait uniquement les banques, pas les particuliers",
            ],
            "correct_index": 0,
            "fun_fact": "Des investisseurs empruntant massivement, parfois avec seulement 10 % d'apport personnel, pour acheter des actions ont amplifié la chute.",
        },
    },
    "pearl-harbor-consequence": {
        "enfant": {
            "prompt": "Que se passe-t-il le lendemain de l'attaque de Pearl Harbor ?",
            "options": [
                "Les États-Unis déclarent la guerre au Japon",
                "Le Japon présente ses excuses",
                "Les États-Unis quittent la guerre",
                "Rien ne se passe",
            ],
            "correct_index": 0,
            "fun_fact": "Le président Roosevelt appelle ce jour « une date qui restera dans l'infamie ».",
        },
        "college": {
            "prompt": "Quelle a été la conséquence directe de l'attaque de Pearl Harbor ?",
            "options": ["Le Japon a capitulé", "Les États-Unis sont entrés en guerre", "La France a été libérée", "L'URSS a rejoint l'Axe"],
            "correct_index": 1,
            "fun_fact": "Le lendemain de l'attaque du 7 décembre 1941, les États-Unis déclarent la guerre au Japon.",
        },
        "lycee": {
            "prompt": "Pourquoi les porte-avions américains échappent-ils à la destruction à Pearl Harbor ?",
            "options": [
                "Ils étaient absents ce jour-là",
                "Ils étaient trop bien protégés",
                "Les Japonais les ont épargnés volontairement",
                "Ils avaient été prévenus de l'attaque",
            ],
            "correct_index": 0,
            "fun_fact": "Les porte-avions américains, absents ce jour-là, échappent à la destruction — un hasard stratégiquement décisif pour la suite de la guerre.",
        },
        "etudiant_adulte": {
            "prompt": "En quoi l'attaque de Pearl Harbor constitue-t-elle une erreur stratégique japonaise malgré son succès tactique ?",
            "options": [
                "L'industrie américaine reconstruit sa flotte bien plus vite que le Japon ne pouvait l'anticiper",
                "Le Japon n'a coulé aucun navire américain",
                "Les États-Unis étaient déjà en guerre avant l'attaque",
                "L'attaque a été annulée à la dernière minute",
            ],
            "correct_index": 0,
            "fun_fact": "Malgré la destruction de plusieurs cuirassés, l'industrie américaine reconstruit sa flotte à un rythme que le Japon n'avait pas anticipé.",
        },
    },
    "hiroshima-date": {
        "enfant": {
            "prompt": "Que se passe-t-il trois jours après la bombe sur Hiroshima ?",
            "options": [
                "Une deuxième bombe tombe sur Nagasaki",
                "Le Japon gagne la guerre",
                "La guerre s'arrête immédiatement",
                "Hiroshima est reconstruite",
            ],
            "correct_index": 0,
            "fun_fact": "Le 9 août 1945, une seconde bombe atomique frappe la ville de Nagasaki.",
        },
        "college": {
            "prompt": "En quelle année la bombe atomique a-t-elle été larguée sur Hiroshima ?",
            "options": ["1943", "1944", "1945", "1946"],
            "correct_index": 2,
            "fun_fact": "Le 6 août 1945, le bombardier Enola Gay largue la première bombe atomique de l'histoire militaire sur Hiroshima.",
        },
        "lycee": {
            "prompt": "Comment s'appelle la bombe atomique larguée sur Hiroshima ?",
            "options": ["Little Boy", "Fat Man", "Trinity", "Manhattan"],
            "correct_index": 0,
            "fun_fact": "La bombe « Little Boy » est larguée sur Hiroshima le 6 août 1945 à 8h15 du matin.",
        },
        "etudiant_adulte": {
            "prompt": "Quel événement militaire majeur survient entre les bombardements d'Hiroshima et de Nagasaki ?",
            "options": [
                "L'URSS déclare la guerre au Japon et envahit la Mandchourie",
                "Le Japon capitule une première fois",
                "Les États-Unis envahissent le Japon par voie terrestre",
                "La Chine signe un armistice avec le Japon",
            ],
            "correct_index": 0,
            "fun_fact": "Le 8 août, entre les deux bombardements, l'URSS déclare la guerre au Japon et envahit la Mandchourie.",
        },
    },
    "victoire-europe-mois": {
        "enfant": {
            "prompt": "Où meurt Adolf Hitler, juste avant la fin de la guerre ?",
            "options": [
                "Dans son bunker à Berlin",
                "En prison",
                "Dans un avion",
                "En Espagne",
            ],
            "correct_index": 0,
            "fun_fact": "Hitler se suicide dans son bunker le 30 avril 1945, alors que Berlin est encerclée.",
        },
        "college": {
            "prompt": "En quel mois la capitulation allemande de 1945 a-t-elle été signée ?",
            "options": ["Janvier", "Mai", "Août", "Décembre"],
            "correct_index": 1,
            "fun_fact": "L'Allemagne capitule le 8 mai 1945, une date encore commémorée chaque année en France.",
        },
        "lycee": {
            "prompt": "Pourquoi une seconde cérémonie de capitulation a-t-elle lieu à Berlin après celle de Reims ?",
            "options": [
                "Staline la juge insuffisamment solennelle et l'exige sur le sol allemand",
                "Les Allemands ont refusé de signer à Reims",
                "Le général Eisenhower était absent le 7 mai",
                "Les Français exigeaient leur propre cérémonie",
            ],
            "correct_index": 0,
            "fun_fact": "Staline, jugeant la cérémonie de Reims insuffisamment solennelle, exige une seconde signature à Berlin.",
        },
        "etudiant_adulte": {
            "prompt": "Pourquoi la date de commémoration de la victoire diffère-t-elle entre l'Occident (8 mai) et la Russie (9 mai) ?",
            "options": [
                "En raison du décalage horaire de la signature nocturne à Berlin",
                "La Russie utilise un calendrier différent",
                "La capitulation a été signée deux fois à des dates différentes",
                "C'est une erreur historique jamais corrigée",
            ],
            "correct_index": 0,
            "fun_fact": "La signature nocturne à Berlin-Karlshorst tombe après minuit heure de Moscou, d'où le décalage entre le 8 et le 9 mai.",
        },
    },
    "gagarine-duree": {
        "enfant": {
            "prompt": "Qu'a accompli Youri Gagarine le 12 avril 1961 ?",
            "options": ["Le premier vol spatial habité", "Le premier alunissage", "La première sortie dans l'espace", "Le premier satellite artificiel"],
            "correct_index": 0,
            "fun_fact": "En 108 minutes, Gagarine devient le premier être humain à voyager dans l'espace.",
        },
        "college": {
            "prompt": "Combien de temps dure le vol de Gagarine autour de la Terre ?",
            "options": ["108 minutes", "24 heures", "8 jours", "3 heures"],
            "correct_index": 0,
            "fun_fact": "Gagarine effectue une orbite complète autour de la Terre en 108 minutes, à bord de Vostok 1.",
        },
        "lycee": {
            "prompt": "Comment Gagarine revient-il sur Terre après son vol ?",
            "options": ["Il s'éjecte et atterrit en parachute", "Le vaisseau se pose comme un avion", "Il amerrit dans l'océan", "Un autre vaisseau vient le récupérer en orbite"],
            "correct_index": 0,
            "fun_fact": "Le vaisseau redescend et Gagarine s'éjecte pour atterrir en parachute près de la Volga, comme prévu par la procédure soviétique.",
        },
        "etudiant_adulte": {
            "prompt": "Pourquoi les commandes de vol de Vostok 1 sont-elles verrouillées pendant le vol de Gagarine ?",
            "options": [
                "Par prudence médicale, les effets de l'apesanteur sur le jugement humain étant alors inconnus",
                "Gagarine n'était pas qualifié pour piloter",
                "Le vaisseau n'avait pas de commandes manuelles",
                "Les ingénieurs craignaient un sabotage",
            ],
            "correct_index": 0,
            "fun_fact": "Le vol est entièrement automatisé par prudence médicale, un code transmis depuis le sol pouvant débloquer les commandes en cas de besoin.",
        },
    },
    "mlk-discours-lieu": {
        "enfant": {
            "prompt": "Où Martin Luther King fait-il son discours célèbre ?",
            "options": ["Devant le Lincoln Memorial à Washington", "Devant la Maison-Blanche", "À New York", "Au Capitole"],
            "correct_index": 0,
            "fun_fact": "King prononce son discours devant plus de 200 000 personnes rassemblées au Lincoln Memorial.",
        },
        "college": {
            "prompt": "Où Martin Luther King a-t-il prononcé son discours « I Have a Dream » ?",
            "options": ["Devant la Maison-Blanche", "Devant le Lincoln Memorial à Washington", "À l'ONU à New York", "Au Capitole"],
            "correct_index": 1,
            "fun_fact": "Le 28 août 1963, King prononce son discours devant plus de 200 000 personnes lors de la Marche sur Washington.",
        },
        "lycee": {
            "prompt": "Quelle formule célèbre King utilise-t-il pour décrire son rêve d'égalité ?",
            "options": [
                "« Ne pas être jugés sur la couleur de leur peau mais sur le contenu de leur caractère »",
                "« La liberté ou la mort »",
                "« Nous ne céderons jamais »",
                "« Un homme, une voix »",
            ],
            "correct_index": 0,
            "fun_fact": "King développe une vision d'une Amérique où ses enfants « ne seront pas jugés sur la couleur de leur peau mais sur le contenu de leur caractère ».",
        },
        "etudiant_adulte": {
            "prompt": "Comment la partie la plus célèbre du discours de King a-t-elle vu le jour ?",
            "options": [
                "En s'écartant de son texte préparé, encouragé par la chanteuse Mahalia Jackson",
                "Elle avait été entièrement écrite à l'avance par ses conseillers",
                "Elle a été improvisée à la suite d'une panne de micro",
                "Elle reprenait mot pour mot un discours de Lincoln",
            ],
            "correct_index": 0,
            "fun_fact": "Encouragé par Mahalia Jackson à improviser, King s'écarte de son texte préparé pour développer l'anaphore « I have a dream ».",
        },
    },
    "revolution-octobre-lieu": {
        "enfant": {
            "prompt": "Quel bâtiment les bolcheviks prennent-ils en novembre 1917 ?",
            "options": ["Le Palais d'Hiver", "Le Kremlin", "Une église", "Un aéroport"],
            "correct_index": 0,
            "fun_fact": "Le Palais d'Hiver, où siège le gouvernement, est pris presque sans combat par les bolcheviks.",
        },
        "college": {
            "prompt": "Quel bâtiment les bolcheviks prennent-ils d'assaut lors de la révolution d'Octobre ?",
            "options": ["Le Kremlin", "Le Palais d'Hiver", "La cathédrale Saint-Basile", "Le palais de Peterhof"],
            "correct_index": 1,
            "fun_fact": "Le Palais d'Hiver de Petrograd, siège du gouvernement provisoire, est pris d'assaut dans la nuit du 6 au 7 novembre 1917.",
        },
        "lycee": {
            "prompt": "Pourquoi appelle-t-on cet événement la « révolution d'Octobre » alors qu'il a lieu en novembre ?",
            "options": [
                "À cause du calendrier julien alors en vigueur en Russie",
                "C'est une erreur historique jamais corrigée",
                "Les combats ont commencé en octobre et fini en novembre",
                "Lénine préférait le nom « Octobre »",
            ],
            "correct_index": 0,
            "fun_fact": "Selon le calendrier julien alors en vigueur en Russie, l'événement tombe le 24-25 octobre, d'où son nom.",
        },
        "etudiant_adulte": {
            "prompt": "Quel signe précoce révèle la nature autoritaire du nouveau pouvoir bolchevique ?",
            "options": [
                "La dissolution manu militari de l'Assemblée constituante où les bolcheviks sont minoritaires",
                "Le maintien du tsar comme chef d'État symbolique",
                "L'interdiction immédiate du parti bolchevique lui-même",
                "Le refus de Lénine de prendre le pouvoir",
            ],
            "correct_index": 0,
            "fun_fact": "Les bolcheviks n'obtiennent qu'une minorité de sièges lors des seules élections réellement libres de l'histoire soviétique, avant de dissoudre l'Assemblée.",
        },
    },
    "luther-consequence": {
        "enfant": {
            "prompt": "Contre quoi Martin Luther proteste-t-il en 1517 ?",
            "options": ["La vente d'indulgences par l'Église", "Les impôts du roi", "La construction des châteaux", "Le prix du pain"],
            "correct_index": 0,
            "fun_fact": "Luther conteste la vente de documents censés réduire les péchés en échange d'argent.",
        },
        "college": {
            "prompt": "Quel mouvement religieux les 95 thèses de Luther ont-elles déclenché ?",
            "options": ["La Réforme protestante", "Les croisades", "Le schisme d'Orient", "L'Inquisition"],
            "correct_index": 0,
            "fun_fact": "En contestant la vente des indulgences en 1517, Luther déclenche la Réforme protestante.",
        },
        "lycee": {
            "prompt": "Grâce à quelle technologie le texte de Luther se diffuse-t-il si rapidement ?",
            "options": ["L'imprimerie", "La poste royale", "Les journaux", "Le télégraphe"],
            "correct_index": 0,
            "fun_fact": "Grâce à l'imprimerie récemment développée par Gutenberg, le texte est rapidement traduit et diffusé dans tout le Saint-Empire.",
        },
        "etudiant_adulte": {
            "prompt": "Pourquoi l'image de Luther affichant ses thèses sur la porte de l'église est-elle historiquement incertaine ?",
            "options": [
                "Elle n'est attestée que par un témoignage tardif de son collègue Melanchthon",
                "Luther a lui-même démenti cet épisode",
                "Aucune église n'existait à Wittenberg à l'époque",
                "Les thèses ont été publiées uniquement à Rome",
            ],
            "correct_index": 0,
            "fun_fact": "L'affichage sur la porte de l'église, devenu image d'Épinal, n'est attesté avec certitude que par un témoignage tardif de Melanchthon.",
        },
    },
    "mandela-duree-prison": {
        "enfant": {
            "prompt": "Combien d'années Mandela a-t-il passées en prison ?",
            "options": ["27 ans", "7 ans", "50 ans", "2 ans"],
            "correct_index": 0,
            "fun_fact": "Mandela est resté 27 ans en prison avant sa libération le 11 février 1990.",
        },
        "college": {
            "prompt": "Combien d'années Nelson Mandela a-t-il passées en prison avant sa libération en 1990 ?",
            "options": ["7 ans", "17 ans", "27 ans", "37 ans"],
            "correct_index": 2,
            "fun_fact": "Emprisonné en 1962, Mandela est libéré le 11 février 1990 après 27 ans de détention.",
        },
        "lycee": {
            "prompt": "Sur quelle île Mandela passe-t-il la majeure partie de sa détention ?",
            "options": ["Robben Island", "Madagascar", "Sainte-Hélène", "L'île d'Elbe"],
            "correct_index": 0,
            "fun_fact": "Mandela passe 18 de ses 27 années de détention sur l'île-bagne de Robben Island, au large du Cap.",
        },
        "etudiant_adulte": {
            "prompt": "Quand les négociations secrètes entre Mandela et le gouvernement sud-africain ont-elles réellement débuté ?",
            "options": [
                "Dès 1985, bien avant sa libération officielle en 1990",
                "Le jour même de sa libération",
                "Seulement après les élections de 1994",
                "Elles n'ont jamais eu lieu avant sa libération",
            ],
            "correct_index": 0,
            "fun_fact": "Des négociations secrètes entre Mandela et le pouvoir sud-africain avaient débuté dès 1985, cinq ans avant sa libération.",
        },
    },
    "spoutnik-annee": {
        "enfant": {
            "prompt": "En quelle année l'URSS a-t-elle envoyé Spoutnik 1 dans l'espace ?",
            "options": ["1957", "1961", "1969", "1949"],
            "correct_index": 0,
            "fun_fact": "Spoutnik 1 est lancé le 4 octobre 1957, marquant le début de l'ère spatiale.",
        },
        "college": {
            "prompt": "En quelle année l'URSS a-t-elle lancé Spoutnik 1, premier satellite artificiel ?",
            "options": ["1949", "1957", "1961", "1969"],
            "correct_index": 1,
            "fun_fact": "Lancé le 4 octobre 1957, Spoutnik 1 déclenche la course à l'espace entre l'URSS et les États-Unis.",
        },
        "lycee": {
            "prompt": "Quelle agence spatiale les États-Unis créent-ils en réaction au « moment Spoutnik » ?",
            "options": ["La NASA", "L'ESA", "Roscosmos", "Le CNES"],
            "correct_index": 0,
            "fun_fact": "Pris de court, les États-Unis créent la NASA dès 1958, l'année suivant le lancement de Spoutnik.",
        },
        "etudiant_adulte": {
            "prompt": "Sur quelle technologie militaire la fusée R-7 ayant lancé Spoutnik était-elle initialement basée ?",
            "options": [
                "Un missile balistique intercontinental",
                "Un avion de chasse",
                "Un sous-marin nucléaire",
                "Un radar de défense antiaérienne",
            ],
            "correct_index": 0,
            "fun_fact": "La fusée R-7, à l'origine conçue comme missile balistique intercontinental, a été réutilisée pour lancer Spoutnik 1.",
        },
    },
    "chute-rome-consequence": {
        "enfant": {
            "prompt": "Qui dépose le dernier empereur romain d'Occident en 476 ?",
            "options": ["Odoacre", "Attila", "Clovis", "Charlemagne"],
            "correct_index": 0,
            "fun_fact": "Odoacre dépose le jeune empereur Romulus Augustule et devient roi d'Italie.",
        },
        "college": {
            "prompt": "Qui dépose le dernier empereur romain d'Occident en 476 ?",
            "options": ["Attila", "Odoacre", "Clovis", "Charlemagne"],
            "correct_index": 1,
            "fun_fact": "Le chef germanique Odoacre dépose Romulus Augustule en 476, une date retenue comme la fin de l'Antiquité.",
        },
        "lycee": {
            "prompt": "Que fait Odoacre des insignes impériaux après avoir déposé Romulus Augustule ?",
            "options": [
                "Il les renvoie à Constantinople",
                "Il les détruit publiquement",
                "Il les garde et se proclame empereur",
                "Il les vend aux Wisigoths",
            ],
            "correct_index": 0,
            "fun_fact": "Odoacre renvoie les insignes impériaux à Constantinople, reconnaissant l'empereur d'Orient comme seul souverain légitime.",
        },
        "etudiant_adulte": {
            "prompt": "Comment l'historiographie contemporaine tend-elle à réinterpréter la déposition de 476 ?",
            "options": [
                "Comme une étape d'un long processus de transformation romano-germanique plutôt qu'une rupture brutale",
                "Comme un événement sans aucune importance historique",
                "Comme le véritable début de l'Empire byzantin",
                "Comme une invention tardive des historiens médiévaux",
            ],
            "correct_index": 0,
            "fun_fact": "Des historiens comme Peter Brown y voient davantage une étape d'un long processus de transformation que la rupture brutale longtemps enseignée.",
        },
    },
    "watt-invention": {
        "enfant": {
            "prompt": "Quelle amélioration James Watt apporte-t-il à la machine à vapeur ?",
            "options": ["Un condenseur séparé qui économise l'énergie", "Des roues en caoutchouc", "Un moteur électrique", "Une chaudière en verre"],
            "correct_index": 0,
            "fun_fact": "Grâce à son condenseur séparé, la machine de Watt gaspille beaucoup moins d'énergie.",
        },
        "college": {
            "prompt": "Quelle amélioration James Watt apporte-t-il à la machine à vapeur en 1769 ?",
            "options": ["Un condenseur séparé", "Des roues en caoutchouc", "Un moteur électrique", "Une chaudière en verre"],
            "correct_index": 0,
            "fun_fact": "En ajoutant un condenseur séparé, Watt améliore considérablement le rendement énergétique de la machine à vapeur.",
        },
        "lycee": {
            "prompt": "Avec quel industriel Watt s'associe-t-il pour commercialiser ses machines ?",
            "options": ["Matthew Boulton", "Thomas Newcomen", "Robert Stephenson", "Richard Arkwright"],
            "correct_index": 0,
            "fun_fact": "Faute de moyens pour exploiter seul son invention, Watt s'associe à l'industriel Matthew Boulton.",
        },
        "etudiant_adulte": {
            "prompt": "Quelle limite majeure de la machine de Newcomen la machine de Watt corrige-t-elle ?",
            "options": [
                "Le gaspillage d'énergie dû au réchauffement et refroidissement répétés du même cylindre",
                "L'impossibilité de fonctionner dans les mines",
                "L'usage exclusif du charbon comme combustible",
                "Sa taille trop réduite pour être efficace",
            ],
            "correct_index": 0,
            "fun_fact": "Le condenseur séparé de Watt, maintenu froid en permanence, évite de réchauffer puis refroidir sans cesse le cylindre principal.",
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
