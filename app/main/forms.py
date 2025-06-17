from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import InputRequired, Length


class CreateTodoForm(FlaskForm):  # (1.)
    description = StringField(validators=[InputRequired(), Length(min=5)])  # (2.)
    submit = SubmitField("Create")
