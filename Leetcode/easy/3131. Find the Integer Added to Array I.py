

class Solution:
    def addedInteger(self, nums1: list, nums2: list) -> int:
        # Time: O(n)
        # Space: O(1)
        return min(nums2) - min(nums1)


