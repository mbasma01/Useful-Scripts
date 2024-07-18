s = " "

""""
1st attempt: Success

def LongestSubstring(s):
    res = 0
    l = 0
    for i, n in enumerate(s):
        l = 0
        checked = set()
        for j in range(i, len(s)):
            if s[j] in checked:
                break
            else:
                l += 1
                checked.add(s[j])
        res = max(res, l)
    return res
"""
def LongestSubstring(s):
    res = 0
    checked = set()
    l = 0
    for r in s:
        while s[r] in checked:
            checked.remove(s[l])
            l += 1
        checked.add(s[r])
        res = max(res, r - l + 1)
    return res



    return res



print(LongestSubstring(" "))