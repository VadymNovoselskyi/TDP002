lowest_amount = -1
while lowest_amount <= 0:
    lowest_amount = int(input("Lowest amount: "))

highest_amount = -1
while highest_amount <= lowest_amount:
    highest_amount = int(input("Highest amount: "))

step = -1
while step <= 0 or step > highest_amount - lowest_amount:
    step = float(input("Step: "))

moms = -1
while moms <= 0 or moms >= 100:
    moms = int(input("Moms percent: "))

inverted_step = 1 / step
amounts = [
    round(x * step, 2)
    for x in range(
        int(lowest_amount * inverted_step), int(highest_amount * inverted_step) + 1
    )
]

print(f"{"=== Momstabell ===":^55}")
print(f"{"Amount without moms":<25}{"Moms":<10}{"Amount with moms":<20}")
for amount in amounts:
    moms_amount = round(amount * (moms / 100), 2)
    print(f"{amount:<25}{moms_amount:<10.2f}{(amount + moms_amount):<20.2f}")
