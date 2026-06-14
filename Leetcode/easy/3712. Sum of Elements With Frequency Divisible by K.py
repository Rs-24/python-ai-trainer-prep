

from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        c = Counter(nums)
        return sum(n for n in nums if c[n] % k == 0)


