import httpx
from app.models.finding_result import FindingResult


class AvailabilityCheck:
    def run(self, response: httpx.Response)-> FindingResult:
        return FindingResult(
            title="API Reachable",
            description=f"The API responded with status code {response.status_code}.",
            severity="INFO",
            passed=True,
            recommendation="No action required."
        )

    def failed(self, exception: Exception)-> FindingResult:
        return FindingResult(
            title="API Unreachable",
            description=f"Failed to connect to the API. Reason: {exception}",
            severity="HIGH",
            passed=False,
            recommendation="Ensure the API is running and accessible from the public internet."
        )
