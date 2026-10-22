
"""Catalog of SentinelCloud storage security rules."""

RULE_CATALOG = {
    "SC-STORAGE-001": {
        "title": "Public access enabled",
        "severity": "high",
    },
    "SC-STORAGE-002": {
        "title": "Encryption not enabled",
        "severity": "medium",
    },
    "SC-STORAGE-003": {
        "title": "Storage versioning is disabled",
        "severity": "medium",
    },
    "SC-STORAGE-004": {
        "title": "Storage access logging is disabled",
        "severity": "low",
    },
}
