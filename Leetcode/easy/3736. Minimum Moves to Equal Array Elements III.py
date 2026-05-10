# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/description/

from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        return (max(nums) * len(nums)) - sum(nums)


