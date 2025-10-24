from functools import reduce


def sum_number_string(string):
    nums = string.split(" ")
    res = 0
    for num in nums:
        res += int(num)
    return res


if __name__ == "__main__":
    s1 = "1 2 3 4 5"
    print(f"Summan av '{s1}' Ã¤r {sum_number_string(s1)}")  # 15

    s2 = "-2 10 -5 7"
    print(f"Summan av '{s2}' Ã¤r {sum_number_string(s2)}")  # 10

    s3 = "100 200 300 400 500"
    print(f"Summan av '{s3}' Ã¤r {sum_number_string(s3)}")  # 1500
