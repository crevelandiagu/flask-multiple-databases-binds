from extensions.extensions_task import scheduler
from .utils import TimeSchedule
import datetime
from .handler_task import TaskGetDataCache


data_cache = TaskGetDataCache()

@scheduler.task('cron',
                id='internal',
                second="59",
                start_date=TimeSchedule().start_date(),
                end_date=TimeSchedule().end_date()
                )
def task_data():
    """Sample task 1.

    Added when app starts.
    """
    # hacer etl
    data_cache.status_data()
    print("running task_data_polygon!", datetime.datetime.now())
    print("scheduler.app.config", datetime.datetime.now())




def task2():
    """Sample task 2.

    Added when /add url is visited.
    """
    print("running task 2!")  # noqa: T001