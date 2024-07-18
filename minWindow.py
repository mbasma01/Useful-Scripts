s = "OUZODYXAZV"
t = "XYZ"

def minWindow(s, t):
    if t == "":
        return ""

    countS, countT = {}, {}

    for char in t:
        countT[char] = 1 + countT.get(char, 0)

    have, need = 0, len(countT)
    #results should be a couple (startIndex, stopIndex)
    res, resLen = [-1, -1], float("infinity")
    l = 0

    for r in range(len(s)):
        c = s[r]
        countS[c] = 1 + countS.get(c, 0)

        if c in countT and countS[c] == countT[c]:
            have += 1

        while have == need:
            if (r - l + 1) < resLen:
                resLen = r - l + 1
                res = [l, r]

            countS[s[l]] -= 1

            if s[l] in countT and countS[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l: r + 1] if resLen != float("infinity") else ""