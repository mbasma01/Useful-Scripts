nums = [2,20,4,10,3,4,5]
"""
1st attempt

def LCS(nums):
    nums = set(nums)
    if nums == []:
        return 0
    if len(nums) == 1:
        return 1

    points = []
    m = 0
    for i, n in enumerate(nums):
        if n - 1 not in nums:
            points.append(n)
    nums = sorted(nums)
    length  = 0
    for i, n in enumerate(nums):
        #print(i, n)
        if n in points:
            length = 1
        else:
            length += 1
            m = max(length, m)
            #print(points, m, length)

    return m
print(LCS(nums))

"""

""""
neat code | cleaner version
"""

def LCS(nums):
    nums = set(nums)
    m = 0
    for  n in nums:
        if n - 1 not in nums:
            length = 1
            while (n + length) in nums:
                length += 1
            m = max(m, length)
    return m
print(LCS(nums))