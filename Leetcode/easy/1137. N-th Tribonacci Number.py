# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c

# Dynamic programming version:
class Solution:
    def tribonacci(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        dp = {0: 0, 1: 1, 2: 1}
        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]
            dp[i] = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
            return dp[i]
        return dfs(n)


