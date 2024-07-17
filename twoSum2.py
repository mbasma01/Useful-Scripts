numbers = [1,2,3,4]
target = 3
"""
def twoSum(nums, target):
    for i, n in enumerate(nums):
        if (target - n) in nums and (target - n) != n:
            for j in range(i, len(nums)):
                if nums[j] == target - n:
                    return [i+1, j+1]

"""
"""
if sorted
"""

def towSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        currSum = numbers[l] + numbers[r]
        if currSum > target:
            r -= 1
        elif currSum < target:
            l += 1
        else:
            return [l +1, r+ 1]

print(twoSum(numbers, target))
