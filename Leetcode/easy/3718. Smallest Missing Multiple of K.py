# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/smallest-missing-multiple-of-k/description/

from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        s = set(nums)
        i = 1
        while i * k in s:
            i += 1
        return i * k


