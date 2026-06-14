

class Solution:
    def maximizeExpressionOfThree(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        a = b = float("-inf")
        c = float("inf")
        for n in nums:
            if n >= a:
                b = a
                a = n
            elif n >= b:
                b = n
            elif n <= c:
                c = n
        return a + b - c


