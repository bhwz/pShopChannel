from flask import render_template, Blueprint, request

blueprint = Blueprint('catalog', __name__, url_prefix='/catalog')


@blueprint.route('/browse', methods=['GET'])
def catalog():
    return render_template('storefront/catalog.html')


@blueprint.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return render_template('storefront/search.html', query=query)

    # TODO: Do Search
    result = 'Some results.'
    return render_template('storefront/search.html', query=query, result=result)


@blueprint.route('/product/<int:pid>', methods=['GET'])
def product(pid):
    return render_template('storefront/product.html')
