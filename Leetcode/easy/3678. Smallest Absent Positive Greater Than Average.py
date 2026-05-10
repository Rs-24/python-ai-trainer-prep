# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/smallest-absent-positive-greater-than-average/description/

from typing import List

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        s = set(nums)
        avg = sum(nums) // len(nums)
        ans = max(1, avg + 1)
        while ans in s:
            ans += 1
        return ans


