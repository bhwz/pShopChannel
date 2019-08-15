from flask import Blueprint, abort, render_template, request
from flask_login import current_user

from app.models import Product

blueprint = Blueprint('manage', __name__, url_prefix='/manage')


@blueprint.route('/dashboard', methods=['GET'])
def overview():
    if not current_user.admin:
        abort(404)
        return ''

    return render_template('dashboard.html', title='Dashboard')


@blueprint.route('/inventory', methods=['GET'])
def inventory():
    if not current_user.admin:
        abort(404)
        return ''

    return render_template('inventory.html', title='Inventory')


@blueprint.route('/inventory/add', methods=['GET', 'POST'])
def add(pid):
    if not current_user.admin:
        abort(404)
        return ''

    if request.method == 'GET':
        return render_template('product_editor.html', title='Add Product', product=None)


@blueprint.route('/inventory/edit/<int:pid>', methods=['GET', 'POST'])
def edit(pid):
    if not current_user.admin:
        abort(404)
        return ''

    if request.method == 'GET':
        product = Product.query.filter_by(id=pid).first_or_404()
        # Pass Product to pre-populate forms with existing data.
        return render_template('product_editor.html', title='Edit Product', product=product)
