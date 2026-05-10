# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/description/

from typing import List

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        unique = sorted(list(set(nums)), reverse=True)
        return unique[:k]


