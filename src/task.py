from celery import Celery
from celery.schedules import crontab
from os import system


app = Celery(
    'task', 
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
    )


@app.task
def check():
    cmd = "python3 manage.py check_date"
    return system(cmd)


@app.task
def add_holidays():
    cmd = "python3 manage.py add_holidays"
    return system(cmd)


app.conf.beat_schedule = {
    "task1": {
        "task": "task.check",
        "schedule": crontab(minute=0, hour="*/1"),
    },
    "task2":{
        "task": "task.add_holidays",
        "schedule": crontab(0, 0, day_of_month='1'),
    }
}