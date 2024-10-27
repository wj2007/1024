"""
Given an integer array 'nums', 
Move all 0's to the end of it while maintaining the relative order of the 
non-zero relements
Note: must do this in-place without making a copy of the array
"""

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Note - 切片：
# 切片将会产生新数组，所以不能用切片的方式来去除数组中的0元素
# 切片的方式，需要用return 将新数组反馈赋值给原数组

# Note - .remove()
# Python 是用列表来模拟数组，remove()函数可以去除元素，但是返回为空。

# Note - 用双指针可以操作原数组

def moveZeros(nums:list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead
    """
    # 记录所有非0元素的位置
    insert_point = 0

    for num in nums:
        if num is not 0:
            nums[insert_point] = num
            insert_point += 1

    for i in range(insert_point,len(nums)):
        nums[i] = 0        

case1 = [0,1,0,3,12]
case2 = [0]

# Note - 因为原函数return None，所以下述print调用结果也是None
#   print(f"Method of example 1 is {moveZeros(case1)}")
#   print(f"Method of example 2 is {moveZeros(case2)}")        

# 调用函数，注意：函数不返回任何值，因此不需要接收返回值  
moveZeros(case1)  
moveZeros(case2) 

print(f"Method of example 1 is {(case1)}")
print(f"Method of example 2 is {(case2)}")      