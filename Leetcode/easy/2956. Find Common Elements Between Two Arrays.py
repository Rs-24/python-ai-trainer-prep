

class Solution:
    def findIntersectionValues(self, nums1: list, nums2: list) -> list:
        # Time: O(n)
        # Space: O(n)
        x, y = set(nums1), set(nums2)
        return [sum(1 for n in nums1 if n in y), sum(1 for n in nums2 if n in x)]


