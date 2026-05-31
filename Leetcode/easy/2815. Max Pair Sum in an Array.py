

from collections import defaultdict

class Solution:
    def maxSum(self, nums: list) -> int:
        # Time: O(n log x)
        # Space: O(n)
        def max_digit(x: int) -> int:
            b = 0
            while x > 0:
                b = max(b, x % 10)
                x //= 10
            return b
        d = defaultdict(lambda: [-1, -1])
        for num in nums:
            a, b = d[max_digit(num)]
            if num > a:
                d[max_digit(num)] = [num, a]
            elif num > b:
                d[max_digit(num)][1] = num
        best = -1
        for a, b in d.values():
            best = max(best, a + b)
        return best


