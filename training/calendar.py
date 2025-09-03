from datetime import datetime

PADDING_LEN = 4
months_len = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
days = ["må", "ti", "on", "to", "fr", "lö", "sö"]


def padd(str):
    return str.ljust(PADDING_LEN)


# while first_day < 1 or first_day > 7:
#     first_day = int(input("First day of the month (1-7): "))

# while count_days < 28 or count_days > 31:
#     count_days = int(input("Count of days in the month (28-31): "))


def print_month(first_day, count_days, offset=0):
    print(offset)
    last_index = -1
    first_row = [str(x + offset) for x in range(1, 7 - first_day + 2)]

    print(f"{''.join(map(padd, days))}")
    print(f"{"":<{(first_day - 1) * PADDING_LEN}}{''.join(map(padd, first_row))}")

    rows_count = int((count_days + first_day - 1) / 7)
    for i in range(1, rows_count + 1):
        last_index = 7 if i != rows_count else (count_days + first_day - 1) % 7
        numbers = [
            str((7 * i + x - first_day + 1) + offset) for x in range(1, last_index + 1)
        ]
        print(f"{''.join(map(padd, numbers))}")

    print()
    return last_index


current_year = int(datetime.today().strftime("%Y"))
current_month = int(datetime.today().strftime("%m"))
# current_day = int(datetime.today().strftime("%d"))
current_day = 10
current_weekday = int(datetime.today().weekday())

first_day = current_weekday + 1
count_days = months_len[current_month % 12]
count_month = 0
offset = 0
if current_day - (current_weekday + 1) >= 0:
    first_day = (current_day - current_weekday) % 7
    offset = current_day - 1

while count_month < 11:
    print(f"{current_year} - {months[current_month - 1]}")
    count_days = months_len[current_month % 12]
    first_day = print_month(first_day + (offset % 7), count_days - offset, offset) + 1
    count_month += 1
    current_month += 1
    offset = 0

    if current_month % 12 == 0:
        current_month = 1
        current_year += 1
