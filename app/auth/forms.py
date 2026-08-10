from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, RadioField, StringField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Regexp,
    ValidationError,
)

from app.models import STUDY_LEVELS, User

USERNAME_REGEXP = r"^[a-zA-Z0-9_.-]{3,32}$"
# At least 8 chars, one lowercase, one uppercase, one digit.
PASSWORD_REGEXP = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"


class RegistrationForm(FlaskForm):
    username = StringField(
        "Identifiant",
        validators=[
            DataRequired(message="L'identifiant est requis."),
            Regexp(
                USERNAME_REGEXP,
                message="3 à 32 caractères : lettres, chiffres, points, tirets ou underscores.",
            ),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="L'email est requis."),
            Email(message="Adresse email invalide."),
        ],
    )
    password = PasswordField(
        "Mot de passe",
        validators=[
            DataRequired(message="Le mot de passe est requis."),
            Regexp(
                PASSWORD_REGEXP,
                message=(
                    "8 caractères minimum, avec au moins une majuscule, "
                    "une minuscule et un chiffre."
                ),
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirmer le mot de passe",
        validators=[
            DataRequired(message="Merci de confirmer le mot de passe."),
            EqualTo("password", message="Les mots de passe ne correspondent pas."),
        ],
    )
    study_level = RadioField(
        "Niveau d'étude",
        choices=[
            ("enfant", "Enfant (6-10 ans)"),
            ("college", "Collège (11-14 ans)"),
            ("lycee", "Lycée (15-18 ans)"),
            ("etudiant_adulte", "Étudiant / Adulte (+18 ans)"),
        ],
        validators=[DataRequired(message="Choisis un niveau d'étude.")],
    )
    submit = SubmitField("Créer mon compte")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Cet identifiant est déjà pris.")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError("Un compte existe déjà avec cet email.")

    def validate_study_level(self, field):
        if field.data not in STUDY_LEVELS:
            raise ValidationError("Niveau d'étude invalide.")


class LoginForm(FlaskForm):
    identifier = StringField(
        "Identifiant ou email", validators=[DataRequired(message="Champ requis.")]
    )
    password = PasswordField(
        "Mot de passe", validators=[DataRequired(message="Champ requis.")]
    )
    remember_me = BooleanField("Se souvenir de moi")
    submit = SubmitField("Se connecter")
