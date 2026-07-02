import httpx
from app.models.finding_result import FindingResult

class SecurityHeadersCheck:
    def run(
            self,
            headers: httpx.Headers,
    )-> list[FindingResult]:
        