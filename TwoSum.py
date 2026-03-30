nums = [2,7,11,15,3,6,4,8,1]
target = 9 
ans = []

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and nums[i] + nums[j] == target:
                ans.append([nums[i], nums[j]])

twoSum(nums, target)
print(ans)

import numpy as np

arr = np.array([2,7,11,15,3,6,4,8,1])
target = 9

sum_matrix = arr[:, None] + arr

rows, cols = np.where(sum_matrix == target)

result = [f"{arr[i]} + {arr[j]} = {target}" for i, j in zip(rows, cols) if i < j]

print(result)

