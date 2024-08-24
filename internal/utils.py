import datetime

class TimeSchedule:
    def __init__(self):
        pass

    def start_date(self):
        dt = datetime.datetime.now()
        dt = dt.replace(hour=11, minute=13, second=0)
        return dt

    def end_date(self):
        dt = datetime.datetime.now()
        dt = dt.replace(hour=23, minute=16, second=0)
        return dt
