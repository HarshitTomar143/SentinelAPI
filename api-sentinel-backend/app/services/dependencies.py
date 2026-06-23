from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.scan_service import ScanService

def get_scan_service(
        db: Session = Depends(get_db),
)-> ScanService:
    return ScanService(db)