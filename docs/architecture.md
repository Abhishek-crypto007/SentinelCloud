
# SentinelCloud — System Architecture

## 1. Overview

SentinelCloud is a defensive cybersecurity application designed to
identify cloud configuration risks, explain security findings, and
recommend remediation steps.

The initial version analyzes sample JSON and YAML configuration files.
Later versions may add security event analysis and authorized,
read-only AWS integration.

## 2. Architecture Goals

- Keep the application modular and beginner-friendly.
- Separate the user interface from security analysis logic.
- Validate all untrusted input before processing.
- Make detection rules transparent and testable.
- Store scan results for later review.
- Avoid requiring cloud credentials for the initial version.
- Add cloud integration only after appropriate security controls
  have been implemented.

## 3. Technology Stack

| Component | Technology | Responsibility |
|---|---|---|
| Frontend | HTML, CSS, JavaScript | Dashboard and user interaction |
| Backend API | Python, FastAPI | Request handling and API responses |
| API server | Uvicorn | Runs the backend application |
| Validation | Pydantic | Validates API request data |
| Configuration parser | Python JSON, PyYAML | Reads supported configuration formats |
| Analysis engine | Python | Evaluates security rules |
| Database | SQLite | Stores scan history and findings |
| Testing | Pytest, HTTPX | Tests rules and API behavior |
| Version control | Git | Tracks source code changes |

## 4. High-Level Architecture

```text
+------------------------------+
|             User             |
+---------------+--------------+
                |
                v
+------------------------------+
|          Frontend            |
|      HTML / CSS / JS         |
+---------------+--------------+
                |
                | HTTP / JSON
                v
+------------------------------+
|         FastAPI API          |
| Request handling and routes  |
+---------------+--------------+
                |
                v
+------------------------------+
|      Input Validation        |
| Type, size and format checks |
+---------------+--------------+
                |
                v
+------------------------------+
|   Configuration Parser       |
|         JSON / YAML          |
+---------------+--------------+
                |
                v
+------------------------------+
|     Security Rules Engine    |
| Detection and risk assessment|
+---------------+--------------+
                |
                v
+------------------------------+
|     Findings and Results     |
| Evidence, severity and fixes |
+---------------+--------------+
                |
                v
+------------------------------+
|          SQLite              |
| Scan history and findings    |
+------------------------------+

       Future Integration
+------------------------------+
| AWS IAM / S3 / CloudTrail     |
| Authorized, limited access    |
+------------------------------+
```

The database supports the application by persisting scan results.
It is not required to be a sequential processing step for every
security rule.

## 5. Core Components

### 5.1 Frontend

Responsibilities:

- Display the SentinelCloud dashboard.
- Accept sample configuration input.
- Send scan requests to the backend.
- Display findings, severity, evidence and recommendations.
- Display previous scans and reports when implemented.

The frontend must not contain AWS secret keys or other sensitive
credentials.

### 5.2 Backend API

The FastAPI backend acts as the application's entry point.

Planned responsibilities:

- Accept scan requests.
- Validate incoming request data.
- Enforce file-size and input limits.
- Call the configuration parser and analysis engine.
- Return structured results.
- Persist findings when database support is implemented.

Potential initial endpoint:

POST /api/v1/scans

Purpose:
Analyze a submitted sample configuration.

GET /api/v1/scans

Purpose:
Retrieve scan history after persistence is implemented.

GET /api/v1/health

Purpose:
Check whether the application is running.

These endpoints are planned interfaces and must be implemented
and tested before they can be used.

### 5.3 Configuration Parser

The parser converts supported JSON or YAML input into Python
data structures.

Security considerations:

- Reject malformed input.
- Enforce input-size limits.
- Use safe YAML loading rather than unrestricted object
  construction.
- Reject unsupported structures.
- Handle parsing errors without exposing internal details.

### 5.4 Security Analysis Engine

The analysis engine evaluates parsed configuration data against
explicit security rules.

Each rule should define:

- Rule identifier.
- Rule name.
- Description.
- Severity.
- Detection condition.
- Evidence.
- Recommended remediation.

Example conceptual rule:

