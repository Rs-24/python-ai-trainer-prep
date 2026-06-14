

class Solution:
    def numberOfPairs(self, nums1: list, nums2: list, k: int) -> int:
        # Time: O(n^2)
        # Space: O(1)
        return sum(1 for a in nums1 for b in nums2 if a % (b * k) == 0)


