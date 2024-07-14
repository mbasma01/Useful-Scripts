"""
sorting approach

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(isAnagram("abc", "bad"))
"""

"""
optimized solution

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

print(isAnagram("abc", "bac"))
"""

