
from fastapi import FastAPI, Query , HTTPException

from pydantic import BaseModel, Field   

from backend.scanner.rules import analyze_configuration
from contextlib import asynccontextmanager

from backend.database import initialize_database, save_scan, get_scans

from backend.scanner.summary import summarize_findings
from backend.scanner.catalog import RULE_CATALOG

from backend.scanner.constants import VALID_SEVERITIES


# Create the FastAPI application
@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    yield


app = FastAPI(
    title="SentinelCloud API",
    description="Cloud security configuration analysis",
    version="0.4.0",
    lifespan=lifespan,
)


# Define the expected request data
class ScanRequest(BaseModel):
    resource_type: str = Field(min_length=1, max_length=50)
    public_access: bool
    encryption_enabled: bool
    versioning_enabled: bool | None = None
    logging_enabled: bool | None = None


# Define the structure of each finding
class Finding(BaseModel):
    rule_id: str
    title: str
    severity: str
    description: str
    remediation: str


# Define the API response
class ScanResponse(BaseModel):
    resource_type: str
    findings: list[Finding]
    total_findings: int
    severity_summary: dict[str, int] 


# Health-check endpoint
@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "project": "SentinelCloud",
        "version": "0.3.0",
    }


# Security scan endpoint
@app.post("/api/v1/scans", response_model=ScanResponse)
def scan_configuration(request: ScanRequest):
    findings = analyze_configuration(request.model_dump())

    save_scan(
        resource_type=request.resource_type,
        findings=findings,
    )

    return ScanResponse(
        resource_type=request.resource_type,
        findings=findings,
        total_findings=len(findings),
        severity_summary=summarize_findings(findings),
    )



@app.get("/api/v1/scans")
def scan_history(
    limit: int = Query(default=20, ge=1, le=100),
    severity: str | None = Query(default=None),
):
    scans = get_scans(limit=limit)

    if severity is not None:
        severity = severity.lower()

        if severity not in VALID_SEVERITIES:
            raise HTTPException(
                status_code=422,
                detail=(
                    "Invalid severity. Choose from: "
                    + ", ".join(sorted(VALID_SEVERITIES))
                ),
            )

        filtered_scans = []

        for scan in scans:
            matching_findings = [
                finding
                for finding in scan["findings"]
                if finding["severity"] == severity
            ]

            if matching_findings:
                filtered_scans.append({
                    **scan,
                    "findings": matching_findings,
                    "total_findings": len(matching_findings),
                })

        scans = filtered_scans

    return {"scans": scans}



@app.get("/api/v1/rules")
def list_security_rules():
    """Return the available security rule definitions."""

    rules = [
        {
            "rule_id": rule_id,
            "title": metadata["title"],
            "severity": metadata["severity"],
        }
        for rule_id, metadata in sorted(RULE_CATALOG.items())
    ]

    return {"rules": rules}
