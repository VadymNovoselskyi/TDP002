def quick_sort(array: list, func=lambda a: a):
    if len(array) < 2:
        return array

    pivot_index = int(len(array) / 2)
    left_part = []
    middle_part = []
    right_part = []
    for element in array:
        if func(element) < func(array[pivot_index]):
            left_part.append(element)
        elif func(element) > func(array[pivot_index]):
            right_part.append(element)
        else:
            if element < array[pivot_index]:
                left_part.append(element)
            elif element > array[pivot_index]:
                right_part.append(element)
            else:
                middle_part.append(element)

    return [
        *quick_sort(left_part, func),
        *middle_part,
        *quick_sort(right_part, func),
    ]


db = [
    ("j", "g"),
    ("a", "u"),
    ("k", "l"),
    ("o", "i"),
    ("b", "s"),
    ("@", "."),
    ("p", "s"),
    ("o", "e"),
]

db = quick_sort(db, lambda e: e[0])
print(db)
