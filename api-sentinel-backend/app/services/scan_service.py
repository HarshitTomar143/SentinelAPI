from sqlalchemy.orm import Session
from app.models.scan import Scan
from app.core.enums import ScanStatus
from app.models.finding import Finding
from uuid import UUID
class ScanService:
    def __init__(self, db: Session):
        self.db = db

    def create_scan(self, base_url : str) -> Scan:
        scan = Scan(
            base_url = str(base_url),
            status = ScanStatus.QUEUED.value,
            progress = 0,
            current_stage = None,
        )

        self.db.add(scan)
        self.db.commit()
        self.db.refresh(scan)
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
        return scan.findings
        ## This is more optimsed approach as we have implemented relationships in our orm models
## return (
#           self.db.query(Finding).filter(Finding.scan_id == scan_id).all() )
