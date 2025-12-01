from flask import Flask, request, jsonify
from scanner.scan_core import run_scan
from database import save_scan, get_scan
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/scan", methods=["POST"])
def scan():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL required"}), 400

    scan_result = run_scan(url)
    scan_id = save_scan(scan_result)

    return jsonify({"scan_id": scan_id, "result": scan_result})

@app.route("/api/scan/<scan_id>", methods=["GET"])
def scan_details(scan_id):
    scan_data = get_scan(scan_id)
    if not scan_data:
        return jsonify({"error": "Not found"}), 404
    return jsonify(scan_data)

if __name__ == "__main__":
    app.run(debug=True)
