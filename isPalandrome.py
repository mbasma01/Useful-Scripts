s = "0P"

"""
first attempt

def isPalindrome(s):
    if s == "":
        return True
    new_s = ""

    for char in s:
        if char.isalpha() or char.isnumeric():
            new_s += char.lower()
    j = len(new_s) - 1
    for i in range(len(new_s)//2):
        if new_s[i] != new_s[j]:
            print(new_s[i], new_s[j])
            return False
        j -= 1
    return True
"""

def isPalindrome(s):
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not(s[l].isalpha() or s[l].isnumeric()):
            l += 1
        while l < r and not(s[r].isalpha() or s[r].isnumeric()):
            r -= 1

        if s[l].lower() !=  s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True
print(isPalindrome(s))