from flask import Blueprint, abort, render_template, request, url_for, redirect
from flask_login import current_user

from app import db
from app.forms.error import flash_errors
from app.forms.manage import EditProductForm, EditPageForm
from app.models import Product, Page

blueprint = Blueprint('manage', __name__, url_prefix='/manage')


@blueprint.route('/dashboard', methods=['GET'])
def dashboard():
    if not current_user.admin:
        abort(404)
        return ''

    return render_template('manage/dashboard.html', title='Dashboard')


@blueprint.route('/inventory', methods=['GET'])
def inventory():
    if not current_user.admin:
        abort(404)
        return ''

    page = request.args.get('page', 1, type=int)
    max_results = 32
    products = Product.query.paginate(page, max_results, False)
    next_url = url_for('manage.inventory', page=products.next_num) if products.has_next else None
    prev_url = url_for('manage.inventory', page=products.prev_num) if products.has_prev else None

    return render_template(
        'manage/inventory.html',
        title='Inventory',
        products=products.items,
        next_url=next_url,
        prev_url=prev_url
    )


@blueprint.route('/product', methods=['GET', 'POST'])
def product():
    if not current_user.admin:
        abort(404)
        return ''

    form = EditProductForm(request.form)

    if request.method == 'GET':
        target = request.args.get('edit', None, type=int)
        editable_product = Product.query.filter_by(id=target).first_or_404() if target else None

        title = 'Edit Product' if editable_product else 'Add Product'

        return render_template(
            'manage/product.html',
            title=title,
            product=editable_product,
            form=form
        )

    if not form.validate_on_submit():
        flash_errors(form)
        return redirect(url_for('manage.product'))

    target = request.args.get('edit', None, type=int)
    editable_product = Product.query.filter_by(id=target).first_or_404() if target else Product()

    editable_product.published = form.published.data
    editable_product.name = form.name.data
    editable_product.stock = form.stock.data
    editable_product.price = form.price.data
    editable_product.description = form.description.data
    editable_product.notes_enabled = form.notes_enabled.data

    db.session.add(editable_product)
    db.session.commit()
    return redirect(url_for('manage.inventory'))


@blueprint.route('/special-pages', methods=['GET'])
def special_pages():
    if not current_user.admin:
        abort(404)
        return ''

    pages = Page.query.all()

    return render_template('manage/special_pages.html', title='Special Pages', pages=pages)


@blueprint.route('/page', methods=['GET', 'POST'])
def page():
    if not current_user.admin:
        abort(404)
        return ''

    form = EditPageForm(request.form)

    if request.method == 'GET':
        target = request.args.get('edit', None, type=int)
        editable_page = Page.query.filter_by(id=target).first_or_404() if target else None

        title = 'Edit Page' if editable_page else 'Add Page'

        return render_template(
            'manage/page.html',
            title=title,
            page=editable_page,
            form=form
        )

    if not form.validate_on_submit():
        flash_errors(form)
        return redirect(url_for('manage.page'))

    target = request.args.get('edit', None, type=int)
    editable_page = Page.query.filter_by(id=target).first_or_404() if target else Page()

    editable_page.published = form.published.data
    editable_page.title = form.title.data
    editable_page.slug = form.slug.data
    editable_page.content = form.content.data

    db.session.add(editable_page)
    db.session.commit()
    return redirect(url_for('manage.special_pages'))
