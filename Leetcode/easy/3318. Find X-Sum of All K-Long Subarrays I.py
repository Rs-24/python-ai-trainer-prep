

from collections import Counter

class Solution:
    def findXSum(self, nums: list, k: int, x: int) -> list:
        # Time: O(n^2 log n)
        # Space: O(n)
        def x_sum(a: list) -> int:
            c = sorted(list(Counter(a).items()), key=lambda t: (-t[1], -t[0]))
            return sum(c[i][0] * c[i][1] for i in range(min(x, len(c))))
        return [x_sum(nums[i:i + k]) for i in range(len(nums) - k + 1)]


