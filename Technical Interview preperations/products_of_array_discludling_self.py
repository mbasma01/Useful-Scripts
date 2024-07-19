"""
Input: nums = [1,2,4,6]

Output: [48,24,12,8]
"""

nums = [1,2,4,6]
"""
O(n) but fails with zeros

product = 1
res = [0]*len(nums)
zero_product = -1
for i, n in enumerate(nums):
    print(i, n, zero_product)
    if n == 0:
        zero_product = i
    else:
        product *= n

if zero_product != -1:
    res = [0]*len(nums)
    res[zero_product] = product
    print(res)
else:
    for i, n in enumerate(nums):
        print(i, n)
        res[i] = product/n
    print(res)
"""

res = [1]*len(nums)

for i in range(1, len(nums)):
    res[i] = res[i - 1] * nums[i - 1]

product = 1

for i in range(len(nums) - 1, -1, -1):
    res[i] *= product
    product *= nums[i]

print(res)