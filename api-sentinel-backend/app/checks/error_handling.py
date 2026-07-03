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

        content_type = response.headers.get(
            "Content-Type", "",
        ).lower()

        if "application/json" in content_type:
            findings.append(
                FindingResult(
                    title="Structured Error Response",
                    description="The API returns structured JSON error responses.",
                    severity=FindingSeverity.INFO.value,
                    passed=True,
                    recommendation="No action required.",
                )
            )

        else:
            findings.append(
                FindingResult(
                    title="Non-JSON Error Response",
                    description="The API does not return JSON for error responses.",
                    severity=FindingSeverity.MEDIUM.value,
                    passed=False,
                    recommendation="Return structured JSON error responses.",
                )
            )

        leakage_keywords = [
             "traceback",
            "exception",
            "stack trace",
            "sqlalchemy",
            "fastapi",
            "express",
            "spring",
            "node.js",
            "postgres",
            "sqlite",
            ] 

        body= response.text.lower()

        if any(keyword in body for keyword in leakage_keywords):
            findings.append(
                FindingResult(
                    title="Sensitive Information Exposed",
                    description="The error response appears to expose internal implementation details.",
                    severity=FindingSeverity.HIGH.value,
                    passed=False,
                    recommendation="Remove stack traces and framework details from production error responses.",
                )
            )
        else:
            findings.append(
                FindingResult(
                    title="No Information Leakage",
                    description="No sensitive implementation details were detected.",
                    severity=FindingSeverity.INFO.value,
                    passed=True,
                    recommendation="No action required.",
                )
            )

        if 300 <= response.status_code < 400:
            findings.append(
                FindingResult(
                    title="Unexpected Redirect",
                    description="The invalid endpoint returned a redirect instead of an error.",
                    severity=FindingSeverity.LOW.value,
                    passed=False,
                    recommendation="Return HTTP 404 for unknown API endpoints instead of redirecting.",
                )
            )
        else:
            findings.append(
                FindingResult(
                    title="No Unexpected Redirect",
                    description="The invalid endpoint did not trigger a redirect.",
                    severity=FindingSeverity.INFO.value,
                    passed=True,
                    recommendation="No action required.",
                )
            )       


        return findings