
from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)




def test_health_endpoint():
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_scan_endpoint_detects_two_issues():
    response = client.post(
        "/api/v1/scans",
        json={
            "resource_type": "sample_storage",
            "public_access": True,
            "encryption_enabled": False,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total_findings"] == 2
    assert len(data["findings"]) == 2


def test_scan_endpoint_returns_no_findings_for_safer_config():
    response = client.post(
        "/api/v1/scans",
        json={
            "resource_type": "sample_storage",
            "public_access": False,
            "encryption_enabled": True,
        },
    )

    assert response.status_code == 200
    assert response.json()["total_findings"] == 0


def test_scan_endpoint_rejects_missing_fields():
    response = client.post(
        "/api/v1/scans",
        json={
            "resource_type": "sample_storage",
            "public_access": True,
        },
    )

    assert response.status_code == 422

def test_scan_response_includes_severity_summary():
    response = client.post(
        "/api/v1/scans",
        json={
            "resource_type": "storage",
            "public_access": True,
            "encryption_enabled": False,
            "versioning_enabled": False,
            "logging_enabled": False,
        },
    )

    assert response.status_code == 200

    data = response.json()
    assert data["total_findings"] == 4
    assert data["severity_summary"] == {
        "critical": 0,
        "high": 1,
        "medium": 2,
        "low": 1,
    }


def test_list_security_rules():
    response = client.get("/api/v1/rules")

    assert response.status_code == 200

    data = response.json()
    assert "rules" in data
    assert len(data["rules"]) == 4

    rule_ids = {rule["rule_id"] for rule in data["rules"]}

    assert rule_ids == {
        "SC-STORAGE-001",
        "SC-STORAGE-002",
        "SC-STORAGE-003",
        "SC-STORAGE-004",
    }


def test_list_security_rules_returns_sorted_ids():
    response = client.get("/api/v1/rules")

    assert response.status_code == 200

    rules = response.json()["rules"]
    rule_ids = [rule["rule_id"] for rule in rules]

    assert rule_ids == sorted(rule_ids)
