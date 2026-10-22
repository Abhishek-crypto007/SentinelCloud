
from fastapi import FastAPI
from pydantic import BaseModel, Field

from backend.scanner.rules import analyze_configuration
from contextlib import asynccontextmanager

from fastapi import FastAPI, Query
from backend.database import initialize_database, save_scan, get_scans

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
    )


@app.get("/api/v1/scans")
def scan_history(
    limit: int = Query(default=20, ge=1, le=100),
):
    return {
        "scans": get_scans(limit=limit),
    }