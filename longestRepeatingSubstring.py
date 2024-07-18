from collections import defaultdict
s = "AAABABB"
k = 1
def characterReplacement(s, k):
    res = 0
    checked = {}
    l = 0
    maxf = 0

    for r in range(len(s)):
        checked[s[r]] = 1 + checked.get(s[r], 0)
        maxf = max(maxf, checked[s[r]])

        # while sum(checked.values()) - max(checked.values()) > k:
        while (r - l + 1) - maxf > k:
            checked[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

print(characterReplacement(s, k))


