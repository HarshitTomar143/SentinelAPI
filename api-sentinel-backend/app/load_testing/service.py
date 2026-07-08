from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor, as_completed
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
            error = None
        )
    
    def _run_concurrent_requests(
              self,
              request: HttpRequest,
              total_requests: int,
              concurrent_workers: int,
    )->list[RequestResult]:
         
         results : list[RequestResult] = []

         with ThreadPoolExecutor(
              max_workers= concurrent_workers,
         ) as executor: 
                futures = []

                for _ in range(total_requests):
                   future = executor.submit(
                        self._make_request,
                        request
                   )

                   futures.append(future)
              
                for future in as_completed(futures):
                     result = future.result()
                     results.append(result)
                     return results     
