import commonmark
from flask import render_template, Blueprint, abort

from app.models import Page

blueprint = Blueprint('pages', __name__)


@blueprint.route('/', methods=['GET'])
def landing():
    return render_template('storefront/landing.html', title='Home')


@blueprint.route('/page/<string:slug>', methods=['GET'])
def page(slug):
    p = Page.query.filter_by(slug=slug, published=True).first_or_404()

    return render_template(
        'storefront/pages.html',
        page=p,
        title=p.title,
        rendered_content=commonmark.commonmark(p.content)
    )
