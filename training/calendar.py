first_day = -1
count_days = -1

while first_day < 1 or first_day > 7:
    first_day = int(input("First day of the month (1-7): "))

while count_days < 28 or count_days > 31:
    count_days = int(input("Count of days in the month (28-31): "))

first_row = [str(x) for x in range(first_day, first_day + (7 - first_day) + 1)]
print("må  ti  on  to  fr  lö  sö")
print(f"{" " * 4 * (first_day - 1)}{'   '.join(first_row)}")

rows_count = int((count_days + first_day - 1) / 7)
for i in range(1, rows_count + 1):
    last_index = 7 if i != rows_count else (count_days + first_day - 1) % 7
    numbers = [str(7 * i + x) for x in range(1, last_index + 1)]
    print(f'{'   '.join(numbers)}')
