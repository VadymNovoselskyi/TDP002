numbers = [4, -2, 7, 10, -5, 3]

def reduce_sum(nums):
    return my_reduce(lambda acc, cur: acc + cur, nums)

def reduce_len(nums):
    return my_reduce(lambda acc, _: acc + 1, nums, 0)

def reduce_minmax(nums):
    return my_reduce(
        lambda acc, cur: [cur if cur < acc[0] else acc[0], cur if cur > acc[1] else acc[1]],
        nums,
        [float('inf'), float('-inf')]
    )

def reduce_avg(nums):
    sum = reduce_sum(nums)
    len = reduce_len(nums)
    return sum/len

def reduce_only_neg(nums):
    return my_reduce(lambda acc, cur: [*acc, cur] if cur < 0 else acc, nums, [])

def filter_only_neg(nums):
    return list(filter(lambda value: value < 0, nums))

def reduce_minmaxsum(nums):
    return my_reduce(
        lambda acc, cur: [
            cur if cur < acc[0] else acc[0],
            cur if cur > acc[1] else acc[1],
            acc[2] + cur
        ],
        nums,
        [float('inf'), float('-inf'), 0]
    )

def builder(comparison: int, less_than=True):
    if less_than:
        return lambda acc, cur: [*acc, cur] if cur < comparison else acc
    else:
        return lambda acc, cur: [*acc, cur] if cur > comparison else acc

def my_reduce(func, iterable, initial=None):
    if initial is not None:
        acc = initial
        skip_first = False
    else:
        acc = iterable.copy()[0]
        skip_first = True
    
    for item in iterable:
        if skip_first:
            skip_first = False
            continue
        acc = func(acc, item)
    return acc

if __name__ == "__main__":
    print(numbers)
    print(reduce_sum(numbers))
    print(reduce_len(numbers))
    print(reduce_minmax(numbers))
    print(f"{reduce_avg(numbers):.4f}")
    print(reduce_only_neg(numbers))
    print(filter_only_neg(numbers))
    print(reduce_minmaxsum(numbers))
    my_func = builder(4, less_than=True)
    print(my_reduce(my_func, numbers, []))