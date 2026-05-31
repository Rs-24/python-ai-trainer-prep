
from math import gcd

class Solution:
    def countBeautifulPairs(self, nums: list) -> int:
        # Time: O(n^2)
        # Space: O(1)
        def first(x: int) -> int:
            while x >= 10:
                x //= 10
            return x
        c = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if gcd(first(nums[i]), nums[j] % 10) == 1:
                    c += 1
        return c


