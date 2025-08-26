final_num = -1

prims = [11, 12, 13, 14, 15, 16, 17, 18]
for i in range (1, int(1e16)):
    if (i % 2 == 1):
        continue

    is_divisible = True
    for prim in prims: 
        if (not (i % prim == 0)):
            is_divisible = False
            break
    if is_divisible:
        final_num = i
        break

print(final_num)