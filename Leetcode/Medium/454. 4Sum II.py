

from collections import Counter

class Solution:
    def fourSumCount(self, nums1: list, nums2: list, nums3: list, nums4: list) -> int:
        # Time: O(n^2)
        # Space: O(n)
        c = Counter()
        for a in nums1:
            for b in nums2:
                c[a + b] += 1
        t = 0
        for a in nums3:
            for b in nums4:
                t += c[-(a + b)]
        return t


