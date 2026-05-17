def assign_theme(text):
    text = text.lower()

    if any(w in text for w in ["login", "otp", "password", "verify"]):
        return "Account Issues"
    elif any(w in text for w in ["transfer", "payment", "failed"]):
        return "Transaction Issues"
    elif any(w in text for w in ["crash", "slow", "error", "freeze"]):
        return "Performance Issues"
    elif any(w in text for w in ["ui", "design", "easy", "navigation"]):
        return "UI/UX"
    else:
        return "Other"
