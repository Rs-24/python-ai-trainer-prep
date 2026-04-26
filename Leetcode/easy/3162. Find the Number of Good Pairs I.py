# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-number-of-good-pairs-i/description/

from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Time: O(n * m), n = len(nums1), m = len(nums2)
        # Space: O(1)
        count = 0
        for a in nums1:
            for b in nums2:
                if a % (b * k) == 0:
                    count += 1
        return count


