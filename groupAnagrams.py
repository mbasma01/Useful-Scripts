from collections import defaultdict
def groupAnagram(strs):
    res = defaultdict(list)
    for str in strs:
        count = [0]*26
        for s in str:
            count[ord(s) - ord("a")] += 1
        res[tuple(count)].append(str)
        print(res)

strs = ["act","pots","tops","cat","stop","hat"]
groupAnagram(strs)