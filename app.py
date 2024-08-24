from flask_cors import CORS
from internal import my_app
from flask_openapi3 import OpenAPI, Info
from extensions.extensions_task import scheduler
from extensions.database import db

ACTIVATE_ENDPOINTS = (('/', my_app),)

def create_app():
    info = Info(title="my_app", version="0.3.2")

    app = OpenAPI(__name__,
                  info=info,
                  doc_prefix="/docs"
                  )
    app.config.from_object('settings.Config')

    db.init_app(app)
    for url, blueprint in ACTIVATE_ENDPOINTS:
        app.register_api(blueprint)
    app.url_map.strict_slashes = False

    CORS(app, resources={r'/*': {'origins': '*'}}, send_wildcard=True)

    scheduler.init_app(app)
    scheduler.start()
    return app


def setup_database(app):
    with app.app_context():
        db.create_all()
