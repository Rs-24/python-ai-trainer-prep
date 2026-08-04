

class Solution:
    def mincostTickets(self, days: list, costs: list) -> int:
        # Time: O(n^2)
        # Space: O(n)
        n = len(days)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            a = dp[i - 1] + costs[0]
            j = i - 1
            while j >= 0 and days[j] >= days[i - 1] - 6:
                j -= 1
            b = dp[j + 1] + costs[1]
            j = i - 1
            while j >= 0 and days[j] >= days[i - 1] - 29:
                j -= 1
            c = dp[j + 1] + costs[2]
            dp[i] = min(a, b, c)
        return dp[n]


