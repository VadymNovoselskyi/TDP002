final_num = -1

for i in range (1, int(1e16)):
    is_divisible = True
    for j in range(1, 14): 
        if (not (i % j == 0)):
            is_divisible = False
            break
    if is_divisible:
        final_num = i
        break

print(final_num)