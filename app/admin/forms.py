from flask_wtf import FlaskForm
from wtforms import BooleanField, FloatField, IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, Optional


class EventEditForm(FlaskForm):
    title = StringField("Titre", validators=[DataRequired()])
    month = IntegerField("Mois", validators=[DataRequired(), NumberRange(min=1, max=12)])
    day = IntegerField("Jour", validators=[DataRequired(), NumberRange(min=1, max=31)])
    year = IntegerField(
        "Année",
        validators=[DataRequired()],
        description="Négative pour avant J.-C. (ex : -44 pour 44 av. J.-C.)",
    )
    date_label = StringField(
        "Date affichée", validators=[DataRequired()], description='Ex : "14 Juillet 1789"'
    )
    era = StringField("Époque", validators=[DataRequired()])
    era_key = StringField(
        "Clé d'époque",
        validators=[DataRequired()],
        description="prehistoire / antiquite / moyen-age / renaissance / epoque-contemporaine",
    )
    category = StringField("Catégorie", validators=[DataRequired()])
    location = StringField("Lieu (complet)", validators=[DataRequired()])
    location_label = StringField("Lieu (affiché sur la carte)", validators=[Optional()])
    map_pos_x = FloatField("Position carte X (%)", validators=[Optional()])
    map_pos_y = FloatField("Position carte Y (%)", validators=[Optional()])
    approximate = BooleanField(
        "Date approximative",
        description="Coché : le jour exact n'est pas fiable, l'événement n'apparaît jamais "
        "comme \"événement du jour\".",
    )
    summary = TextAreaField("Résumé court", validators=[DataRequired()])
    before = TextAreaField("Avant", validators=[DataRequired()])
    during = TextAreaField("Pendant", validators=[DataRequired()])
    after = TextAreaField("Après", validators=[DataRequired()])
    narrative = TextAreaField(
        "Récit complet",
        validators=[DataRequired()],
        description="Un paragraphe par bloc, séparés par une ligne vide.",
    )
    why_it_matters = TextAreaField("Pourquoi c'est important", validators=[DataRequired()])
    characters = TextAreaField(
        "Personnages clés",
        validators=[Optional()],
        description="Un par ligne : Nom | Rôle | Emoji | #couleur (ex : Louis XVI | Roi de "
        "France | 👑 | #FFF3C4)",
    )
    quiz_slug = StringField("Slug du quiz associé", validators=[Optional()])
    submit = SubmitField("Enregistrer")


class LevelContentForm(FlaskForm):
    summary = TextAreaField("Résumé court", validators=[DataRequired()])
    before = TextAreaField("Avant", validators=[DataRequired()])
    during = TextAreaField("Pendant", validators=[DataRequired()])
    after = TextAreaField("Après", validators=[DataRequired()])
    narrative = TextAreaField(
        "Récit complet",
        validators=[DataRequired()],
        description="Un paragraphe par bloc, séparés par une ligne vide.",
    )
    why_it_matters = TextAreaField("Pourquoi c'est important", validators=[DataRequired()])
    submit = SubmitField("Enregistrer")
