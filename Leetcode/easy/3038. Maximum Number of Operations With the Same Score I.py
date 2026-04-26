# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/description/

from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        need = nums[0] + nums[1]
        count = 1
        i = 2
        while i < len(nums) - 1 and nums[i] + nums[i + 1] == need:
            i += 2
            count += 1
        return count


