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

s = ""
for i in range(4):
    s = "t".join(s)  # Reassign the result back to s
    print(s)


print(s)