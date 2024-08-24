from environs import Env
env = Env()
env.read_env()

class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'do-i-really-need-this'
    FLASK_SECRET = SECRET_KEY

    SQLALCHEMY_DATABASE_URI = env('DATABASE_URL','postgresql://postgres:postgres@localhost:5432/data_db' )
    SQLALCHEMY_BINDS = {
        'cache': 'sqlite:///cache_task.db'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True
    CORS_HEADERS="*"
    TIMEZONE = 'America/Bogota'



class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False


