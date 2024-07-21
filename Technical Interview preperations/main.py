"""
Freddy's question

def has_path(nums):
    mi = min(nums[0], nums[len(nums) - 1])
    #mi = 1
    ma = max(nums[0], nums[len(nums) - 1])
    #ma = 5

    if mi == ma:
        return (mi + 1) in nums or (mi - 1) in nums

    for i in range(mi + 1, ma):
        if i in nums:
            continue
        else:
            return False
    return True

nums = [1, 2, 1, 2, 1]
print(has_path(nums))
"""
"+3 or -5"

"""
graph
2, -3, 0
"""

nums = [-1,0,2,4,6,8]
target = 4
def binarySearch(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r)//2
        print(l, r, m)
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m

print(binarySearch(nums, target))