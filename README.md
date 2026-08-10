# Chronos

Application musée d'histoire gamifiée ("On This Day") — design issu de Google Stitch.

## Backend d'authentification

Un backend Flask minimal fournit la création de compte (identifiant + mot de passe) et la connexion :

- Mots de passe hashés avec `werkzeug.security` (scrypt), jamais stockés en clair.
- Formulaires validés côté serveur (unicité identifiant/email, complexité du mot de passe) via Flask-WTF, avec protection CSRF.
- Sessions gérées par Flask-Login (`remember me`, page d'accueil protégée par `@login_required`).
- Choix du niveau d'étude à l'inscription (repris de l'écran d'onboarding Stitch).

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

### Structure

```
app/
  __init__.py        # application factory (db, login manager, CSRF, blueprints)
  models.py           # modèle User
  auth/
    forms.py          # formulaires d'inscription / connexion
    routes.py          # routes /auth/inscription, /auth/connexion, /auth/deconnexion
  main/
    routes.py          # route d'accueil protégée
  templates/            # gabarits Jinja2, cohérents avec le design Chronos (or/parchemin)
```
