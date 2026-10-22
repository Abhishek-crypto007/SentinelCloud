
"""Helpers for summarizing SentinelCloud findings."""

from backend.scanner.constants import VALID_SEVERITIES


def summarize_findings(
    findings: list[dict[str, str]],
) -> dict[str, int]:
    """Count findings by severity."""

    summary = {
        severity: 0
        for severity in VALID_SEVERITIES
    }

    for finding in findings:
        severity = finding["severity"]

        if severity not in summary:
            raise ValueError(
                f"Unsupported finding severity: {severity}"
            )

        summary[severity] += 1

    return summary
