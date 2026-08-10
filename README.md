# Chronos

Application musée d'histoire gamifiée ("On This Day") — design issu de Google Stitch, backend Flask.

## Fonctionnalités

- **Comptes utilisateurs** : inscription (identifiant, email, mot de passe, niveau d'étude), connexion, déconnexion.
- **Mot de passe oublié** : demande de réinitialisation par email avec lien à durée de vie limitée (30 min).
- **Pages câblées** : accueil (événement du jour), explorateur (frise des époques), fiche événement, quiz avec récompenses XP/tokens/série, profil avec statistiques réelles. Toutes protégées par connexion.

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
