# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/description/

from typing import List

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        # Time: O(m + n), m = len(nums1), n = len(nums2)
        # Space: O(m + n)
        temp = set(nums1) & set(nums2)
        if len(temp) > 0:
            return min(temp)
        return min(min(nums1), min(nums2)) * 10 + max(min(nums1), min(nums2))


