import os

# Base directory of project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# JSON database file path
DB_FILE = os.path.join(BASE_DIR, "scans.json")

# Flask settings
FLASK_HOST = "127.0.0.1"
FLASK_PORT = 5000
FLASK_DEBUG = True

# Scanner Settings
REQUEST_TIMEOUT = 5
COMMON_PORTS = [80, 443, 21, 22, 25]

# Required security headers for analysis
REQUIRED_SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options"
]

# Risk weights (you can tune these)
RISK_WEIGHTS = {
    "missing_https": 30,
    "missing_header": 10,
    "open_port": 5,
    "server_exposed": 15
}
