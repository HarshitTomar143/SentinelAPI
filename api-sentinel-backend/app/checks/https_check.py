from app.models.finding_result import FindingResult
from urllib.parse import urlparse
from app.core.enums import FindingSeverity

class HttpsCheck:
    def run(
            self,
            input_url: str,
            final_url: str
    )-> FindingResult:
        input_scheme = urlparse(input_url).scheme
        final_scheme = urlparse(final_url).scheme

        if input_scheme == "https":
            if final_scheme == "https":
                return FindingResult(
                title="HTTPS Enabled",
                description=f"The API is served over HTTPS.",
                severity=FindingSeverity.INFO.value,
                passed=True,
                recommendation="No action required."
                )
            else:
                return FindingResult(
                title="HTTPS Downgrade Detected",
                description=(
                    "The request started over HTTPS but was redirected to an "
                    "unencrypted HTTP connection."
                ),
                severity=FindingSeverity.CRITICAL.value,
                passed=False,
                recommendation=(
                    "Remove the HTTPS to HTTP redirect immediately and ensure all "
                    "traffic remains encrypted using TLS."
                ),
)
            
        
        elif input_scheme == "http" and final_scheme == "https":
            return FindingResult(
            title="HTTP Redirects to HTTPS",
            description=f"The API redirects HTTP requests to HTTPS.",
            severity=FindingSeverity.LOW.value,
            passed=True,
            recommendation="Better enable https initially rather than redirecting from http."
            )
        
        else :
            return FindingResult(
            title="HTTPS Not Enabled",
            description=f"The API is served over HTTP without encryption.",
            severity=FindingSeverity.HIGH.value,
            passed=False,
            recommendation="Enable HTTPS to encrypt client-server communication using TLS."
            )
