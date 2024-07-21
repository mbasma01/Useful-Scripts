def threeSum(numbers):
    res = []
    numbers.sort()

    for i, n in enumerate(numbers):
        if i > 0 and n == numbers[i -1]:
            continue
        l, r = i + 1, len(numbers) - 1

        while l < r:
            s = n + numbers[l] + numbers[r]

            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                res.append([n, numbers[l], numbers[r]])
                l += 1
                r -= 1
                while numbers[l] == numbers[l -1] and l < r:
                    l += 1
    return res


