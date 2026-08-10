# Chronos

Application musée d'histoire gamifiée — design issu de Google Stitch, backend Flask.

## Fonctionnalités

- **Comptes utilisateurs** : inscription (identifiant, email, mot de passe, niveau d'étude), connexion, déconnexion, suppression de compte.
- **Mot de passe oublié** : demande de réinitialisation par email avec lien à durée de vie limitée (30 min).
- **Pages câblées** : accueil (événement du jour), explorateur (frise des époques), fiche événement, quiz (question aléatoire à chaque visite parmi plusieurs, récompenses XP/tokens/série), profil avec statistiques réelles et choix d'avatar. Toutes protégées par connexion.
- **Chronos Tokens** : icône dédiée (SVG inline, pas d'étoile générique), affichée dans la navigation, le profil et les résultats de quiz.
- **Illustrations** : bannières SVG inline dédiées à chaque événement/époque — pas de dépendance à des images externes éphémères (ce sandbox de développement bloque d'ailleurs Wikimedia/Wikipedia par politique réseau ; de vraies photos nécessiteraient de les déposer manuellement dans `app/static/`).
- **Calendrier "aujourd'hui dans l'histoire" réel** : 45 événements documentés (avant/pendant/après, récit, personnages, lieu, quiz dédié) répartis sur l'année et sur tous les continents (Europe, Amériques précolombiennes et coloniales, Afrique, Asie, Moyen-Orient, Océanie, Caraïbes), de l'Antiquité (79, 476, -44) à la fin du XXe siècle. L'accueil calcule la vraie date du jour (`datetime.now()`) et affiche l'événement qui tombe exactement ce jour-là ; à défaut, un événement « à la une » tourne quotidiennement (jamais présenté comme s'étant produit ce jour précis). Tout événement listé (recherche, filtres, accueil) est trié chronologiquement par la vraie date historique (`app/events.py:chronological_key`), jamais par ordre d'écriture. Un événement dont le jour exact n'est pas fiable historiquement peut être marqué `"approximate": True` (voir commentaire dans `app/data.py`) : il reste consultable partout (recherche, filtres, carte) mais n'apparaît jamais comme « événement du jour ».
- **Explorateur interactif** : recherche en texte libre (insensible aux accents/casse), filtres par catégorie et par époque (cliquer une carte d'époque filtre réellement), bascule Frise Chronologique / Carte Interactive — avec un planisphère stylisé en fond (continents dessinés en SVG, pas une simple grille) et des repères cliquables géolocalisés (approximativement) pour chaque événement —, et une grille « Collections Phares » pointant vers de vraies fiches événement (chute de Rome en 476, brevet de la machine à vapeur de Watt en 1769, découverte de la tombe de Toutânkhamon en 1922).

## Sécurité

- Mots de passe hashés avec `werkzeug.security` (scrypt), jamais stockés en clair.
- Formulaires validés côté serveur (unicité identifiant/email, complexité du mot de passe) via Flask-WTF, avec protection CSRF sur tous les formulaires.
- Sessions gérées par Flask-Login (`remember me`, pages protégées par `@login_required`).
- Réinitialisation de mot de passe par jeton signé (`itsdangerous`) à expiration ; le message de confirmation est identique que l'email existe ou non (pas d'énumération de comptes).

### Lancer le projet en local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# éditer .env et définir SECRET_KEY (python -c "import secrets; print(secrets.token_hex(32))")

python run.py
```

Puis ouvrir `http://localhost:5000/auth/inscription`.

Sans configuration SMTP (`MAIL_SERVER` non défini dans `.env`), le lien de réinitialisation de mot de passe est simplement écrit dans les logs de l'application au lieu d'être envoyé par email — pratique pour le développement local.

### Déployer sur Render (gratuit)

Le dépôt est prêt pour Render : `requirements.txt` (avec `gunicorn`), `Procfile` (`web: gunicorn run:app`) et `runtime.txt` (version Python) sont déjà en place.

Sur [render.com](https://render.com) → **New → Web Service**, renseigner :

| Champ | Valeur |
|---|---|
| Source / Repository | `Kraakimbo/Chronos` |
| Branch | `main` (ou la branche à déployer) |
| Language / Runtime | **Python 3** |
| Region | la plus proche de toi |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn run:app` |
| Instance Type | **Free** |

Puis dans l'onglet **Environment**, ajouter les variables :

| Clé | Valeur |
|---|---|
| `SECRET_KEY` | une valeur générée avec `python -c "import secrets; print(secrets.token_hex(32))"` |
| `FLASK_ENV` | `production` |

`DATABASE_URL`, `MAIL_SERVER` et les autres variables de `.env.example` sont optionnelles : sans elles, l'app utilise SQLite et journalise les liens de réinitialisation de mot de passe dans les logs Render au lieu de les envoyer par email.

Dans **Settings → Health Check Path**, mettre `/auth/connexion` (la route `/` redirige vers la connexion si non authentifié, ce que le health check par défaut sur `/` peut mal interpréter).

Cliquer sur **Create Web Service** : Render construit et démarre l'app, puis fournit une URL publique du type `https://chronos-xxxx.onrender.com`.

⚠️ **Persistance** : le plan gratuit a un disque éphémère — la base SQLite (et donc les comptes créés) est réinitialisée à chaque redéploiement ou redémarrage après inactivité. Pour une démo qui doit garder ses données, ajouter une base Postgres gratuite Render et définir `DATABASE_URL` avec l'URL fournie (nécessite d'ajouter `psycopg2-binary` à `requirements.txt`).

#### Compte de connexion sans passer par l'inscription

Pour te connecter directement sans remplir le formulaire `/auth/inscription`, ajoute ces variables dans **Environment** sur Render (voir `app/seed.py`) :

| Clé | Valeur |
|---|---|
| `ADMIN_USERNAME` | l'identifiant que tu veux |
| `ADMIN_EMAIL` | ton email |
| `ADMIN_PASSWORD` | un mot de passe (8+ caractères, majuscule, minuscule, chiffre) |

Au prochain déploiement/redémarrage, ce compte est créé automatiquement s'il n'existe pas encore. Va ensuite sur `/auth/connexion` avec ces identifiants. C'est un compte utilisateur classique (le projet n'a pas de rôle "administrateur" avec des permissions particulières côté app) — juste un raccourci pour éviter de repasser par le formulaire d'inscription à chaque redéploiement, puisque le disque gratuit de Render efface la base à chaque redémarrage.

⚠️ **Le mot de passe est resynchronisé à chaque démarrage** sur la valeur courante de `ADMIN_PASSWORD` (tant que l'identifiant *et* l'email correspondent exactement à un compte déjà créé) : change la variable dans Render puis redéploie, pas besoin de supprimer le compte avant. En contrepartie, si tu changes ce mot de passe *depuis l'app* (page profil, mot de passe oublié) sans retirer la variable d'environnement, il sera écrasé par `ADMIN_PASSWORD` au prochain redémarrage — retire la variable une fois que tu n'as plus besoin de ce raccourci. Si l'identifiant ou l'email est déjà pris par un **autre** compte (un vrai utilisateur inscrit normalement), ce compte-là n'est jamais modifié ; le bootstrap est simplement ignoré (visible dans les logs).

Pour un **deuxième compte** (ou plus), ajoute les mêmes 3 variables avec un suffixe `_2`, `_3`, etc. — pas dans les mêmes cases, chaque compte a son propre trio de variables :

| Clé | Valeur |
|---|---|
| `ADMIN_USERNAME_2` | identifiant du 2e compte |
| `ADMIN_EMAIL_2` | son email |
| `ADMIN_PASSWORD_2` | son mot de passe |

Continue avec `_3`, `_4`... pour d'autres comptes (jusqu'à 10 pris en charge).

### Structure

```
app/
  __init__.py             # application factory (db, login manager, mail, CSRF, blueprints)
  models.py                # modèle User (auth + XP/tokens/série + jeton de reset)
  data.py                   # contenu de démo (événements, quiz) — futur CMS/DB
  email.py                   # envoi (ou log local) de l'email de réinitialisation
  auth/
    forms.py                # formulaires inscription / connexion / reset
    routes.py                # /auth/inscription, /connexion, /deconnexion, /mot-de-passe-oublie, /reinitialiser/<token>
  main/
    routes.py                # accueil, explorateur, fiche événement, quiz, profil
  templates/
    base.html                 # layout pages d'auth (formulaire centré)
    base_app.html              # layout applicatif (nav desktop/mobile, palette Chronos complète)
    auth/                       # pages d'inscription/connexion/reset
    pages/                       # accueil, explorer, event_detail, quiz, profile
    email/                        # gabarit de l'email de réinitialisation
```
