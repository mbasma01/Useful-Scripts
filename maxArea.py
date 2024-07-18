heights = [2, 2, 2]

"""
brute force
"""
"""
ma = 0
for i, n in enumerate(height):
    for j in range(i + 1, len(height)):
        ma = max(min(height[i], height[j]) * (j - i), ma)

print(ma)
"""

def maxArea(heights):
    l, r = 0, len(heights) - 1
    res = 0

    while l < r:
        res = max(min(heights[l], heights[r]) * (r - l), res)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return res

print(maxArea(heights))

