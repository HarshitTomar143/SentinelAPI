from app.models.finding_result import FindingResult


class ResponseTimeCheck:
    def run(
        self,
        response_time_ms: float,
    ) -> FindingResult:

        response_time_ms = round(response_time_ms, 2)

        if response_time_ms < 200:
            return FindingResult(
                title="Excellent Response Time",
                description=f"The API responded in {response_time_ms} ms.",
                severity="INFO",
                passed=True,
                recommendation="No action is required. The API response time is excellent.",
            )

        elif response_time_ms < 500:
            return FindingResult(
                title="Good Response Time",
                description=f"The API responded in {response_time_ms} ms.",
                severity="LOW",
                passed=True,
                recommendation="The response time is acceptable for most public APIs.",
            )

        elif response_time_ms < 1000:
            return FindingResult(
                title="Moderate Response Time",
                description=f"The API responded in {response_time_ms} ms.",
                severity="MEDIUM",
                passed=True,
                recommendation=(
                    "Consider reviewing database queries, caching, "
                    "or external API calls to improve response time."
                ),
            )

        else:
            return FindingResult(
                title="High Response Time",
                description=f"The API responded in {response_time_ms} ms.",
                severity="HIGH",
                passed=True,
                recommendation=(
                    "High latency detected. Investigate database performance, "
                    "caching strategy, infrastructure, or network latency."
                ),
            )