from persona import detect_persona
from knowledge_base import get_knowledge
from escalation import check_escalation


def generate_response(query):
    persona = detect_persona(query)

    if check_escalation(query):
        return f"""
Escalating to Human Agent...

Context Handoff:
Detected Persona: {persona}
Customer Query: {query}
Escalation Reason: High priority keyword detected
"""

    knowledge = get_knowledge(query)

    if persona == "Technical Expert":
        return f"""
Detected Persona: {persona}

Technical Explanation:
{knowledge}

Please verify logs and configuration settings.
"""

    elif persona == "Frustrated User":
        return f"""
Detected Persona: {persona}

I sincerely apologize for the inconvenience.

{knowledge}

Please let me know if you need further assistance.
"""

    else:
        return f"""
Detected Persona: {persona}

{knowledge}
"""


if __name__ == "__main__":
    query = input("Enter customer query: ")
    response = generate_response(query)
    print(response)