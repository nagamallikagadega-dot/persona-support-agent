def check_escalation(user_message: str, persona: str) -> dict:
    escalation_keywords = [
        "refund", "legal", "lawsuit", "cancel", "immediate",
        "demand", "unacceptable", "fraud", "duplicate charge",
        "billing error", "worst", "horrible"
    ]
    
    message_lower = user_message.lower()
    
    triggered_keywords = [kw for kw in escalation_keywords if kw in message_lower]
    
    should_escalate = len(triggered_keywords) > 0 and persona == "Frustrated User"
    
    return {
        "should_escalate": should_escalate,
        "reason": f"Sensitive keywords detected: {', '.join(triggered_keywords)}" if triggered_keywords else "No escalation needed",
        "handoff_json": {
            "escalation": True,
            "persona": persona,
            "keywords": triggered_keywords,
            "priority": "HIGH" if should_escalate else "NORMAL"
        }
    }
