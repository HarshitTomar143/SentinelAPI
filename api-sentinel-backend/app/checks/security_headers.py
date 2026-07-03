import httpx
from app.models.finding_result import FindingResult
from app.core.enums import FindingSeverity

class SecurityHeadersCheck:
    def run(
            self,
            headers: httpx.Headers,
    )-> list[FindingResult]:
        