# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-common-elements-between-two-arrays/description/

from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time: O(m + n), m = len(nums1), n = len(nums2)
        # Space: O(m + n)
        s1 = set(nums1)
        s2 = set(nums2)
        answer1 = sum(1 for num in nums1 if num in s2)
        answer2 = sum(1 for num in nums2 if num in s1)
        return [answer1, answer2]


