def topKfrequent(nums,k):
    elements = {}
    freq = [[] for _ in range(len(nums) + 1)]
    for i, n in enumerate(nums):
        elements[n] = 1 + elements.get(n, 0)

    for key, value in elements.items():
        freq[value].append(key)

    res = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


nums = [1,2,2,3,3,4]
topKfrequent(nums, 4)