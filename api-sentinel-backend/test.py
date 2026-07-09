import httpx

from app.load_testing.service import LoadTestService
from app.load_testing.schemas import (
    HttpRequest,
    LoadTestRequest,
)
from app.core.enums import HttpMethod


def main() -> None:
    with httpx.Client(timeout=30.0) as client:
        service = LoadTestService(client)

        request = LoadTestRequest(
            request=HttpRequest(
                url="https://clothingbrand-ddfx.onrender.com/api/user/login",
                method=HttpMethod.POST,
                headers={
                    "Content-Type": "application/json",
                },
                body={
                    "email": "xyz@gmail.com",
                    "password": "Harshit@14",
                },
            ),
            total_requests=100,          # Increase later
            concurrent_workers=20,       # Increase later
        )

        response = service.run_load_test(request)

        print("\n===== LOAD TEST RESULTS =====")
        print(f"Total Requests      : {response.total_requests}")
        print(f"Successful          : {response.successful_requests}")
        print(f"Failed              : {response.failed_requests}")
        print(f"Rate Limited (429)  : {response.rate_limited_requests}")
        print(f"Server Errors (5xx) : {response.server_errors}")
        print(f"Timeouts            : {response.timeout_requests}")
        print(f"Average Response    : {response.average_response_time_ms:.2f} ms")
        print(f"Minimum Response    : {response.minimum_response_time_ms:.2f} ms")
        print(f"Maximum Response    : {response.maximum_response_time_ms:.2f} ms")


if __name__ == "__main__":
    main()