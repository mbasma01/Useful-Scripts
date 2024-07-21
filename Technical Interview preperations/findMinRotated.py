nums = [2,3,4,5]


def findMin(nums):
    l, r = 0, len(nums) - 1
    m = float('inf')
    while l < r:
        mid = (l + r) // 2
        m = min(m, nums[mid])
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid - 1

    return min(m, nums[l])


print(findMin(nums))