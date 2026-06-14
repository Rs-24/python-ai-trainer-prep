

from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        c = Counter(nums)
        b = max(c.values())
        return sum(f for _, f in c.items() if f == b)


