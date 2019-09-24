from flask_wtf import FlaskForm
from wtforms import validators, SubmitField, StringField, IntegerField


class OrderForm(FlaskForm):
    item = IntegerField('Item', validators=[
        validators.DataRequired(message='Please pick a variation from the drop down first.')
    ])
    quantity = IntegerField('Quantity', validators=[
        validators.DataRequired(message='Please specify how many of this item you wish to order.'),
        validators.NumberRange(message='Please specify at least one or more to place this order.', min=1)
    ])
    notes = StringField('Notes')
    submit = SubmitField('Order')
