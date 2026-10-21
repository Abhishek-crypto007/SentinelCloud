
from backend.scanner.rules import analyze_configuration


def test_detects_both_security_issues():
    config = {
        "resource_type": "sample_storage",
        "public_access": True,
        "encryption_enabled": False,
    }

    findings = analyze_configuration(config)

    assert len(findings) == 2

    rule_ids = {finding["rule_id"] for finding in findings}

    assert "SC-STORAGE-001" in rule_ids
    assert "SC-STORAGE-002" in rule_ids


def test_safe_configuration_has_no_findings():
    config = {
        "resource_type": "sample_storage",
        "public_access": False,
        "encryption_enabled": True,
    }

    findings = analyze_configuration(config)

    assert findings == []


def test_public_access_rule_works_independently():
    config = {
        "resource_type": "sample_storage",
        "public_access": True,
        "encryption_enabled": True,
    }

    findings = analyze_configuration(config)

    assert len(findings) == 1
    assert findings[0]["rule_id"] == "SC-STORAGE-001"


def test_encryption_rule_works_independently():
    config = {
        "resource_type": "sample_storage",
        "public_access": False,
        "encryption_enabled": False,
    }

    findings = analyze_configuration(config)

    assert len(findings) == 1
    assert findings[0]["rule_id"] == "SC-STORAGE-002"
