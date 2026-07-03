import httpx
from app.models.finding_result import FindingResult
from app.core.enums import FindingSeverity

class SecurityHeadersCheck:
    def run(
            self,
            headers: httpx.Headers,
    )-> list[FindingResult]:
        
        required_headers = {
                "Strict-Transport-Security": {
                        "severity": FindingSeverity.HIGH.value,
                        "recommendation": "Enable HSTS to enforce HTTPS connections."
                },
                "X-Content-Type-Options": {
                        "severity": FindingSeverity.MEDIUM.value,
                        "recommendation": "Set X-Content-Type-Options to prevent MIME type sniffing."
                },
                "X-Frame-Options": {
                        "severity": FindingSeverity.LOW.value,
                        "recommendation": "Set X-Frame-Options to protect against clickjacking."
                },
                "Content-Security-Policy": {
                        "severity": FindingSeverity.LOW.value,
                        "recommendation": "Define a Content Security Policy to reduce XSS risks."
                },
                "Referrer-Policy": {
                        "severity": FindingSeverity.LOW.value,
                        "recommendation": "Configure a Referrer-Policy to limit information leakage."
                },
                }
        finding : list[FindingResult] = []

        for header, config in required_headers.items():
            if header in headers:
                pass
            else:
                pass
            
        return finding    