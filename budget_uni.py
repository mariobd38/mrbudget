from flask import render_template, abort, Blueprint
from jinja2 import TemplateNotFound

budget_uni_bp = Blueprint('budget_uni',__name__)

@budget_uni_bp.route('/budget_university',methods=['GET'])
def budget_uni():
    try:
        return render_template('budget_university/budget_uni.html')
    except TemplateNotFound:
            abort(404)