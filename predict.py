THRESHOLD = 0.5


def predict(scores):
    """Nhãn có điểm cao nhất; 'unknown' nếu điểm cao nhất < THRESHOLD."""
    label = max(scores, key=scores.get)
    if scores[label] < THRESHOLD:
        return "unknown"
    return label