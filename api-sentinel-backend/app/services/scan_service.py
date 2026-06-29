from sqlalchemy.orm import Session
from app.models.scan import Scan
from app.core.enums import ScanStatus
from app.models.finding import Finding
from app.models.finding_result import FindingResult

from uuid import UUID
class ScanService:
    def __init__(self, db: Session):
        self.db = db

    def create_scan(self, base_url : str) -> Scan:
        from app.workers.tasks import run_scan
        scan = Scan(
            base_url = str(base_url),
            status = ScanStatus.QUEUED.value,
            progress = 0,
            current_stage = None,
        )

        self.db.add(scan)
        self.db.commit()
        self.db.refresh(scan)
        run_scan.delay(scan.id)
        return scan

    def get_scan(self, scan_id:UUID,)-> Scan | None:
        return (
            self.db.query(Scan).filter(Scan.id == scan_id).first()
        )
    
    def get_scan_findings(
            self, 
            scan_id : UUID,
    )-> list[Finding] : 
        scan = self.get_scan(scan_id)
        if scan is None:
            raise ValueError(f"Scan {scan_id} is not found")
        return scan.findings
        ## This is more optimsed approach as we have implemented relationships in our orm models
## return (
#           self.db.query(Finding).filter(Finding.scan_id == scan_id).all() )

    def start_scan(self, scan_id: UUID)-> Scan:
        scan = self.get_scan(scan_id)
        if scan is None:
            raise ValueError(f"Scan {scan_id} is not found")
        scan.status = ScanStatus.RUNNING.value
       
        self.db.commit()
        self.db.refresh(scan)

        return scan
    
    def save_finding(
            self,
            scan_id: UUID,
            finding_result: FindingResult
    )-> Finding:
       finding = Finding(
        scan_id=scan_id,
        severity=finding_result.severity,
        title=finding_result.title,
        description=finding_result.description,
        recommendation=finding_result.recommendation,
    )
       
       self.db.add(finding)
       self.db.commit()
       self.db.refresh(finding)

       return finding
