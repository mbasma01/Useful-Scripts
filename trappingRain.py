heights = [2,1,4,5]

"""
Attempt 1: Failed
"""
"""
def trap(heights):
    maxLeft, maxRight, oldLeft, oldRight, l, r = 0, 0, 0, 0, 0, len(heights) - 1
    res = 0
    pointsL = 0
    pointsR = 0
    while l < r:
        while heights[l] >= maxLeft:
            maxLeft = heights[l]
            l += 1
        print("Found Max Left", maxLeft)

        while heights[r] >= maxRight:
            maxRight = heights[r]
            r -= 1
        print("Found Max right", maxRight, "current points", pointsL)


        print("checking for", heights[l], heights[r])
        if maxRight == maxLeft:
            res += ((maxLeft - heights[l]) + (maxRight - heights[r]))
            print(f"added {(maxLeft - heights[l]) + (maxRight - heights[r])}")
        elif maxRight > maxLeft:
            res += ((min(maxLeft, maxRight) - heights[l]) + (min(maxRight, maxLeft) - heights[r]))
            pointsL += 1
            print(f"added {(min(maxLeft, maxRight) - heights[l]) + (min(maxRight, maxLeft) - heights[r])}")
        elif maxLeft > maxRight:
            res += ((min(maxLeft, maxRight) - heights[l]) + (min(maxRight, maxLeft) - heights[r]))
            print(f"added {(min(maxLeft, maxRight) - heights[l]) + (min(maxRight, maxLeft) - heights[r])}")
            pointsR += 1

        l += 1
        r -= 1

        oldLeft = maxLeft
        oldRight = maxRight

        if maxLeft > oldLeft:
            res += pointsL*(maxLeft - oldLeft)
            print(f"added {pointsL}")
            #pointsL = 0
        if maxRight > oldRight:
            res += pointsR*(maxRight - oldRight)
            print(f"added {pointsR}")
            #pointsR = 0
        print(res)
    return res
"""
""""
Attempt 2: Failed
"""

"""
def trap(heights):
    res = 0
    l, r = 0, len(heights) -1
    maxLL, maxLR, maxRR, maxRL = 0, 0, 0, 0
    ll, rr = 0,  len(heights)
    heightl, heightr = 0, 0
    while l < r:
        while heights[l] >= maxLL and l < r:
            maxLL = heights[l]
            l += 1
            ll = l
        print(f"LL equals {maxLL}", ll)
        while heights[l] < maxLL and l < r:
            heightl += heights[l]
            l += 1
            maxLR = heights[l]
        print(f"LR equal {maxLR}", l)
        print(f"min is {min(maxLR, maxLL)}")
        if maxLR < maxLL:
            l = 0
        else:
            res += (min(maxLL, maxLR)*(l - ll)) - heightl
            print(f"added {min(maxLL, maxLR) * (l - ll) - heightl}")
        heightl = 0
        while heights[r] >= maxRR and l < r:
            maxRR = heights[r]
            rr = r
            r -= 1
        print(f"RR equals {maxRR}", rr)
        while heights[r] < maxRR and l < r:
            heightr += heights[r]
            r -= 1
            maxRL = heights[r]
        print(f"RL equals {maxRL}", r)
        res += min(maxRR, maxRL)*(rr-r -1) - heightr
        print(f"added {min(maxRR, maxRL)*(rr-r - 1) - heightr}")

        heightr = 0

        maxLL = maxLR
        maxRR = maxRL
    return res
"""


#this can also be done in O(n) space
def trap(height):
    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res

print(trap(heights))