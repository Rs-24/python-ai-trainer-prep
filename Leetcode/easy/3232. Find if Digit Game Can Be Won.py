# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-if-digit-game-can-be-won/description/

from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        return sum(num for num in nums if num >= 10) != sum(num for num in nums if num < 10)


