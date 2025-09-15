def insertion_sort(db, func = lambda a : a):
    for i in range(len(db)):
        element = func(db[i])

        j = i - 1
        while (element < func(db[j]) or (element == func(db[j]) and db[j + 1] < db[j])) and j >= 0:
            temp = db[j]
            db[j] = db[j + 1]
            db[j + 1] = temp
            j -= 1

    return db

db = [
    ('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
    ('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
]

db = insertion_sort(db, lambda e: e[0])
print(db)