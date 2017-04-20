SECRET_KEY = 'he  setting must not be empty.'
CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']

CELERY_RESULT_BACKEND = 'django-db'
# CELERY_RESULT_BACKEND = 'django-cache'
# CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'

CELERY_TASK_SERIALIZER = 'json'
