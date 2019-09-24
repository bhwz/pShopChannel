from flask_wtf import FlaskForm
from wtforms import validators, SubmitField, BooleanField, StringField, IntegerField


class EditProductForm(FlaskForm):
    parent_id = IntegerField('Parent Id')
    published = BooleanField('Published')
    name = StringField('Name', validators=[
        validators.DataRequired(message='Please give the product a name.')
    ])
    stock = IntegerField('Stock')
    price = IntegerField('Price')
    description = StringField('Description', validators=[
        validators.DataRequired(message='Please give the product a description.')
    ])
    notes_enabled = BooleanField('Notes Enabled')
    submit = SubmitField('Submit')


class EditPageForm(FlaskForm):
    published = BooleanField('Published')
    slug = StringField('Slug', validators=[
        validators.DataRequired(message='A URL slug is required.'),
        validators.Length(message='Please choose a slug shorter than 1024 characters.', max=1024)
    ])
    title = StringField('Title', validators=[
        validators.DataRequired(message='A title is required.')
    ])
    content = StringField('Content', validators=[
        validators.DataRequired(message='Page content is required.')
    ])
    submit = SubmitField('Submit')
