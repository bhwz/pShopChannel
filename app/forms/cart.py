from flask_wtf import FlaskForm
from wtforms import validators, SubmitField, StringField, IntegerField


class AddToCartForm(FlaskForm):
    item = IntegerField('Item', validators=[
        validators.DataRequired(message='Please pick an item to add to your cart first.')
    ])
    quantity = IntegerField('Quantity', validators=[
        validators.DataRequired(message='Please specify how many of this item you wish to add to your cart.'),
        validators.NumberRange(message='Quantity must be more than none in order to be added to your cart.', min=1)
    ])
    notes = StringField('Notes')
    submit = SubmitField('Add To Cart')
