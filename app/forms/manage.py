from flask_wtf import FlaskForm
from wtforms import validators, SubmitField, BooleanField, StringField, IntegerField


class EditInventoryForm(FlaskForm):
    parent_id = IntegerField('Parent Id')
    published = BooleanField('Published', validators=[
        validators.DataRequired(message='Please specify if the product is published.')
    ])
    name = StringField('Name', validators=[
        validators.DataRequired(message='Please give the product a name.')
    ])
    stock = IntegerField('Stock')
    price = IntegerField('Price')
    description = StringField('Description', validators=[
        validators.DataRequired(message='Please give the product a description.')
    ])
    customizable = BooleanField('Customizable', validators=[
        validators.DataRequired(message='Please specify if the product is customizable.')
    ])
    submit = SubmitField('Submit')
