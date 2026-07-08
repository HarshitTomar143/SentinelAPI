import httpx
from app.load_testing.schemas import HttpRequest
from app.models.request_result import RequestResult
import time

class LoadTestService:

    def __init__(
        self,
        client: httpx.Client,
    ) -> None:
        self.client = client

    def _make_request(
            self,
            request: HttpRequest,
    ) -> RequestResult:
           
            start = time.perf_counter()

            response = self.client.request(
                method=request.method.value,
                url= str(request.url),
                headers= request.headers,
                params=request.quesry_params,
                json=request.body,
           )
            
            response_time_ms = (
            time.perf_counter() - start
        ) * 1000
            
            return RequestResult(
            status_code=response.status_code,
            response_time_ms=response_time_ms,
            timed_out=False,
        )
