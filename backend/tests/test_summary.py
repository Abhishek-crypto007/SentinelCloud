
import pytest

from backend.scanner.summary import summarize_findings


def test_summarize_findings_counts_each_severity():
    findings = [
        {"severity": "high"},
        {"severity": "high"},
        {"severity": "medium"},
        {"severity": "low"},
    ]

    summary = summarize_findings(findings)

    assert summary["critical"] == 0
    assert summary["high"] == 2
    assert summary["medium"] == 1
    assert summary["low"] == 1


def test_summarize_empty_findings():
    assert summarize_findings([]) == {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
    }


def test_summarize_rejects_unknown_severity():
    findings = [{"severity": "urgent"}]

    with pytest.raises(ValueError, match="Unsupported finding severity"):
        summarize_findings(findings)
