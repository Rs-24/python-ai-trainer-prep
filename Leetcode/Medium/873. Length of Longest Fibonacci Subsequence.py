

class Solution:
    def lenLongestFibSubseq(self, arr: list) -> int:
        # Time: O(n^2)
        # Space: O(n^2)
        n = len(arr)
        d = {x: i for i, x in enumerate(arr)}
        dp = [[2] * n for _ in range(n)]
        a = 0
        for k in range(n):
            for j in range(k):
                t = arr[k] - arr[j]
                if t < arr[j] and t in d:
                    dp[j][k] = dp[d[t]][j] + 1
                    a = max(a, dp[j][k])
        return a if a >= 3 else 0 


