

class Solution:
    def findGCD(self, nums: list) -> int:
        # Time: O(n + m), n = len(nums), m = min(nums)
        # Space: O(1)
        l, h = min(nums), max(nums)
        for d in range(min(l, h), 0, -1):
            if l % d == 0 and h % d == 0:
                return d


