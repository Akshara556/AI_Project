def detect_persona(query):
    query = query.lower()

    frustrated_keywords = ["again", "not working", "failed", "issue", "problem", "angry", "bad"]
    technical_keywords = ["api", "error", "401", "token", "server", "integration"]

    if any(word in query for word in frustrated_keywords):
        return "Frustrated User"
    elif any(word in query for word in technical_keywords):
        return "Technical Expert"
    else:
        return "General User"