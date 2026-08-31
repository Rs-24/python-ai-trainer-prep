

class Solution:
    def longestStrChain(self, words: list) -> int:
        # Time: O(n * (L^2))
        # Space: O(n)
        words.sort(key=len)
        dp = {}
        a = 1
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                if w[:i] + w[i + 1:] in dp:
                    dp[w] = max(dp[w], dp[w[:i] + w[i + 1:]] + 1)
            a = max(a, dp[w])
        return a


