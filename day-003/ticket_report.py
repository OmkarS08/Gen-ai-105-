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
        return {
            "word_count": 0,
            "character_count": 0,
            "priority": "normal",
        }

    return {
        "word_count": count_words(ticket_text),
        "character_count": count_characters(ticket_text),
        "priority": detect_priority(ticket_text),
    }


def analyze_tickets(tickets):
    analyzed_tickets = []

    for ticket in tickets:
        analysis = ticket_analyzer(ticket["description"])

        analyzed_ticket = {
            "id": ticket["id"],
            "customer": ticket["customer"],
            "description": ticket["description"],
            "word_count": analysis["word_count"],
            "character_count": analysis["character_count"],
            "priority": analysis["priority"],
        }

        analyzed_tickets.append(analyzed_ticket)

    return analyzed_tickets


tickets = [
    {
        "id": 101,
        "customer": "Asha",
        "description": "My payment failed",
    },
    {
        "id": 102,
        "customer": "Rahul",
        "description": "I need product information",
    },
    {
        "id": 103,
        "customer": "Neha",
        "description": "My account is locked",
    },
]


results = analyze_tickets(tickets)

urgent_count = 0
normal_count = 0

for ticket in results:
    if ticket["priority"] == "urgent":
        urgent_count = urgent_count + 1
    else:
        normal_count = normal_count + 1


for ticket in results:
    print(
        f'Ticket #{ticket["id"]} | '
        f'{ticket["customer"]} | '
        f'{ticket["priority"]} | '
        f'{ticket["word_count"]} words | '
        f'{ticket["character_count"]} characters'
    )


print("\nTicket Summary")
print("Total tickets:", len(results))
print("Urgent tickets:", urgent_count)
print("Normal tickets:", normal_count)


assert len(results) == 3
assert results[0]["priority"] == "urgent"
assert results[1]["priority"] == "normal"
assert results[2]["priority"] == "urgent"
assert urgent_count == 2
assert normal_count == 1

print("\nAll Day 3 tests passed!")