from fastapi import APIRouter, Depends

from uuid import UUID

from app.schemas.scan import (
    CreateScanData,
    CreateScanRequest,
    CreateScanResponse,
    ScanStatusResponse
)

from app.services.scan_service import ScanService
from app.services.dependencies import get_scan_service

router = APIRouter()

@router.post(
    "/scans",
    response_model=CreateScanResponse,
)
def create_scan(
    payload : CreateScanRequest,
    scan_service: ScanService = Depends(get_scan_service)
):
    scan = scan_service.create_scan(
        payload.base_url
    )

    return CreateScanResponse(
        data = CreateScanData(
            scan_id= scan.id,
            status= scan.status,
            created_at= scan.created_at,
        )
    )

@router.get(
    "/scans/{sacn_id}",
    response_model= ScanStatusResponse
)
def get_scan(
    scan_id: UUID,
    scan_service : ScanService = Depends(get_scan_service)
):
    pass