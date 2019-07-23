from flask import Blueprint, redirect, url_for, request, render_template, flash
from flask_login import current_user, login_user, logout_user

from app import db
from app.forms.auth import LoginForm, RegisterForm
from app.forms.error import flash_errors
from app.models.order import Order
from app.models.user import User

blueprint = Blueprint('account', __name__, url_prefix='/account')


@blueprint.route('/overview', methods=['GET'])
def overview():
    if not current_user.is_authenticated:
        return redirect(url_for('account.login'))

    orders = Order.query.filter_by(user_id=current_user.id)

    return render_template('storefront/account.html', title='Account', orders=orders)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('pages.overview'))

    form = LoginForm(request.form)

    if request.method == 'GET':
        return render_template('storefront/login.html', title='Login', form=form)

    if not form.validate_on_submit():
        flash_errors(form)
        return redirect(url_for('account.login'))

    user = User.query.filter_by(email=form.email.data).first()

    if user is None or not user.verify_password(form.password.data):
        flash('Invalid email or password.', category='error')
        return redirect(url_for('account.login'))

    login_user(user, remember=form.remember_me.data)

    return redirect(url_for('account.overview'))


@blueprint.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('pages.landing'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('pages.overview'))

    form = RegisterForm(request.form)
    if request.method == 'GET':
        return render_template('storefront/register.html', title='Register', form=form)

    if not form.validate_on_submit():
        flash_errors(form)
        return redirect(url_for('account.register'))

    user = User()
    user.email = form.email.data
    user.set_password(form.password.data)

    db.session.add(user)
    db.session.commit()

    login_user(user)
    return redirect(url_for('account.login'))
