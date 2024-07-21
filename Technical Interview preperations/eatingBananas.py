import math
piles = [25,10,23,4]
h = 6


def minEatingSpeed(piles, h):

    if len(piles) == h:
        return max(piles)

    m = max(piles)
    l, r = 1, m

    res = 1
    while l <= r:
        mid = l + (r-l)//2
        total_time = 0
        for p in piles:
            total_time += math.ceil(float(p)/mid)
        if total_time <= h:
            res = mid
            # check for min
            r = mid - 1
        else:
            l = mid + 1

    return res

print(minEatingSpeed(piles, h))