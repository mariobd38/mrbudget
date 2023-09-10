from flask import render_template, abort, Blueprint
from jinja2 import TemplateNotFound

#how it works
how_it_works = Blueprint('how_it_works',__name__)

@how_it_works.route('/info',methods=['GET'])
def info():
    return render_template('how_it_works/info.html')

@how_it_works.route('/payment_tracker',methods=['GET'])
def payment_tracker():
    try:
        return render_template('how_it_works/payment_tracker.html')
    except TemplateNotFound:
            abort(404)

@how_it_works.route('/budget_visualizer',methods=['GET'])
def budget_visualizer():
    try:
        return render_template('how_it_works/budget_visualizer.html')
    except TemplateNotFound:
            abort(404)

@how_it_works.route('/sub_management',methods=['GET'])
def sub_management():
    try:
        return render_template('how_it_works/sub_management.html')
    except TemplateNotFound:
            abort(404)

@how_it_works.route('/alerts',methods=['GET'])
def alerts():
    try:
        return render_template('how_it_works/alerts.html')
    except TemplateNotFound:
            abort(404)

@how_it_works.route('/budget_envelopes',methods=['GET'])
def budget_envelopes():
    try:
        return render_template('how_it_works/budget_envelopes.html')
    except TemplateNotFound:
            abort(404)

@how_it_works.route('/security',methods=['GET'])
def security():
    try:
        return render_template('how_it_works/security.html')
    except TemplateNotFound:
            abort(404)

#budget university
budget_uni_bp = Blueprint('budget_uni',__name__)
@budget_uni_bp.route('/budget_university',methods=['GET'])
def budget_uni():
    try:
        return render_template('budget_university/budget_uni.html')
    except TemplateNotFound:
            abort(404)

#stocks
stocks_bp = Blueprint('stocks',__name__)

@stocks_bp.route('/stocks',methods=['GET'])
def stocks():
    try:
        return render_template('stocks/stocks.html')
    except TemplateNotFound:
            abort(404)

#resources
resources_bp = Blueprint('resources',__name__)

@resources_bp.route('/home_affordability_calc',methods=['GET'])
def home_aff_calc():
    return render_template('resources/home_aff_calc.html')

@resources_bp.route('/loan_repayment_calc',methods=['GET'])
def loan_repay_calc():
    try:
        return render_template('resources/loan_repay_calc.html')
    except TemplateNotFound:
            abort(404)

@resources_bp.route('/currency_converter',methods=['GET'])
def currency_converter():
    try:
        return render_template('resources/currency_converter.html')
    except TemplateNotFound:
            abort(404)