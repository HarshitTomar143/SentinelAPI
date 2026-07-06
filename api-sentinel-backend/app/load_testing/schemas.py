from pydantic import BaseModel
from pydantic import HttpUrl
from http import HTTPMethod

class LoadTestRequest(BaseModel):
    url: HttpUrl

    method: HTTPMethod

    headers: dict[str, str] = {}

    body: dict | None = None

    total_requests: int = 2000

    concurrent_workers: int = 100

class LoadTestResponse(BaseModel):

    total_requests: int

    successful_requests: int

    failed_requests: int

    rate_limited_requests: int

    server_errors: int

    timeout_requests: int

    average_response_time_ms: float

    minimum_response_time_ms: float

    maximum_response_time_ms: float    