# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximize-expression-of-three-elements/description/

from typing import List

class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        first = second = float("-inf")
        mn = float("inf")
        for num in nums:
            if num >= first:
                second = first
                first = num
            elif num >= second:
                second = num
            if num < mn:
                mn = num
        return first + second - mn


