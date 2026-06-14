

from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: list) -> bool:
        # Time: O(n)
        # Space: O(n)
        c = Counter(nums)
        for f in c.values():
            if f > 2:
                return False
        return True