Rule ID: SC-S3-001
Name: Public storage access
Severity: High
Condition: A supported configuration explicitly enables
           public access.
Remediation: Restrict public access unless it is explicitly
             required and appropriately controlled.

This example is illustrative. It does not prove that a real
AWS bucket is publicly accessible.

The scanner should distinguish a detected risk from a condition
that cannot be determined using the available configuration.

### 5.5 Database

SQLite will be used for the initial implementation.

Planned records include:

- Scans.
- Findings.
- Timestamps.
- Rule identifiers.
- Severity and remediation information.

User identity and ownership fields will be introduced when
authentication is implemented.

The application must enforce authorization before allowing
users to retrieve or modify their scan records.

### 5.6 Threat Detection Module

A later module will process simulated security events.

Potential examples:

- Repeated failed login attempts.
- Unusual access patterns in sample logs.
- Unexpected configuration changes.

The initial event monitor will use controlled test data and
explicit detection rules. It will not claim to detect all
real-world attacks.

### 5.7 AWS Integration

AWS integration is a future milestone.

Potential services:

- IAM for identity and permission analysis.
- S3 for storage configuration checks.
- CloudTrail for supported audit-event analysis.

The integration must use explicit authorization, least-privilege
permissions, secure credential handling and controlled test
resources.

The first version should operate without AWS credentials.

## 6. End-to-End Data Flow

1. A user submits a sample configuration through the frontend.
2. The frontend sends the data to the FastAPI backend.
3. The backend validates the request.
4. The parser processes the supported JSON or YAML structure.
5. The analysis engine evaluates applicable security rules.
6. The engine generates structured findings.
7. The backend stores results when database persistence is enabled.
8. The API returns the results to the frontend.
9. The frontend displays findings and remediation guidance.

If input validation or parsing fails, the application returns
a safe error response and does not run the security rules on
invalid data.

## 7. Finding Data Model

A finding may contain the following fields:

```json
{
  "rule_id": "SC-S3-001",
  "title": "Public storage access",
  "severity": "high",
  "description": "Public access is enabled in the sample configuration.",
  "evidence": {
    "public_access": true
  },
  "remediation": "Restrict public access and review intended permissions."
}
```

This is an illustrative data structure, not a real scan result.

Severity labels should be assigned using documented criteria.
The presence of a finding alone does not establish exploitability.

## 8. Security Requirements

- Validate and limit all incoming input.
- Parse YAML using safe parsing methods.
- Never execute uploaded configuration content.
- Do not store secrets in source code or public repositories.
- Keep credentials out of frontend code and logs.
- Use parameterized database queries.
- Implement authentication and authorization before exposing
  private scan history to multiple users.
- Restrict cloud integration to explicitly authorized resources.
- Use read-only permissions wherever possible.
- Test the application using synthetic or authorized data.
- Return safe error messages.
- Add automated tests for security rules and API endpoints.

## 9. Deployment Strategy

Development stages:

1. Run the frontend and backend locally.
2. Test the rules engine using sample configuration files.
3. Connect the frontend to the API.
4. Add SQLite persistence.
5. Test application security controls.
6. Deploy a demo with appropriate security settings.
7. Add controlled AWS integration if required.

The initial release does not require a public server or an AWS
account.

## 10. Current Limitations

At the initial stage:

- Security checks are rule-based.
- Only explicitly supported configuration formats and fields
  can be evaluated.
- Results depend on the accuracy and completeness of the input.
- The scanner cannot establish the complete security posture
  of a live cloud environment from a sample file.
- Threat detection will initially use simulated events.
- Authentication, persistence, deployment and AWS integration
  must be implemented in later milestones.

## 11. Future Improvements

- Additional configuration security rules.
- Improved severity scoring.
- Downloadable security reports.
- Secure authentication and user-specific scan history.
- Automated security testing in CI pipelines.
- Cloud audit-event analysis.
- Authorized read-only AWS assessment.
- Optional AI-assisted explanations with evidence-based output.

## 12. Development Principle

Build each component incrementally, test it, document its
limitations, and integrate it only after it works independently.

SentinelCloud is intended to support defensive security learning
and authorized security assessments.
