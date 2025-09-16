db = [
    {"name": "Jakob", "position": "assistant"},
    {"name": "Åke", "position": "assistant"},
    {"name": "Ola", "position": "examiner"},
    {"name": "Ola2", "position": "examiner"},
    {"name": "Henrik", "position": "assistant"},
]


def db_search(db, field, value):
    matched = []
    for entry in db:
        if entry.get(field) == value:
            matched.append(entry)

    return matched


print(db_search(db, "position", "examiner"))
