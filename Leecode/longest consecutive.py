"""
Given an unsorted array of integers 'nums',
Return the length of the longest consecutive elements sequence.
"""

# Example 1 
# Input: nums = [100,4,200,1,3,2]
# Output: 4

# Example 2
# Input: nums = [1,2,0,1]
# Output: 2

def longestConsecutive(nums: list[int]) -> int:
        
    if not nums:
        return 0

    # 直接在 nums 上排序，避免使用额外的列表，也可以用set函数去重 sorted(set(nums))
    nums = sorted(nums)  
    longest_streak = 1   # 已知最长的连续数列，因为可以有很多个连续数列
    current_streak = 1   # 当前连续数列长度

    for i in range(1,len(nums)):
        if nums[i-1] + 1 == nums[i]:
            current_streak += 1
        else:
            longest_streak = max(longest_streak,current_streak)
            current_streak = 1  # 打破连续点，重新开始计算

    longest_streak = max(longest_streak,current_streak)
    return longest_streak  

case1 = [100,4,200,1,3,2]
case2 = [1,2,0,1]
print(f"Method of example 1 is {longestConsecutive(case1)}")
print(f"Method of example 2 is {longestConsecutive(case2)}")