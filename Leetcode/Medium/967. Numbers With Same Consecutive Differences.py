

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list:
        # Time: O(n)
        # Space: O(n)
        if n == 1:
            return [x for x in range(10)]
        a = []
        def dfs(x: int, l: int) -> None:
            if l == n:
                a.append(x)
            for d in {x % 10 - k, x % 10 + k}:
                if 0 <= d < 10:
                    dfs(x * 10 + d, l + 1)
        for x in range(1, 10):
            dfs(x, 1)
        return a


        