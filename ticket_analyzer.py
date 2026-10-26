URGENT_KEYWORDS = [
    "urgent",
    "payment failed",
    "account locked",
    "account is locked",
    "server down",
    "login failed",
]


def count_words(ticket_text):
    return len(ticket_text.split())


def count_characters(ticket_text):
    return len(ticket_text.replace(" ", ""))


def detect_priority(ticket_text):
    normalized_text = ticket_text.lower()

    for keyword in URGENT_KEYWORDS:
        if keyword in normalized_text:
            return "urgent"

    return "normal"


def ticket_analyzer(ticket_text):
    if not ticket_text.strip():
        return {"error": "Problem description cannot be empty"}

    return {
        "word_count": count_words(ticket_text),
        "character_count_without_spaces": count_characters(ticket_text),
        "priority": detect_priority(ticket_text),
    }


assert count_words("payment failed") == 2
assert count_characters("a b c") == 3
assert detect_priority("My SERVER DOWN") == "urgent"
assert detect_priority("Need product information") == "normal"

print("All tests passed!")

problem = input("Enter the problem description: ")
result = ticket_analyzer(problem)
print(result)