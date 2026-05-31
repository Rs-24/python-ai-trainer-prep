

from collections import Counter

class Solution:
    def unequalTriplets(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        c = Counter(nums)
        l = 0
        n = len(nums)
        ans = 0
        for f in c.values():
            r = n - l - f
            ans += l * f * r
            l += f
        return ans


