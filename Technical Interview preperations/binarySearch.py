nums = [-1,0,2,4,6,8]
target = 4

def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r)//2  # in case of overflow m = l + ((r - l)//2)
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
