# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/

from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        s = set(nums)
        while original in s:
            original *= 2
        return original


