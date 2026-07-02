from celery import shared_task
import logging
from uuid import UUID
from app.db.session import SessionLocal
from app.services.scan_service import ScanService
from app.services.scanner_service import ScannerService
from app.core.enums import ScanStage

logger = logging.getLogger(__name__)

@shared_task
def run_scan(scan_id : UUID)-> None:
    db = SessionLocal()

    try : 
        service = ScanService(db)
        scanner_service = ScannerService(db)
        service.start_scan(scan_id)

        service.update_progress(
        scan_id=scan_id,
        progress=20,
        current_stage=ScanStage.STARTING.value,
    )
        
        logger.info("Started scan %s", scan_id)

        response= scanner_service.run_availability(
            scan_id
        )

        service.update_progress(
        scan_id=scan_id,
        progress=50,
        current_stage=ScanStage.AVAILABILITY.value,
    )
        scanner_service.run_response_time(
            scan_id,
            response
        )

        service.update_progress(
        scan_id=scan_id,
        progress=80,
        current_stage=ScanStage.RESPONSE_TIME.value,
    )
        
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