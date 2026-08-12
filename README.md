# Chronos

Application musée d'histoire gamifiée — design issu de Google Stitch, backend Flask.

## Fonctionnalités

- **Comptes utilisateurs** : inscription (identifiant, email, mot de passe, niveau d'étude), connexion, déconnexion, suppression de compte.
- **Mot de passe oublié** : demande de réinitialisation par email avec lien à durée de vie limitée (30 min).
- **Pages câblées** : accueil (événement du jour), explorateur (frise des époques), fiche événement, quiz (question aléatoire à chaque visite parmi plusieurs, récompenses XP/tokens/série), profil avec statistiques réelles, choix d'avatar et historique d'activité (connexions, tentatives échouées, réinitialisations de mot de passe). Toutes protégées par connexion.
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

flask --app run.py db upgrade  # crée les tables (voir "Migrations de base de données" plus bas)
python run.py
```

Puis ouvrir `http://localhost:5000/auth/inscription`.

Sans configuration email (`BREVO_API_KEY` non défini dans `.env`), le lien de réinitialisation de mot de passe est simplement écrit dans les logs de l'application au lieu d'être envoyé par email — pratique pour le développement local.

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

`DATABASE_URL`, `BREVO_API_KEY` et les autres variables de `.env.example` sont optionnelles : sans elles, l'app utilise SQLite et journalise les liens de réinitialisation de mot de passe dans les logs Render au lieu de les envoyer par email.

Dans **Settings → Health Check Path**, mettre `/auth/connexion` (la route `/` redirige vers la connexion si non authentifié, ce que le health check par défaut sur `/` peut mal interpréter).

Cliquer sur **Create Web Service** : Render construit et démarre l'app, puis fournit une URL publique du type `https://chronos-xxxx.onrender.com`.

⚠️ **Persistance** : le plan gratuit a un disque éphémère — la base SQLite (et donc les comptes créés) est réinitialisée à chaque redéploiement ou redémarrage après inactivité. Pour garder les comptes durablement, voir la section [Base de données persistante](#base-de-données-persistante) ci-dessous.

#### Base de données persistante

`requirements.txt` inclut déjà `psycopg2-binary` : il suffit de définir `DATABASE_URL` sur Render pour que l'app bascule sur Postgres au prochain redémarrage, sans autre changement de code.

Options :

- **[Neon](https://neon.tech) ou [Supabase](https://supabase.com)** (recommandé pour rester gratuit durablement) : créer un projet Postgres gratuit, copier la *connection string* (`postgresql://...`) fournie, la coller dans `DATABASE_URL` sur Render.
- **Render Postgres** (tout centralisé au même endroit) : **New → PostgreSQL** sur Render, puis copier l'*Internal Database URL* dans `DATABASE_URL` du service web. Le plan gratuit Render Postgres expire après 90 jours (à recréer) ; le plan payant (~7 $/mois) est permanent avec backups automatiques.

Dans les deux cas, redéployer (ou redémarrer) le service web après avoir ajouté `DATABASE_URL` : les migrations (voir ci-dessous) créent automatiquement les tables sur la nouvelle base au démarrage.

#### Migrations de base de données

Le schéma est géré par [Flask-Migrate](https://flask-migrate.readthedocs.io/) (Alembic), pas par `db.create_all()` : `db.create_all()` crée les tables manquantes mais **ne modifie jamais** une table déjà existante, donc toute nouvelle colonne ajoutée à un modèle (`app/models.py`) serait silencieusement absente en production tant que la base n'est pas persistante ; une fois une vraie base persistante en place (Postgres), ça casse le déploiement au lieu de simplement ne rien faire — c'est exactement ce qui est arrivé lors de l'ajout de `users.email_confirmed`.

Le `Procfile` lance désormais `flask db upgrade` avant Gunicorn à chaque déploiement Render, donc les migrations s'appliquent automatiquement sans action manuelle pour les prochains changements de schéma.

**Après avoir modifié un modèle** dans `app/models.py` :

```bash
flask --app run.py db migrate -m "description du changement"
flask --app run.py db upgrade   # applique en local pour vérifier avant de commit
```

Relis toujours le fichier généré dans `migrations/versions/` avant de le commiter — l'autogénération d'Alembic est fiable pour les cas simples (nouvelle colonne, nouvelle table) mais pas infaillible (renommages, contraintes complexes).

Les tests (`tests/conftest.py`) ne passent pas par les migrations : ils recréent un schéma frais avec `db.create_all()` à chaque run, pour toujours refléter l'état actuel des modèles sans dépendre de l'historique des migrations.

#### Envoi réel des emails (mot de passe oublié)

Le code envoie l'email via l'**API HTTPS de Brevo** (voir `app/email.py`) dès que `BREVO_API_KEY` est configuré — aucun développement n'est nécessaire, seulement les variables d'environnement sur Render.

⚠️ **Pas de SMTP classique** : Render bloque les connexions sortantes sur les ports SMTP habituels (25/465/587) sur ses services web, donc `smtp-relay.brevo.com:587` (ou tout autre fournisseur SMTP) ne fonctionnera jamais depuis Render (timeout de connexion). C'est pour ça que le code passe par l'API HTTPS de Brevo (port 443, jamais bloqué) plutôt que par du SMTP.

Avec [Brevo](https://www.brevo.com) (ex-Sendinblue, 300 emails/jour gratuits à vie) :
1. Créer un compte, valider un email expéditeur (ou un domaine) dans **Expéditeurs, domaines et IPs dédiées**.
2. Récupérer une **clé API** (pas la clé SMTP) dans **Paramètres → SMTP & API → onglet API Keys** — génère-en une nouvelle si besoin.
3. Définir sur Render :

| Clé | Valeur |
|---|---|
| `BREVO_API_KEY` | ta clé API Brevo |
| `MAIL_DEFAULT_SENDER` | l'adresse expéditrice validée dans Brevo |

Pour un autre fournisseur d'email transactionnel (Resend, SendGrid, Amazon SES, ...), le principe est le même : utiliser son API HTTPS plutôt que son SMTP, tant que l'app tourne sur Render — ça demanderait d'adapter `app/email.py` au format de l'API choisie.

#### Suivi des erreurs (Sentry)

Sans configuration, les erreurs de production ne sont visibles que dans les logs Render (qu'il faut consulter manuellement). Pour les recevoir automatiquement avec la stack trace complète :

1. Créer un compte gratuit sur [sentry.io](https://sentry.io) (5 000 erreurs/mois gratuites), créer un projet **Flask**.
2. Copier le **DSN** fourni (URL du type `https://xxxx@xxxx.ingest.sentry.io/xxxx`).
3. Sur Render, ajouter la variable `SENTRY_DSN` avec cette valeur.

Sans `SENTRY_DSN` (développement local, tests), rien n'est envoyé nulle part — comportement inchangé.

#### Compte de connexion sans passer par l'inscription

Pour te connecter directement sans remplir le formulaire `/auth/inscription`, ajoute ces variables dans **Environment** sur Render (voir `app/seed.py`) :

| Clé | Valeur |
|---|---|
| `ADMIN_USERNAME` | l'identifiant que tu veux |
| `ADMIN_EMAIL` | ton email |
| `ADMIN_PASSWORD` | un mot de passe (8+ caractères, majuscule, minuscule, chiffre) |

Au prochain déploiement/redémarrage, ce compte est créé automatiquement s'il n'existe pas encore. Va ensuite sur `/auth/connexion` avec ces identifiants. C'était à l'origine un simple raccourci pour éviter de repasser par le formulaire d'inscription à chaque redéploiement (puisque le disque gratuit de Render effaçait la base à chaque redémarrage) ; ces comptes ont maintenant aussi le rôle **admin** (`is_admin`, voir section suivante), qui donne accès à `/admin/evenements`.

⚠️ **Le mot de passe est resynchronisé à chaque démarrage** sur la valeur courante de `ADMIN_PASSWORD` (tant que l'identifiant *et* l'email correspondent exactement à un compte déjà créé) : change la variable dans Render puis redéploie, pas besoin de supprimer le compte avant. En contrepartie, si tu changes ce mot de passe *depuis l'app* (page profil, mot de passe oublié) sans retirer la variable d'environnement, il sera écrasé par `ADMIN_PASSWORD` au prochain redémarrage — retire la variable une fois que tu n'as plus besoin de ce raccourci. Si l'identifiant ou l'email est déjà pris par un **autre** compte (un vrai utilisateur inscrit normalement), ce compte-là n'est jamais modifié ; le bootstrap est simplement ignoré (visible dans les logs).

Pour un **deuxième compte** (ou plus), ajoute les mêmes 3 variables avec un suffixe `_2`, `_3`, etc. — pas dans les mêmes cases, chaque compte a son propre trio de variables :

| Clé | Valeur |
|---|---|
| `ADMIN_USERNAME_2` | identifiant du 2e compte |
| `ADMIN_EMAIL_2` | son email |
| `ADMIN_PASSWORD_2` | son mot de passe |

Continue avec `_3`, `_4`... pour d'autres comptes (jusqu'à 10 pris en charge).

#### Éditer le contenu (panneau admin)

Les 45 événements du calendrier (`app/data.py` à l'origine) et leurs 4 variantes de texte par niveau d'étude (`app/level_content.py` à l'origine) sont maintenant en base de données, éditables sans redéploiement via **`/admin/evenements`** (lien "Admin" dans la nav desktop, visible seulement pour un compte admin). Cette table est peuplée automatiquement une seule fois au premier démarrage à partir du contenu existant dans le code ; les éditions faites depuis l'admin ne sont ensuite jamais écrasées par un redéploiement.

- **Texte de référence** (`/admin/evenements/<slug>/modifier`) : titre, dates, lieu, résumé/récit/personnages — c'est ce texte qui s'affiche sur l'aperçu public (`/decouvrir/...`).
- **Texte par niveau d'étude** (`/admin/evenements/<slug>/niveau/<niveau>`) : la réécriture spécifique à chaque niveau (enfant/collège/lycée/étudiant-adulte), affichée aux utilisateurs connectés selon leur profil. Sans texte spécifique pour un niveau donné, le texte de référence sert de repli.
- **Illustrations** (`/admin/evenements/<slug>/illustrations`) : les images de la "Galerie d'archives" en bas de fiche (photo/tableau/portrait — `app/event_images.py` à l'origine), avec URL, légende, description (texte affiché au survol/sur la page dédiée — vide = texte générique par défaut selon le type d'image), crédit et licence. Laisser l'URL vide retire l'image de ce type. La meilleure image disponible sert aussi de bannière de couverture.

Pour donner le rôle admin à un compte qui n'est pas un compte bootstrap `ADMIN_*` (ex. ton compte personnel déjà inscrit normalement), passe par le SQL Editor de Supabase :

```sql
UPDATE users SET is_admin = true WHERE username = 'ton_identifiant';
```

Les questions de quiz (`app/data.py:QUIZ_QUESTIONS`, `app/level_content.py:QUIZ_BY_LEVEL`) restent en code pour l'instant, hors périmètre de cette première étape.

### Structure

```
migrations/                 # historique des migrations Alembic (voir "Migrations de base de données")
app/
  __init__.py             # application factory (db, migrate, login manager, mail, CSRF, blueprints)
  models.py                # User, AccountEvent, HistoricalEvent, EventLevelContent
  audit.py                  # journalisation des événements de compte (connexion, reset, ...)
  data.py                   # source du seed initial des événements (voir app/seed.py) + banque de quiz
  level_content.py           # source du seed initial du texte par niveau + résolution des overrides (DB)
  email.py                   # envoi (ou log local) de l'email de réinitialisation
  seed.py                    # comptes bootstrap ADMIN_*, peuplement initial des événements/textes par niveau
  admin/
    forms.py                # formulaires d'édition événement / texte par niveau
    routes.py                # /admin/evenements, /admin/evenements/<slug>/modifier|niveau/<niveau>
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

### App mobile (App Store / Google Play)

Le dossier [`mobile/`](mobile/README.md) contient un wrapper
[Capacitor](https://capacitorjs.com/) qui embarque ce même site (déployé sur
Render) dans une vraie app iOS/Android — une seule codebase Flask reste la
source de vérité pour le contenu, l'auth et la gamification. Voir
`mobile/README.md` pour la procédure complète (build Android via Android
Studio, build iOS via Xcode sur Mac, soumission App Store Connect / Google
Play Console).
