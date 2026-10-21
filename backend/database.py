
import json
import sqlite3
from pathlib import Path
from typing import Any

DATABASE_PATH = Path(__file__).resolve().parent / "sentinelcloud.db"


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                resource_type TEXT NOT NULL,
                total_findings INTEGER NOT NULL,
                findings_json TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT
                    (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
            )
            """
        )


def save_scan(
    resource_type: str,
    findings: list[dict[str, Any]],
) -> int:
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO scans (
                resource_type,
                total_findings,
                findings_json
            )
            VALUES (?, ?, ?)
            """,
            (
                resource_type,
                len(findings),
                json.dumps(findings),
            ),
        )
        return cursor.lastrowid


def get_scans(limit: int = 20) -> list[dict[str, Any]]:
    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT id, resource_type, total_findings,
                   findings_json, created_at
            FROM scans
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    results = []

    for row in rows:
        results.append({
            "id": row["id"],
            "resource_type": row["resource_type"],
            "total_findings": row["total_findings"],
            "findings": json.loads(row["findings_json"]),
            "created_at": row["created_at"],
        })

    return results
