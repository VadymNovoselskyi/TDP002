PADDING_LEN = 4
days = ["må", "ti", "on", "to", "fr", "lö", "sö"]
first_day = -1
count_days = -1
count_month = 0


def padd(str):
    return str.ljust(PADDING_LEN)


while first_day < 1 or first_day > 7:
    first_day = int(input("First day of the month (1-7): "))

while count_days < 28 or count_days > 31:
    count_days = int(input("Count of days in the month (28-31): "))


def print_month(first_day, count_days):
    last_index = -1
    first_row = [str(x) for x in range(1, 7 - first_day + 2)]

    print(f"{''.join(map(padd, days))}")
    print(f"{"":<{(first_day - 1) * PADDING_LEN}}{''.join(map(padd, first_row))}")

    rows_count = int((count_days + first_day - 1) / 7)
    for i in range(1, rows_count + 1):
        last_index = 7 if i != rows_count else (count_days + first_day - 1) % 7
        numbers = [str(7 * i + x - first_day + 1) for x in range(1, last_index + 1)]
        print(f"{''.join(map(padd, numbers))}")

    print()
    return last_index


while count_month < 12:
    first_day = print_month(first_day, count_days) + 1
    count_month += 1
