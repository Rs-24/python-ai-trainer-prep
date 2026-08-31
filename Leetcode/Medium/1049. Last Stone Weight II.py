

class Solution:
    def lastStoneWeightII(self, stones: list) -> int:
        # Time: O(n * sum(stones))
        # Space: O(sum(stones))
        dp = [True] + [False] * (sum(stones) // 2)
        for s in stones:
            for t in range(sum(stones) // 2, s - 1, -1):
                dp[t] = dp[t] or dp[t - s]
        for i in range(sum(stones) // 2, -1, -1):
            if dp[i]:
                return sum(stones) - 2 * i
        return 0


