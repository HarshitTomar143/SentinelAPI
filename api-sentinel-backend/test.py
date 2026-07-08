import httpx
from app.load_testing.service import LoadTestService
from app.load_testing.schemas import LoadTestRequest
from app.load_testing.schemas import HttpRequest
from app.core.enums import HttpMethod

with httpx.Client(timeout=10.0) as client:
    service = LoadTestService(client)

    request = LoadTestRequest(
    request=HttpRequest(
        url="https://jsonplaceholder.typicode.com/todos/1",
        method=HttpMethod.GET,
    ),
    total_requests=10,
    concurrent_workers=5,
    )

    response = service.run_load_test(request)

    print(response)