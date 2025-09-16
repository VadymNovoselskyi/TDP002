def binary_search(list, target, func=None):
    middrle_index = int(len(list) / 2)
    entry = list[middrle_index]
    comparing_entry = func(entry) if func else entry
    if target == comparing_entry:
        return entry
    elif target < comparing_entry:
        return binary_search(list[:middrle_index], target, func)
    elif target > comparing_entry:
        return binary_search(list[middrle_index + 1 :], target, func)


people = [
    {"name": "Pontus", "age": 30},
    {"name": "Pontus999", "age": 30},
    {"name": "Sara", "age": 20},
    {"name": "Sara999", "age": 20},
    {"name": "Xavier1", "age": 19},
    {"name": "Xavier2", "age": 19},
    {"name": "Xavier3", "age": 19},
    {"name": "Xavier4", "age": 19},
    {"name": "Xavier5", "age": 19},
]

print(binary_search(people, "Pontus", lambda e: e["name"]))
print(binary_search(people, "Sara999", lambda e: e["name"]))
print(binary_search(people, "Xavier5", lambda e: e["name"]))
# {'name': 'Pontus', 'age': 30}
