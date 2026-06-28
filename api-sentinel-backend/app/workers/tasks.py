from celery import shared_task
import logging
from uuid import UUID
from app.db.session import SessionLocal
from app.services.scan_service import ScanService

logger = logging.getLogger(__name__)

@shared_task
def run_scan(scan_id : UUID)-> None:
    db = SessionLocal()

    try : 
        service = ScanService(db)
        service.start_scan(scan_id)
        logger.info("Started scan %s", scan_id)
    except Exception:
        db.rollback()
        logger.exception(
        "Failed to start scan %s",
        scan_id,)
        raise

    finally:
        db.close()