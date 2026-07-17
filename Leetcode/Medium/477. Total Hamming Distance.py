

class Solution:
    def totalHammingDistance(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        n = len(nums)
        a = 0
        for b in range(32):
            t = 0
            for x in nums:
                t += (x >> b) & 1
            a += t * (n - t)
        return a


