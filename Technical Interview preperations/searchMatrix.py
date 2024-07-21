matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 7

"""
brute force

def matrixToArray(matrix):
    m = len(matrix)
    n = len(matrix[0])
    res = [0]* (m * n)
    idx = 0
    for i in range(m):
        for j in range(n):
            res[idx] = matrix[i][j]
            idx += 1
    return res
def search(matrix, target):
    nums = matrixToArray(matrix)
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (r-l)//2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return True
    return False

"""
print(search(matrix, target))