from sqlalchemy.orm import Session
from app.models.scan import Scan
from app.core.enums import ScanStatus

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

    def get_scan(self, scan_id,)-> Scan | None:
        return (
            self.db.query(Scan).filter(Scan.id == scan_id).first
        )