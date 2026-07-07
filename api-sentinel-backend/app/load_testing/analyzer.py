import httpx

class LoadTestService:

    def __init__(
        self,
        client: httpx.Client,
    ) -> None:
        self.client = client