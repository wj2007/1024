"""
Given an array of strings 'strs'
Group the anagrams together.
You can return the answer in any order.
"""

# Example 1
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2
# Input: strs = [""]
# Output: [[""]]

  
def groupAnagrams(strs:list[str]) -> list[list[str]]:

    # 定义字典，Key是sorted_s, Value是符合sorted_s的str数组 
    anagrams_dict = {}  
    for s in strs:

        # 对strs的每个字符排序并将排序后的字符重新拼接起来
        sorted_s = ''.join(sorted(s))

        if sorted_s in anagrams_dict:
            anagrams_dict[sorted_s].append(s)
        else:
            # 用list S赋值，否则不能append
            anagrams_dict[sorted_s] = [s]  
            
    # 返回字典Value
    return (anagrams_dict.values())  

case1 = ["eat","tea","tan","ate","nat","bat"]
print(f"Mothod 1 of Example 1 is {groupAnagrams(case1)}")

case2 = [""]
print(f"Mothod 1 of Example 2 is {groupAnagrams(case2)}")


