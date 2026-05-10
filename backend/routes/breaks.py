from datetime import datetime

from flask import Blueprint, jsonify, request

from database.db import get_connection


breaks_bp = Blueprint("breaks", __name__)


@breaks_bp.get("/breaks")
def list_breaks():
    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT id, employee_name, record_type, record_date, record_time, created_at
            FROM break_records
            ORDER BY id DESC
            """
        ).fetchall()

    return jsonify([dict(row) for row in rows])


@breaks_bp.post("/breaks")
def create_break():
    payload = request.get_json(silent=True) or {}
    employee_name = str(payload.get("employee_name", "")).strip()
    record_type = str(payload.get("record_type", "")).strip().lower()

    if not employee_name:
        return jsonify({"error": "employee_name is required"}), 400

    if record_type not in {"start", "end"}:
        return jsonify({"error": "record_type must be start or end"}), 400

    now = datetime.now()
    record_date = payload.get("record_date") or now.strftime("%Y-%m-%d")
    record_time = payload.get("record_time") or now.strftime("%H:%M:%S")

    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO break_records (employee_name, record_type, record_date, record_time)
            VALUES (?, ?, ?, ?)
            """,
            (employee_name, record_type, record_date, record_time),
        )
        connection.commit()

    return (
        jsonify(
            {
                "id": cursor.lastrowid,
                "employee_name": employee_name,
                "record_type": record_type,
                "record_date": record_date,
                "record_time": record_time,
            }
        ),
        201,
    )


@breaks_bp.delete("/breaks")
def clear_breaks():
    with get_connection() as connection:
        connection.execute("DELETE FROM break_records")
        connection.commit()

    return jsonify({"status": "cleared"})
