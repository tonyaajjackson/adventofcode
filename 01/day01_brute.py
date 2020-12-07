with open("input_nums", 'r') as f:
    nums = [int(num) for num in f.read().split("\n") if num != ""]

for (i, num1) in enumerate(nums):
    for num2 in nums[i:]:
        if (num1 + num2) == 2020:
            print("Found it!")
            print("num1: " + str(num1))
            print("num2: " + str(num2))
            print("product: " + str(num1 * num2))