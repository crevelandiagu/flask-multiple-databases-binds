from .models.sqlite.models import MyModleSqlite


class TaskGetDataCache:
    def __init__(self):
        pass

    def status_data(self):
        cache_data = 'CacheMemory.query.all()'
        if not cache_data:
            print("go and get data to populated cahce memory")
            return "the cache is populate"
        return "has data"



