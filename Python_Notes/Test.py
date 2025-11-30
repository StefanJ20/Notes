def TwoSums(nums, target):
    map = {}
    for i, num in enumerate(nums):
        complement = num - target
        if complement in map:
            return [map[complement], i]
        map[num] = i

nums = [2, 7, 11, 15]
target = 26
print(TwoSums(nums, target))  # Output: [0, 1]