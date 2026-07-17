

from collections import Counter

class Solution:
    def findPairs(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        if k < 0:
            return 0
        c = Counter(nums)
        a = 0
        if k == 0:
            for t in c.values():
                a += t > 1
        else:
            for x in c.keys():
                a += x + k in c
        return a


