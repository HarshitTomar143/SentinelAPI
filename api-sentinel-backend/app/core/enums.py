from enum import Enum

class ScanStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class FindingSeverity(str, Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"   

class ScanStage(str, Enum):
    STARTING = "Starting Scan"
    AVAILABILITY = "Availability Check"
    RESPONSE_TIME = "Response Time Check"
    HTTPS = "HTTPS Check"
    SECURITY_HEADERS = "Security Headers Check"
    RATE_LIMIT = "Rate Limiting Check"
    COMPLETED = "Completed"