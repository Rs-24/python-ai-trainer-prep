

class Solution:
    def minElement(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        b = float("inf")
        for n in nums:
            t = 0
            while n > 0:
                t += n % 10
                n //= 10
            b = min(b, t)
        return b


