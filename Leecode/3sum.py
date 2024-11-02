"""
Given an integer array nums, return all the triplets.
"""
# Example 1
# input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

def threeSum(nums: list[int]) -> list[list[int]]:

    nums.sort()
    result = []

    for i in range(len(nums)):

        # 避免使用相同的第一个元素
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i+1
        right = len(nums) - 1

        while left < right:
        
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1   # 增加左指针以增大总和
            elif total > 0:
                right -= 1  # 减小右指针以减小总和
            else:
                # 找到一个三元组
                result.append([nums[i], nums[left], nums[right]])  
                
                # 跳过重复的元素
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # 移动指针
                left += 1
                right -= 1

    return result

print(threeSum([-1,0,1,2,-1,-4]))                 


    