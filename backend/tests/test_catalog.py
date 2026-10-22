
from backend.scanner.catalog import RULE_CATALOG
from backend.scanner.constants import VALID_SEVERITIES
from backend.scanner.rules import analyze_configuration


def test_catalog_contains_four_storage_rules():
    assert len(RULE_CATALOG) == 4


def test_every_catalog_rule_has_required_metadata():
    for rule_id, rule in RULE_CATALOG.items():
        assert rule_id.startswith("SC-STORAGE-")
        assert rule["title"]
        assert rule["severity"] in VALID_SEVERITIES


def test_rule_ids_are_unique():
    rule_ids = list(RULE_CATALOG.keys())

    assert len(rule_ids) == len(set(rule_ids))




def test_scanner_findings_match_catalog_metadata():
    config = {
        "public_access": True,
        "encryption_enabled": False,
        "versioning_enabled": False,
        "logging_enabled": False,
    }

    findings = analyze_configuration(config)

    for finding in findings:
        rule = RULE_CATALOG[finding["rule_id"]]

        assert finding["title"] == rule["title"]
        assert finding["severity"] == rule["severity"]
