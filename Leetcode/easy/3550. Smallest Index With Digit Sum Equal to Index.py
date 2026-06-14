

class Solution:
    def smallestIndex(self, nums: list) -> int:
        # Time: O(n log n)
        # Space: O(1)
        for i, n in enumerate(nums):
            t = 0
            while n > 0:
                t += n % 10
                n //= 10
            if t == i:
                return i
        return -1


