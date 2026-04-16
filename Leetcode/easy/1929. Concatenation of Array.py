# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/concatenation-of-array/description/

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Aux space: O(1)
        return nums * 2


