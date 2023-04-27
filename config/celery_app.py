import os
# import celery packages 
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("dev_test1")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.schedule_beat = {
    'every-15-seconds':{  # whatever the name you want
        'task':'mytestApis.tasks.test_email_notification', # name of task with path
        'schedule': crontab(), # crontab() runs the tasks every minute
        # 'args':('email',) #this is used if the function has an argument
        'args': (),
    }
}


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

