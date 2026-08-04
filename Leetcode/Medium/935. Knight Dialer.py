

class Solution:
    def knightDialer(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        d = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        dp = [1] * 10
        for _ in range(n - 1):
            t = [0] * 10
            for x in range(10):
                for y in d[x]:
                    t[y] = (t[y] + dp[x]) % (10 ** 9 + 7)
            dp = t
        return sum(dp) % (10 ** 9 + 7)


        