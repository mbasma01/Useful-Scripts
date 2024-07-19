"""
brute force approach

def hasDuplicates(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                print(nums[i], nums[j])
                return True

    return False

print(hasDuplicates([1,2,3,3]))
"""

"""
sorting approach

def hasDuplicates(nums):
    nums =  sorted(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums [i + 1]:
            return True
    return False
print(hasDuplicates([1,2,3,4]))
"""
"""
hashsets

def hasDuplicates(nums:list[int]):
    if nums == []:
        return False
    hashset = set(nums)
    if len(nums) == len(hashset):
        return False
    return True
print(hasDuplicates([1,2,3,3]))
"""


