from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime
from uuid import UUID

class CreateScanRequest(BaseModel):
    base_url: HttpUrl

class CreateScanData(BaseModel):
    scan_id : UUID
    status: str
    created_at: datetime

class CreateScanResponse(BaseModel):
    success : bool = True
    data : CreateScanData

class ScanStatusData(BaseModel):
    scan_id : UUID
    status: str
    progress : int
    current_stage : str | None        

class ScanResultsData(BaseModel):
    health_score: int
    success_rate: float
    avg_latency : float
    min_latency : float
    max_latency : float
    p95_latency : float

    http_enabled : bool
    rate_limiting_detected : bool

class ScanResultsResponse(BaseModel):
    success : bool = True
    data : ScanResultsData