from concurrent.futures import ThreadPoolExecutor, as_completed
import httpx
from app.load_testing.schemas import HttpRequest, LoadTestRequest, LoadTestResponse
from app.models.request_result import RequestResult
import time
from app.models.performance_stats import PerformanceStats

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
                params=request.query_params,
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

    def _calculate_performance_stats(
              self,
              results: list[RequestResult],
    )-> PerformanceStats:
            total_requests = len(results)

            successful_requests = 0
            rate_limited_requests = 0
            server_error_requests = 0
            timeout_requests = 0

            latencies : list[float] = []

            for request in results:
                if request.status_code is not None and 200<= request.status_code < 300:
                    successful_requests += 1
                elif request.status_code == 429:
                    rate_limited_requests += 1
                elif (
                        request.status_code is not None
                        and 500 <= request.status_code < 600
                    ):
                        server_error_requests  += 1
                elif  request.timed_out:
                        timeout_requests += 1

                latencies.append(
                  request.response_time_ms
                )

            if latencies:
                average_response_time_ms = (
                    sum(latencies) / len(latencies)
                )

                minimum_response_time_ms = min(latencies)

                maximum_response_time_ms = max(latencies)

            else:
                average_response_time_ms = 0.0
                minimum_response_time_ms = 0.0
                maximum_response_time_ms = 0.0

            failed_requests = (
                total_requests - successful_requests
            )        

            return PerformanceStats(
                total_requests= total_requests,
                successful_requests = successful_requests,
                rate_limited_requests = rate_limited_requests,
                server_errors= server_error_requests,
                failed_requests = failed_requests,
                timeout_requests = timeout_requests,
                other_error_requests = 0,
                average_response_time_ms = average_response_time_ms,
                min_response_time_ms = minimum_response_time_ms,
                max_response_time_ms = maximum_response_time_ms,
            )

    def run_load_test(
                self,
                load_test : LoadTestRequest,
    ) -> LoadTestResponse:
                results = self._run_concurrent_requests(
                          load_test.request,
                            load_test.total_requests,
                            load_test.concurrent_workers,

                )

                stats = self._calculate_performance_stats(results)

                return LoadTestResponse(
                total_requests=stats.total_requests,
                successful_requests=stats.successful_requests,
                failed_requests=stats.failed_requests,
                rate_limited_requests=stats.rate_limited_requests,
                server_errors=stats.server_errors,
                timeout_requests=stats.timeout_requests,
                average_response_time_ms=stats.average_response_time_ms,
                minimum_response_time_ms=stats.min_response_time_ms,
                maximum_response_time_ms=stats.max_response_time_ms,
            )