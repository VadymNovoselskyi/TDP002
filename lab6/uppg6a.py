# total_mul = 1
# for i in range(1, 513):
#     total_mul *= i
# print(total_mul)

# total_sum = 0
# for i in range(513):
#     total_sum += i
# print(total_sum)

def my_reduce(list, func, acc):
    for item in list:
        acc = func(acc, item)
    return acc

nums = [x for x in range(1, 513)]

sum = my_reduce(nums, lambda acc, num : acc + num, 0)
# print(sum)

mul = my_reduce(nums, lambda acc, num : acc * num, 1)
print(mul)