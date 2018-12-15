from flask import (Blueprint, render_template, make_response,
                   url_for, request, abort, flash, redirect)
from flask_login import (current_user, login_required, login_url)


frontend = Blueprint('frontend', __name__, template_folder='templates')


@frontend.route('/favicon.ico')
def favicon_ico():
    return redirect(url_for('static', filename='favicon.ico'))


@frontend.route('/robots.txt')
def robots_txt():
    return 'User-agent: *\nDisallow: \n'


@frontend.route('/')
def index():
    return render_template('frontend/index.html', user=current_user,
                           mainPage=True)
