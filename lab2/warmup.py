# 1
# def main():
#     numbers = [1, 2, 3]
#     numbers_refernce = numbers
#     return None

# if __name__=="__main__":
#     main()

# 2
# def main():
#     numbers = [1, 2, 3]
#     numbers_refernce = numbers.copy()
#     return None

# if __name__=="__main__":
#     main()

# 3
# def main():
#     numbers = [1, 2, 3, 4]
#     print(add_element(numbers, 0))

# def add_element(l, e):
#     if len(l) == 0:
#         return e
#     return add_element(l[1:], e + l[0])

# if __name__=="__main__":
#     main()

# 4
def main():
    numbers = [1, 2, 3]
    print(add_element([1, 2, 3, 4], 0))

def add_element(l, e):
    if len(l) == 0:
        return e
    return add_element(l[1:], e + l[0])

if __name__=="__main__":
    main()