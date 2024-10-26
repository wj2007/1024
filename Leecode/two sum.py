"""
Given an arrays of integers 'nums' and an integer 'target', 
Return indices of the two numbers such that they add up to 'target'.
You may assume that each input would have eactly one solution,
And you may not use the same element twice.
You can return the answer in any order
"""

# Example 1
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Example: 2
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

def twoSum(nums:list[int],target:int)->list[int]:

    for i in range(len(nums)):
        res = target - nums[i]
        if res in nums[i+1:]:
            return[i,nums[i+1:].index(res)+i+1]


# nums[i+1:]: 切片数组从i+1往后的所有值
# nums[i+1:].index(res): 数值=res的索引，从nums[i+1:]的第一个数算0
# nums[i+1:].index(res)+i+1: 该索引在原数组中的索引

case1 = twoSum(nums=[2,7,11,15],target=9)
case2 = twoSum(nums=[3,2,4],target=6)
print(f'Methon #1 of example 1 is {case1}, and example 2 is {case2}')

def twoSum_2(nums:list[int],target:int)->list[int]:

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if target == nums[i] + nums[j]:
                return [i,j]
            
case1_1 = twoSum(nums=[2,7,11,15],target=9)
case2_2 = twoSum(nums=[3,2,4],target=6)
print(f'Methon #2 of example 1 is {case1_1}, and example 2 is {case2_2}')
          