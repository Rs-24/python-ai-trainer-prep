# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        return len({num for num in nums if num != 0})


