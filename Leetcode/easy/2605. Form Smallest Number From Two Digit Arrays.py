

class Solution:
    def minNumber(self, nums1: list, nums2: list) -> int:
        # Time: O(n)
        # Space: O(n)
        s = set(nums1) & set(nums2)
        if len(s) > 0:
            return min(s)
        return min(min(nums1), min(nums2)) * 10 + max(min(nums1), min(nums2))


