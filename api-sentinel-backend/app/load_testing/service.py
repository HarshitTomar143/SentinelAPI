import httpx


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
           self.client.request(
                method=request.method.value,
                url= str(request.url),
                headers= request.headers,
                params=request.quesry_params,
                json=request.body,
           )