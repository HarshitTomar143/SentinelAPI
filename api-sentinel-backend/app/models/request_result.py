from dataclasses import dataclass

@dataclass
class RequestResult:
    status_code: int | None
    response_time_ms: float
    timed_out: bool
    error: str | None