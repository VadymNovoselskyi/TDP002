def contains(target, words_list):
    for word in words_list:
        if target == word:
            return True
    return False

haystack = 'Can you find the needle in this haystack?'.split()
print(contains('find', haystack))
print(contains('needle', haystack))
print(contains('haystack', haystack))
  