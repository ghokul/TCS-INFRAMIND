from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class stackcreationForm(FlaskForm):
    Description = StringField('Description',validators=[DataRequired(), Length(min=2, max=20)])
    KeyPair = StringField('KeyPair',validators=[DataRequired(), Length(min=2, max=20)])
    InstanceType = StringField('InstanceType',validators=[DataRequired(), Length(min=2, max=20)])
    DBname = StringField('DBname',validators=[DataRequired(), Length(min=2, max=20)])
    DBuser = StringField('DBuser',validators=[DataRequired(), Length(min=2, max=20)])

    DBpassword = PasswordField('DBpassword',validators=[DataRequired()])
    DBRootPassword = PasswordField('DBRootPassword',validators=[DataRequired()])

    CreateStack= SubmitField('CREATE')


