from dataclasses import dataclass


@dataclass
class PerformanceStats:
    total_requests: int

    successful_requests: int

    rate_limited_requests: int

    server_errors: int

    timeout_requests: int

    other_error_requests: int

    average_response_time_ms: float

    failed_requests : int

    min_response_time_ms: float

    max_response_time_ms: float