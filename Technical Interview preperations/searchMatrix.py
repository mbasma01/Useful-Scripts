matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 4

"""
brute force -- wrong, I could have traversed the matrix and save O(m*n) space

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

"""
optimized approach
"""

def search(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    l, r = 0, n - 1

    # binary search to find the row that possibly has the target
    while l <= r :
        row = (l + r) //2
        if matrix[row][0] < target:
            l = row + 1
        elif matrix[row][-1] > target:
            r = row - 1
        else:
            break

    row = (l + r)//2

    l, r = 0, n - 1

    if l > r:
        return False # we didn't find a row statisfying the conditions

        #binary search on the row we found
    while l <= r:
        m = (l + r)//2
        if matrix[row][m] < target:
            l = m + 1
        elif matrix[row][m] > target:
            r = m - 1
        else:
            return True
    return False

print(search(matrix, target))