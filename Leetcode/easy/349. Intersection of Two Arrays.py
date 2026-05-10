

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Time: O(m + n), m = len(nums1), n = len(nums2)
        # Space: O(m + n)
        return list(set(nums1) & set(nums2))


