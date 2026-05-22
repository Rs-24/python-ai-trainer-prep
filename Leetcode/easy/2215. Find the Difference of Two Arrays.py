

class Solution:
    def findDifference(self, nums1: list, nums2: list) -> list[list]:
        # Time: O(n)
        # Space: O(n)
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1 - s2), list(s2 - s1)]


