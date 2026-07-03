import httpx
from app.core.enums import FindingSeverity
from app.models.finding_result import FindingResult

class ErrorHandlingCheck:
    def run(
            self,
            response: httpx.Response
    ) -> list[FindingResult]:
        
        findings : list[FindingResult] = []

        if response.status_code == 404:
            findings.append(
                FindingResult(
                    title="Proper 404 Handling",
                    description="The API correctly returns HTTP 404 for unknown endpoints.",
                    severity=FindingSeverity.INFO.value,
                    passed=True,
                    recommendation="No action required.",
                )
            )

        else:
            findings.append(
                FindingResult(
                    title="Unexpected Status Code",
                    description=f"The API returned HTTP {response.status_code} instead of HTTP 404 for an unknown endpoint.",
                    severity=FindingSeverity.HIGH.value,
                    passed=False,
                    recommendation="Ensure unknown endpoints return HTTP 404.",
                )
            )

