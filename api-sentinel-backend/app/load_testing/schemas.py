from typing import Any

from pydantic import BaseModel
from pydantic import HttpUrl
from app.core.enums import HttpMethod

class HttpRequest(BaseModel):
    url: HttpUrl

    method: HttpMethod

    headers: dict[str, str] = {}

    query_params: dict[str, str] = {}

    body: dict | None = None

class LoadTestRequest(BaseModel):
    request: HttpRequest

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