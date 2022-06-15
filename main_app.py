from wittypedia import app, db
from wittypedia.models import Link


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Link': Link}