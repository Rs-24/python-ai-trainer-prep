# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-integer-added-to-array-i/description/

from typing import List

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # Time: O(m + n), m = len(nums1), n = len(nums2)
        # Space: O(1)
        return min(nums2) - min(nums1)


