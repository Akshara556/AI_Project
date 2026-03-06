knowledge = {
    "401": "A 401 error usually indicates an authentication failure. Please verify your API key, token validity, and headers.",
    "api": "API issues may arise due to incorrect endpoint, invalid credentials, or server misconfiguration.",
    "payment": "Payment failures can occur due to insufficient balance, expired card, or network timeout.",
    "refund": "Refunds are typically processed within 5–7 business days depending on the payment provider."
}

def get_knowledge(query):
    query = query.lower()

    for key in knowledge:
        if key in query:
            return knowledge[key]

    return "No relevant knowledge found."