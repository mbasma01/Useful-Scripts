nums = [3, 4, 5, 6]
target = 7

"""
brute force
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums [j] == target:
            print("Found it!", nums[i], " + ", nums[j], " = ", target)
            break
"""

"""
1-pass
checkedMap = {}
for i, n in enumerate(nums):
    print(i, n)
    diff = target - n
    if diff in checkedMap:
        print([checkedMap[diff], i])
        break
    checkedMap[n] = i
    print(checkedMap)
    
"""
