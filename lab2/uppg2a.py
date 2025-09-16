def frame(str):
    print("*" * (len(str) + 4))
    print(f"* {str} *")
    print("*" * (len(str) + 4))


frame_str = input("Your frame_str: ")
frame(frame_str)
print()


def triangle(num):
    acc = 1
    for _ in range(1, num + 1):
        print("*" * acc)
        acc += 2


triangle_num = int(input("Your triangle_num: "))
triangle(triangle_num)
print()


def flag(num):
    for i in range(1, (num * 11) + 1):
        if i == num * 5 + 1:
            print()
            continue
        row = "*" * (num * 10)
        print(f"{row} {row}")


flag_num = int(input("Your flag_num: "))
flag(flag_num)
print()
