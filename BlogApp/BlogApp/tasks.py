from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def add_numbers(x, y):
    return x + y