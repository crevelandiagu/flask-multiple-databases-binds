from flask_openapi3 import APIBlueprint, Tag
from extensions.extensions_task import scheduler
from flask import jsonify
from .task import task2
from .models.sqlite.models import MyModleSqlite

my_app = APIBlueprint('my_app', __name__, url_prefix='/my_app')


task_health_tag = Tag(name="my_app healtcheck", description="my_app")

@my_app.get('/ping', tags=[task_health_tag])
def root():
    """
    Healt Check
    :return: pong
    """
    return 'pong'

task_my_app = Tag(name="Task Schedule task_my_app", description="handler task for task_my_app")

@my_app.get("/add-task", tags=[task_my_app])
def add():
    """Add a task.

    :url: /add/
    :returns: job
    """
    job = scheduler.add_job(
        func=task2,
        trigger="interval",
        seconds=10,
        id="test job 2",
        name="test job 2",
        replace_existing=True,
    )
    return "%s added!" % job.name

@my_app.get("/status-task",tags=[task_my_app])
def status_task():
    job = scheduler.get_job('internal')
    print(job)
    return f'{job}'



