from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def run_scan(scan_id : int):
    print(f"Running scan {scan_id}")