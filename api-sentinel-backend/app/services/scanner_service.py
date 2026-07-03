from uuid import UUID
import httpx
import logging
from sqlalchemy.orm import Session
from app.checks.availability import AvailabilityCheck
from app.checks.response_time import ResponseTimeCheck
from app.checks.https_check import HttpsCheck
from app.services.scan_service import ScanService
from app.checks.security_headers import SecurityHeadersCheck

logger = logging.getLogger(__name__)


class ScannerService:
    def __init__(
        self,
        db: Session,
        client: httpx.Client,
    ) -> None:
        self.db = db
        self.client = client
        self.scan_service = ScanService(db)

    def run_availability(
        self,
        scan_id: UUID,
    ) -> httpx.Response:
        scan = self.scan_service.get_scan(scan_id)

        if scan is None:
            raise ValueError(
                f"Scan with id '{scan_id}' was not found."
            )

        availability_check = AvailabilityCheck()

        try:

     

            response= self.client.get(
                str(scan.base_url)
            )




            finding = availability_check.run(response)

            logger.info(
                "Scanned %s - Status Code: %s",
                scan.base_url,
                response.status_code,
            )

        except httpx.HTTPError as exc:

            logger.exception(
                "Failed to scan %s",
                scan.base_url,
            )

            finding = availability_check.failed(exc)

            self.scan_service.save_finding(
                scan.id,
                finding,
            )

            raise

        self.scan_service.save_finding(
            scan.id,
            finding,
        )

        return response

    def run_response_time(
        self,
        scan_id: UUID,
        response: httpx.Response,
    ) -> None:

        response_time_ms = (
            response.elapsed.total_seconds() * 1000
        )

        response_time_check = ResponseTimeCheck()

        finding = response_time_check.run(
            response_time_ms,
        )

        self.scan_service.save_finding(
            scan_id,
            finding,
        )
    
    def run_https(
            self, 
            scan_id: UUID,
            input_url : str,
            response : httpx.Response,
    ) -> None :
        https_check = HttpsCheck()

        finding = https_check.run(
            input_url= input_url,
            final_url= str(response.url),
        )

        self.scan_service.save_finding(
            scan_id= scan_id,
            finding_result= finding,
        )

    def run_security_headers(
            self, 
            scan_id : UUID,
            response : httpx.Response,
    )-> None:
        security_headers_check = SecurityHeadersCheck()

        findings = security_headers_check.run(
            response.headers
        )

        for finding in findings:
            self.scan_service.save_finding(
                scan_id=scan_id,
                finding_result= finding
            )