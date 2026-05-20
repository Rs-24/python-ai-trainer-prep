

from collections import Counter

class Solution:
    def twoOutOfThree(self, nums1: list, nums2: list, nums3: list) -> list:
        # Time: O(m + n + k), m = len(nums1), n = len(nums2), k = len(nums3)
        # Space: O(m + n + k)
        c = Counter(set(nums1))
        c.update(set(nums2))
        c.update(set(nums3))
        return [num for num, freq in c.items() if freq >= 2]


