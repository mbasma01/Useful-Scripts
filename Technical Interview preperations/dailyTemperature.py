temps = [30,38,30,36,35,40,28]
"""
brute force O(n^2)

def dailyTemp(temps):
    res = [0]*len(temps)

    for i in range(len(temps) - 1):
        for j in range(i+1, len(temps)):

            if temps[j] > temps[i]:
                res[i] += 1
                print(i, temps[i], j, temps[j])
                break
            elif j == len(temps) - 1:
                res[i] = 0
                break
            else:
                res[i] += 1
    return res
"""

"""Optimized to O(n) with O(n) space"""
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []  # pair: [temp, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append((t, i))
    return res

print(dailyTemp(temps))

