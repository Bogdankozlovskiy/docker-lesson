from celery import Celery
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


app.conf.beat_schedule = {
    "task": {
        "task": "task.check",
        "schedule": 5.0,
   }
}