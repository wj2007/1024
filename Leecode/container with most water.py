"""
You are given an integer array 'height' of length 'n'.
There are n vertical lines drawn such that the two endpoints of
the 1st line are (i,0) and (i,height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximun amount of water a container can store
"""

def maxArea(height:list[int]) -> int:
    left = 0
    right = len(height) - 1
    ans = 0

    while left < right:
        area = min(height[left],height[right]) * (right-left)
        ans = max(ans, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return ans        

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))