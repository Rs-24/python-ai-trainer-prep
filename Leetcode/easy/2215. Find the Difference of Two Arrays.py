# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Time: O(m + n), m = len(nums1), n = len(nums2)
        # Aux space: O(m + n)
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1 - s2), list(s2 - s1)]


