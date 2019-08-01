from app.views.pages import blueprint as pages_blueprint
from app.views.catalog import blueprint as catalog_blueprint
from app.views.account import blueprint as account_blueprint
from app.views.backoffice import blueprint as backoffice_blueprint


def register_blueprints(app):
    app.register_blueprint(pages_blueprint)
    app.register_blueprint(catalog_blueprint)
    app.register_blueprint(account_blueprint)
    app.register_blueprint(backoffice_blueprint)
