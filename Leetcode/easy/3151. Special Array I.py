# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/special-array-i/description/

from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        prev_mod = None
        for num in nums:
            if prev_mod is not None and prev_mod == num % 2:
                return False
            prev_mod = num % 2
        return True 


