# SentinelCloud ☁️🛡️

### Cloud Security Misconfiguration & Threat Detection Platform

**SentinelCloud** is a beginner-built cybersecurity project designed to identify risky cloud configurations, explain security findings, and recommend remediation steps through a simple web dashboard.

The long-term goal is to develop a practical cloud security platform that combines configuration analysis, security event detection, risk scoring, and actionable remediation guidance.

> **Project status:** 🚧 In development  
> **Initial focus:** Simulated cloud configuration analysis  
> **Future goal:** Controlled, read-only AWS security assessment

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Objectives](#-objectives)
- [Planned Features](#-planned-features)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Development Roadmap](#-development-roadmap)
- [Security and Ethical Use](#-security-and-ethical-use)
- [Learning Outcomes](#-learning-outcomes)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 Overview

Cloud environments are powerful, but incorrectly configured permissions, publicly exposed storage, and insufficient logging can create serious security risks.

SentinelCloud aims to help users identify these risks by analyzing configuration data against predefined security rules.

The platform will provide:

- Detection of insecure configuration settings.
- Clear explanations of security risks.
- Severity classifications for findings.
- Suggested remediation steps.
- Scan history and security reports.
- Simulated security event monitoring.
- Optional AWS integration in a later development phase.

The initial version will operate on sample JSON/YAML configuration files. Live cloud integration will be introduced only after the core application and its security controls are implemented.

---

## 🎯 Problem Statement

Cloud misconfigurations can expose sensitive resources, grant excessive permissions, and make suspicious activity difficult to detect.

Beginners and small development teams may struggle to understand these risks and determine how to fix them.

SentinelCloud aims to address this problem by providing an accessible platform that identifies configuration weaknesses and explains practical remediation steps.

## 🎯 Objectives

1. Build a functional cybersecurity web application from scratch.
2. Develop a Python-based configuration analysis engine.
3. Identify predefined security misconfigurations using transparent rules.
4. Present findings through a clear and interactive dashboard.
5. Store scan history and findings in a database.
6. Demonstrate simulated security event detection.
7. Explore secure integration with AWS security services.
8. Apply secure coding, testing, version control, and documentation practices.

---

## ✨ Planned Features

### Phase 1 — Core Application

- [ ] Security dashboard using HTML, CSS, and JavaScript.
- [ ] Upload or submit sample JSON/YAML configurations.
- [ ] Python-based rules engine.
- [ ] Detection of predefined insecure settings.
- [ ] Finding descriptions and severity classifications.
- [ ] Remediation recommendations.

### Phase 2 — Backend and Database

- [ ] REST API using FastAPI.
- [ ] Input validation and safe error handling.
- [ ] SQLite database for scan history.
- [ ] Detailed findings and scan timestamps.
- [ ] Automated tests for detection rules and API endpoints.

### Phase 3 — Application Security

- [ ] Secure authentication and session management.
- [ ] Authorization and user-specific scan history.
- [ ] Audit logging.
- [ ] Secure configuration and secret management.
- [ ] Risk-based reporting.

### Phase 4 — Threat Detection

- [ ] Simulated security event ingestion.
- [ ] Detection of repeated failed logins.
- [ ] Identification of predefined suspicious access patterns.
- [ ] Alert generation and event timelines.

### Phase 5 — Cloud Integration

- [ ] AWS IAM policy analysis.
- [ ] S3 configuration security checks.
- [ ] CloudTrail event analysis.
- [ ] Read-only AWS integration in a controlled test account.
- [ ] Security reports for analyzed cloud resources.

*These are planned features, not claims that the features are already implemented.*

---

## 🏗️ System Architecture

The application will use a modular architecture.

```text
                    ┌──────────────────────┐
                    │         User         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Frontend        │
                    │ HTML, CSS, JavaScript│
                    └──────────┬───────────┘
                               │ HTTP / JSON
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI         │
                    │    Backend API       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Input Validation    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Security Analysis    │
                    │    Python Rules      │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    ▼                      ▼
          ┌──────────────────┐   ┌──────────────────┐
          │ Findings and Risk│   │ SQLite Database  │
          │ Remediation      │   │ Scan History     │
          └────────┬─────────┘   └──────────────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ Results Dashboard│
          └──────────────────┘

          Future Integration:
          AWS IAM / S3 / CloudTrail
```

### Workflow

1. The user submits a sample configuration.
2. The frontend sends it to the backend API.
3. The backend validates the submitted data.
4. The security engine evaluates the configuration against predefined rules.
5. The engine generates findings and remediation recommendations.
6. Results are saved in the database.
7. The frontend displays the results to the user.

The future AWS integration will use a separate, explicitly authorized workflow with appropriately restricted permissions.

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| HTML5 | Webpage structure |
| CSS3 | Dashboard styling and layout |
| JavaScript | User interactions and API communication |
| Python | Security analysis and backend logic |
| FastAPI | REST API development |
| Uvicorn | Local API server |
| SQLite | Initial database |
| JSON / YAML | Configuration input formats |
| Git | Version control |
| GitHub | Source code hosting |
| Pytest | Automated testing |
| AWS IAM, S3, CloudTrail | Future cloud security integration |

**Design principle:** Start with simple tools and add complexity only when the project needs it.

---

## 📁 Project Structure

The planned directory structure is:

```text
SentinelCloud/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── main.py
│   ├── scanner/
│   │   ├── __init__.py
│   │   └── rules.py
│   └── tests/
│       ├── __init__.py
│       └── test_rules.py
│
├── data/
│   └── sample_config.json
│
├── docs/
│   └── architecture.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

This structure will be created gradually as the application develops.

---

## 🚀 Getting Started

### Prerequisites

Install the following software:

- [Python](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Git](https://git-scm.com/downloads)
- A modern web browser

Basic programming experience is not required to begin learning this project.

### Step 1 — Create the project folder

Create a folder called `SentinelCloud` and open it in Visual Studio Code.

### Step 2 — Create a Python virtual environment

Open the VS Code terminal in the project directory.

On Windows:

```powershell
py -m venv .venv
```

Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt and run:

```cmd
.venv\Scripts\activate.bat
```

On Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3 — Install the initial backend dependencies

Create a `requirements.txt` file containing:

```text
fastapi
uvicorn[standard]
pytest
```

Install the packages:

```bash
python -m pip install -r requirements.txt
```

For a reproducible setup, dependency versions will be pinned after the initial development environment is tested.

### Step 4 — Verify the installation

Run:

```bash
python -c "import fastapi; print('FastAPI installed successfully')"
```

At this point, the environment is prepared for backend development. The application itself still needs to be implemented.

### Step 5 — Build the first working version

The first development milestone is to:

1. Create the dashboard.
2. Write the first Python security rule.
3. Test the rule with sample configuration data.
4. Expose the scanner through a FastAPI endpoint.
5. Connect the dashboard to the endpoint.
6. Display the findings returned by the backend.

The application will initially run locally. Deployment and AWS integration will come later.

---

## 🗺️ Development Roadmap

| Milestone | Deliverable |
|---|---|
| 1. Foundations | Project setup and basic dashboard |
| 2. Scanner | Working Python configuration checks |
| 3. API | FastAPI endpoint returning findings |
| 4. Integration | Dashboard connected to the scanner |
| 5. Persistence | Scan history stored in SQLite |
| 6. Security | Authentication, authorization, logging and tests |
| 7. Threat detection | Simulated events and alerts |
| 8. Cloud security | Controlled AWS configuration analysis |
| 9. Portfolio | Documentation, demo and final presentation |

Progress will be measured by working, tested features rather than the number of technologies added.

---

## 🔐 Security and Ethical Use

SentinelCloud is intended for defensive security education and authorized security assessment.

- Use sample data or cloud resources you are authorized to assess.
- Never upload real credentials, private keys, access tokens, or sensitive production configurations.
- Validate and limit uploaded files before parsing them.
- Treat configuration files as untrusted input.
- Use least-privilege permissions for any future cloud integration.
- Never store AWS credentials in source code or commit secrets to GitHub.
- Test security features in a controlled environment.
- Do not automatically modify production resources.

Initial findings are rule-based indicators. They should not be treated as proof that a cloud environment is completely secure or compromised.

---

## 📚 Learning Outcomes

Building SentinelCloud is intended to provide hands-on experience with:

- Web development fundamentals.
- Python programming.
- REST APIs and HTTP communication.
- Configuration parsing and validation.
- Cloud security and IAM principles.
- Security monitoring and event analysis.
- Database design.
- Secure software development.
- Automated testing and Git workflows.
- Technical documentation and project presentation.

The project is designed as a learning journey, with each module introducing concepts that will be useful in cybersecurity and cloud security roles.

---

## 🤝 Contributing

This project is being developed as a learning and portfolio project.

Suggestions, improvements, bug reports, and educational contributions are welcome. Any contribution should include a clear explanation of the change and appropriate tests where applicable.

---

## 📄 License

A license has not yet been selected. Before publishing or accepting contributions, choose an appropriate open-source license, such as the MIT License, if it fits your goals.

---

## 👨‍💻 Project Status

## Current Security Rules

SentinelCloud currently analyzes simulated storage configurations using four rules:

| Rule ID | Check | Severity |
|---|---|---|
| `SC-STORAGE-001` | Public access enabled | High |
| `SC-STORAGE-002` | Encryption disabled | Medium |
| `SC-STORAGE-003` | Versioning disabled | Medium |
| `SC-STORAGE-004` | Access logging disabled | Low |

### Input Validation

The scanner validates required Boolean settings and validates optional Boolean settings when they are provided. Invalid or missing required values raise a clear validation error.

### Current Limitations

- Scans use supplied configuration data; live cloud accounts are not scanned.
- Severity levels are project-defined priorities, not a complete risk assessment.
- Missing optional settings are treated as unspecified rather than automatically insecure.
- Remediation guidance is informational and does not change cloud resources.

The first objective is to build a local dashboard and a working rules-based scanner before adding authentication, databases, threat monitoring, or cloud integrations.

**SentinelCloud — Detect misconfigurations. Understand the risk. Improve cloud security.** ☁️🛡️
