import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("dev_test1")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.schedule_beat = {
    'every-15-seconds':{
        'task':'mytestApis.tasks.test_email_notification',
        'schedule': 15,
        # 'args':('email',) #this is used if the function has an argument
        'args': (),
    }
}


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
