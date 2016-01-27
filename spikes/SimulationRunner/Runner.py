import random
import time
from celery import Celery
app = Celery('tasks', backend='db+postgresql://kishorek:password@centnix.eastus.cloudapp.azure.com/celery-tasks', broker='amqp://rabbituser:password@mynix.cloudapp.net//')


@app.task
def run(x):
    random_gen = random.Random()
    print "Stating simulation run"
    random_sleep_time = random_gen.randint(1, 50)
    print "Sleeping for ", random_sleep_time, " seconds"
    time.sleep(random_sleep_time)
    print "Done sleeping"
    return x
