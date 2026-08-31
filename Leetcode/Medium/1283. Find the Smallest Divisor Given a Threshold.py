

class Solution:
    def smallestDivisor(self, nums: list, threshold: int) -> int:
        # Time: O(n log max(nums))
        # Space: O(1)
        l, r = 1, max(nums)
        while l < r:
            m = (l + r) // 2
            t = 0
            for num in nums:
                t += (num + m - 1) // m
            if t <= threshold:
                r = m
            else:
                l = m + 1
        return l


