def linear_search(list, target, func = lambda e : e):
    for entry in list:
        if func(entry) == target:
            return entry

imdb = [
    {'title': 'The Rock', 'actress': 'Nicholas Cage', 'score': 11},          
    {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10},    
    {'title': 'Black Hawk Down', 'actress': 'Eric Bana', 'score': 12},
]

print(linear_search(imdb, 10, lambda e: e['score']))
# > {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10}
