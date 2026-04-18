def generate_summary(text):
    if not text:
        return "No content available to summarize."

    # Simple summary logic (first 2 lines)
    sentences = text.split(".")
    summary = ".".join(sentences[:2])

    return summary.strip()