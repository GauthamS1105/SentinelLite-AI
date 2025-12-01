from .utils import check_https, get_headers, scan_ports
from .risk_model import calculate_risk
from urllib.parse import urlparse

# ⭐ Add the URL normalizer function HERE
def normalize_url(url):
    # If protocol missing, assume HTTPS
    if not url.startswith("http://") and not url.startswith("https://"):
        return "https://" + url
    return url


def run_scan(url):

    # ⭐ Normalize the URL BEFORE the scan begins
    url = normalize_url(url)

    headers = get_headers(url)

    features = {
        "https": check_https(url),
        "missing_headers": 0,
        "open_ports": [],
        "server_exposed": False
    }

    required_headers = [
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Frame-Options",
        "X-Content-Type-Options"
    ]

    for h in required_headers:
        if h not in headers:
            features["missing_headers"] += 1

    if "Server" in headers:
        features["server_exposed"] = True

    # Extract domain safely
    domain = urlparse(url).hostname

    if domain:  # Prevent crash if URL is invalid
        features["open_ports"] = scan_ports(domain)
    else:
        features["open_ports"] = []

    score, level = calculate_risk(features)

    return {
        "url": url,
        "features": features,
        "risk_score": score,
        "risk_level": level
    }
