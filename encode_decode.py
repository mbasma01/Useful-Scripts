def encode(strs):
    res = ""
    for s in strs:
        res += (str(len(s)) + "#" + s)
    return res

def decode(s):
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        print(s[i:j])
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j

    return res
