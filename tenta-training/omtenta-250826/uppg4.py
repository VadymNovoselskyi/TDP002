import math


def my_sort(nums: list[int]):
    if len(nums) < 2:
        return nums
    left_part = []
    middle_part = []
    right_part = []
    pivot = nums[int(len(nums) / 2)]
    for num in nums:
        if num < pivot:
            left_part.append(num)
        elif num == pivot:
            middle_part.append(num)
        elif num > pivot:
            right_part.append(num)
    return [*my_sort(left_part), *middle_part, *my_sort(right_part)]

def get_pair(target: int, num_a: int, nums_b: list[int]):
    closest_num = float("inf")
    closest_distance = float("inf")
    for num_b in nums_b:
        dist = math.fabs(num_a + num_b - target)
        if dist < closest_distance:
            closest_distance = dist
            closest_num = num_b
    return closest_num

def fill_double_list(part_a: list[int], part_b: list[int], target: int):
    double_list = []
    for num_a in part_a:
        num_b = get_pair(target, num_a, part_b)
        double_list.append([num_a, num_b])
    return double_list


target = 12
numbers = [1, 3, 5, 8, 10, 11, 4, 7]

sorted_numbers = my_sort(numbers)
middle = int(len(sorted_numbers) / 2)
part_a = sorted_numbers[:middle]
part_b = sorted_numbers[middle:]
result = fill_double_list(part_a, part_b, target)
print(result)
