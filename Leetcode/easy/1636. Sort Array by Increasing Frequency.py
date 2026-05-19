

from collections import Counter

class Solution:
    def frequencySort(self, nums: list) -> list:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        c = Counter(nums)
        nums.sort(key=lambda x: (c[x], -x))
        return nums


