from celery import Celery

from app.core.config import settings


celery_app = Celery(
    "api_sentinel",
    broker=settings.REDIS_URL,
    # We are not providing any backend url because our application is directly polling from the database and we do not need any other service as backend
)

celery_app.autodiscover_tasks(
    [
        "app.workers"
    ]
)

celery_app.set_default()