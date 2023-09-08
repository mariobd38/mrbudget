from flask import render_template, abort, Blueprint
from jinja2 import TemplateNotFound

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