def check_escalation(query):
    escalation_keywords = ["refund immediately", "legal", "complaint", "sue", "urgent"]

    query = query.lower()

    if any(word in query for word in escalation_keywords):
        return True
    return False