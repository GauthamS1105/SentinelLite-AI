import json
import uuid
import os

DB_FILE = "scans.json"

def save_scan(data):
    scan_id = str(uuid.uuid4())
    data["id"] = scan_id

    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump([], f)

    with open(DB_FILE, "r") as f:
        all_scans = json.load(f)

    all_scans.append(data)

    with open(DB_FILE, "w") as f:
        json.dump(all_scans, f, indent=4)

    return scan_id

def get_scan(scan_id):
    if not os.path.exists(DB_FILE):
        return None

    with open(DB_FILE, "r") as f:
        scans = json.load(f)

    for scan in scans:
        if scan["id"] == scan_id:
            return scan

    return None
