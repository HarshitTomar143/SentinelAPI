from uuid import UUID
from sqlalchemy.orm import Session
from app.services.scan_service import ScanService
import httpx
import logging
from app.checks.availability import AvailabilityCheck

logger = logging.getLogger(__name__)

class ScannerService:
    def __init__(self, db:Session) -> None:
        self.db= db
        self.scan_service = ScanService(db)
        
    

    def execute(self, scan_id : UUID) -> None:
        availability_check = AvailabilityCheck()
        scan = self.scan_service.get_scan(scan_id)

        if scan is None:
            raise ValueError(
                f"Scan with id '{scan_id}' was not found."
            )
        
        try :    
            response = httpx.get(
                str(scan.base_url),
                timeout=10.0,
            )


            finding = availability_check.run(response)

            logger.info(
                "Scanned %s - Status Code: %s",
                scan.base_url,
                response.status_code,)
        except httpx.HTTPError as e:

            logger.exception(
                "Failed to scan %s",
                scan.base_url,
            )
            finding = availability_check.failed(e)

        
        
        self.scan_service.save_finding(
            scan.id,
            finding,
        )

        
    