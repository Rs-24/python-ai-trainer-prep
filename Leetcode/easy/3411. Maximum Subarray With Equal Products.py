

from math import gcd, lcm

class Solution:
    def maxLength(self, nums: list) -> int:
        # Time: O(n^2)
        # Space: O(1)
        b = 0
        for i in range(len(nums)):
            p = 1
            g = 1
            l = nums[i]
            for j in range(i, len(nums)):
                p *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                if p == l * g:
                    b = max(b, j - i + 1)
        return b


