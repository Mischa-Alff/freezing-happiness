import sys
sys._stdout = sys.stdout
sys.stdout = sys.stderr

from flask import Flask
from flask.ext.mongoengine import MongoEngine
import logging

app = Flask(__name__)
app.template_folder = 'templates'
app.config['MONGODB_SETTINGS'] = {'DB':'freezing-happiness'}
app.config['PROPAGATE_EXCEPTIONS'] = True

db = MongoEngine(app)
application = app

def register_blueprints(app):
    from application.main import main
    app.register_blueprint(main)

register_blueprints(app)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='0.0.0.0', port=5000, use_reloader=True)
