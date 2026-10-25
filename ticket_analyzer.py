def ticket_analyzer(ticket_text):
    ticket_text = ticket_text.lower()
    words = ticket_text.split()

    word_count = len(words)
    char_count = 0

    for word in words:
        char_count = char_count + len(word)

    urgent_keywords = [
        "urgent",
        "payment failed",
        "account locked",
        "server down",
        "login failed",
    ]

    priority = "normal"

    for keyword in urgent_keywords:
        if keyword in ticket_text:
            priority = "urgent"
            break

    return {
        "word_count": word_count,
        "character_count_without_spaces": char_count,
        "priority": priority,
    }


problem = input("Enter the problem description: ")
result = ticket_analyzer(problem)
print(result)