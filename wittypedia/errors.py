from flask import render_template
from wittypedia import app, db
from flask_wtf.csrf import CSRFError


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.errorhandler(CSRFError)
def handle_csrf_error(error):
    return render_template("csrf.html"), 404
