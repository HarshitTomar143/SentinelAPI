from celery import shared_task
import logging
from uuid import UUID
from app.db.session import SessionLocal
from app.services.scan_service import ScanService
from app.services.scanner_service import ScannerService

logger = logging.getLogger(__name__)

@shared_task
def run_scan(scan_id : UUID)-> None:
    db = SessionLocal()

    try : 
        service = ScanService(db)
        scanner_service = ScannerService(db)
        service.start_scan(scan_id)
        logger.info("Started scan %s", scan_id)
        scanner_service.execute(scan_id)
        logger.info("Calling complete_scan()")
        service.complete_scan(scan_id)
    except Exception:
        db.rollback()
        logger.exception(
        "Failed to start scan %s",
        scan_id,)
        
        try:
            service.fail_scan(scan_id)
        except Exception:
            logger.exception(
                "Unable to mark scan %s as failed", scan_id
            )

        raise    

    finally:
        db.close()