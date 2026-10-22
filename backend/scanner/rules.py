
from typing import Any


def analyze_configuration(config: dict[str, Any]) -> list[dict[str, str]]:
    """Analyze a sample resource configuration and return findings."""

    findings = []

    if config["public_access"]:
        findings.append({
            "rule_id": "SC-STORAGE-001",
            "title": "Public access enabled",
            "severity": "high",
            "description": (
                "The sample configuration enables public access, "
                "which could expose data to unauthorized users."
            ),
            "remediation": (
                "Disable public access unless explicitly required "
                "and appropriately controlled."
            ),
        })

    if not config["encryption_enabled"]:
        findings.append({
            "rule_id": "SC-STORAGE-002",
            "title": "Encryption not enabled",
            "severity": "medium",
            "description": (
                "The sample configuration indicates that encryption "
                "is not enabled."
            ),
            "remediation": (
                "Enable appropriate encryption and verify the "
                "resource's encryption settings."
            ),
        })
    if config.get("versioning_enabled") is False:
        findings.append({
            "rule_id": "SC-STORAGE-003",
            "title": "Storage versioning is disabled",
            "severity": "medium",
            "description": (
                "Object versioning is disabled, which may "
                "make recovery from accidental deletion "
                "or overwrites more difficult."
            ),
            "remediation": (
                "Enable object versioning where appropriate "
                "for the storage resource."
            ),
        })

    if config.get("logging_enabled") is False:
        findings.append({
            "rule_id": "SC-STORAGE-004",
            "title": "Storage access logging is disabled",
            "severity": "low",
            "description": (
                "Access logging is disabled, which can "
                "reduce visibility during security investigations."
            ),
            "remediation": (
                "Enable appropriate access logging and "
                "configure log retention and access controls."
            ),
        })






    return findings
