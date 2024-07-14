def topKfrequent(nums,k):
    elements = {}
    for i, n in enumerate(nums):
        elements[n] = 1 + elements.get(n, 0)
    if len(elements.keys()) == k:
        print(elements.keys())
    frequent = [0]*k


nums = [1,2,2,3,3,4]
topKfrequent(nums, 4)

