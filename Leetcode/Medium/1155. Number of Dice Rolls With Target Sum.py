

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # Time: O(n * target * k)
        # Space: O(target)
        dp = [1] + [0] * target
        for _ in range(n):
            nxt = [0] + [0] * target
            for s in range(target + 1):
                for f in range(1, k + 1):
                    if s + f <= target:
                        nxt[s + f] += dp[s]
                        nxt[s + f] %= (10 ** 9 + 7)
            dp = nxt
        return dp[target]


