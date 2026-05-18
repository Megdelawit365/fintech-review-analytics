def assign_theme(text):

    text = str(text).lower()

    if any(x in text for x in ["login", "otp", "password"]):
        return "Login Issues"

    if any(x in text for x in ["transfer", "transaction", "payment"]):
        return "Transaction Issues"

    if any(x in text for x in ["slow", "crash", "bug", "error"]):
        return "Performance Issues"

    if any(x in text for x in ["ui", "interface", "design", "easy", "user friendly"]):
        return "UI/UX"

    return "Other"
