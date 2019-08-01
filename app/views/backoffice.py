from flask import render_template, Blueprint

blueprint = Blueprint('backoffice', __name__, url_prefix='/backoffice')


@blueprint.route('dash', methods=['GET'])
def dashboard():
    return render_template('backoffice/dashboard.html', title='Dashboard')
