# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-number-game/description/

from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # Time: O(n log n), n = len(nums)
        # Aux space: O(n)
        nums.sort()
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums


