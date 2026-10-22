
import pytest

from backend.scanner.rules import (
    analyze_configuration,
    validate_configuration,
)
from backend.scanner.constants import VALID_SEVERITIES


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



def test_disabled_versioning_creates_finding():
    config = {
        "resource_type": "storage",
        "public_access": False,
        "encryption_enabled": True,
        "versioning_enabled": False,
    }

    findings = analyze_configuration(config)

    assert any(
        finding["rule_id"] == "SC-STORAGE-003"
        for finding in findings
    )


def test_disabled_logging_creates_finding():
    config = {
        "resource_type": "storage",
        "public_access": False,
        "encryption_enabled": True,
        "logging_enabled": False,
    }

    findings = analyze_configuration(config)

    assert any(
        finding["rule_id"] == "SC-STORAGE-004"
        for finding in findings
    )

def test_missing_required_field_is_rejected():
    config = {"public_access": True}

    with pytest.raises(ValueError, match="encryption_enabled"):
        validate_configuration(config)


def test_non_boolean_security_setting_is_rejected():
    config = {
        "public_access": "false",
        "encryption_enabled": True,
    }

    with pytest.raises(ValueError, match="public_access"):
        validate_configuration(config)



def test_all_four_security_findings_are_detected():
    config = {
        "public_access": True,
        "encryption_enabled": False,
        "versioning_enabled": False,
        "logging_enabled": False,
    }

    findings = analyze_configuration(config)

    rule_ids = {finding["rule_id"] for finding in findings}

    assert rule_ids == {
        "SC-STORAGE-001",
        "SC-STORAGE-002",
        "SC-STORAGE-003",
        "SC-STORAGE-004",
    }


def test_secure_configuration_returns_no_findings():
    config = {
        "public_access": False,
        "encryption_enabled": True,
        "versioning_enabled": True,
        "logging_enabled": True,
    }

    findings = analyze_configuration(config)

    assert findings == []


def test_omitted_optional_fields_do_not_create_findings():
    config = {
        "public_access": False,
        "encryption_enabled": True,
    }

    findings = analyze_configuration(config)

    assert findings == []


def test_findings_have_required_fields():
    config = {
        "public_access": True,
        "encryption_enabled": False,
        "versioning_enabled": False,
        "logging_enabled": False,
    }

    findings = analyze_configuration(config)

    required_fields = {
        "rule_id",
        "title",
        "severity",
        "description",
        "remediation",
    }

    for finding in findings:
        assert required_fields.issubset(finding.keys())
        assert finding["severity"] in VALID_SEVERITIES


