

class Solution:
    def numFactoredBinaryTrees(self, arr: list) -> int:
        # Time: O(n^2)
        # Space: O(n)
        arr.sort()
        dp = {}
        s = set(arr)
        for x in arr:
            t = 1
            for y in arr:
                if y >= x:
                    break
                if x % y == 0:
                    if x // y in s:
                        t = (t + dp[y] * dp[x // y]) % (10**9 + 7)
            dp[x] = t
        return sum(dp.values()) % (10**9 + 7)


