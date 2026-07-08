from dataclasses import dataclass

@dataclass
class RequestResult:
    status_code: int | None
    response_time_ms: float
    timed_out: bool
    error_type: str | None
    error_message: str | None