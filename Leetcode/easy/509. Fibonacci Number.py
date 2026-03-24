# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/fibonacci-number/description/

class Solution:
    def fib(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        if n <= 1:
            return n
        prev_prev = 0
        prev = 1
        for _ in range(2, n + 1):
            cur = prev_prev + prev
            prev_prev = prev
            prev = cur
        return prev

# Recursion with dynamic programming method:
class Solution:
    def fib(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        dp = {0: 0, 1: 1}
        def recurse(x: int) -> int:
            if x not in dp:
                dp[x] = recurse(x - 1) + recurse(x - 2)
            return dp[x]
        return recurse(n)


