def calculate_risk(features):

    score = 0

    if not features["https"]:
        score += 30

    score += features["missing_headers"] * 10
    score += len(features["open_ports"]) * 5

    if features["server_exposed"]:
        score += 15

    level = (
        "Low" if score < 30 else
        "Medium" if score < 70 else
        "High"
    )

    return score, level
