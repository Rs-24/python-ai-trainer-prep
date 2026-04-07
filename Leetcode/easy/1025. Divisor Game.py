# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/divisor-game/description/

class Solution:
    def divisorGame(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        return n % 2 == 0

# Dynamic programming method:
class Solution:
    def divisorGame(self, n: int) -> bool:
        # Time: O(n^2)
        # Space: O(n)
        dp = [False] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
        return dp[n]


