

from collections import Counter

class Solution:
    def checkPrimeFrequency(self, nums: list) -> bool:
        # Time: O(n^2)
        # Space: O(n)
        c = Counter(nums)
        for f in c.values():
            v = True
            if f < 2:
                v = False
            for d in range(2, int(f ** 0.5) + 1):
                if f % d == 0:
                    v = False
            if v:
                return True
        return False


