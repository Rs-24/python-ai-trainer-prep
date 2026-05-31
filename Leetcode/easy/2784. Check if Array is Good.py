
from collections import Counter

class Solution:
    def isGood(self, nums: list) -> bool:
        # Time: O(n^2)
        # Space: O(n)
        c  = Counter(nums)
        for x in range(1, len(nums)):
            if x not in nums:
                return False
            if x < len(nums) - 1 and c[x] != 1:
                return False
            if x == len(nums) - 1 and c[x] != 2:
                return False
        return True


