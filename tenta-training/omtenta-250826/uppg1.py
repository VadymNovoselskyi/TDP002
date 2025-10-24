def collatz(n):
    print(n)
    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(n * 3 + 1)
        print(n)


print("n = 1:", end=" ")
collatz(1)
print()

print("n = 2:", end=" ")
collatz(2)
print()

print("n = 3:", end=" ")
collatz(3)
print()

print("n = 128:", end=" ")
collatz(128)
print()
