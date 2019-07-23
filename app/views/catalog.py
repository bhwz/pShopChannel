from flask import render_template, Blueprint, request, url_for

from app.models import Product

blueprint = Blueprint('catalog', __name__, url_prefix='/catalog')


@blueprint.route('', methods=['GET'])
def browse():
    search = request.args.get('search', None, type=str)
    page = request.args.get('page', 1, type=int)
    max_results = 8
    # TODO: More filtering based on search.
    products = Product.query.filter_by(parent_id=None, published=True).paginate(page, max_results, False)
    next_url = url_for('catalog.browse', page=products.next_num) if products.has_next else None
    prev_url = url_for('catalog.browse', page=products.prev_num) if products.has_prev else None
    title = 'Search: ' + search if search else 'Catalog'

    return render_template(
        'storefront/catalog.html', title=title, search=search, products=products.items, next_url=next_url, prev_url=prev_url
    )


@blueprint.route('/product/<int:pid>', methods=['GET'])
def product(pid):
    return render_template('storefront/product.html')
