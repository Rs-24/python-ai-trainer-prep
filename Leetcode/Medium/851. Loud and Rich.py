

from collections import defaultdict

class Solution:
    def loudAndRich(self, richer: list, quiet: list) -> list:
        # Time: O(n)
        # Space: O(n)
        n = len(quiet)
        d = defaultdict(list)
        for a, b in richer:
            d[b].append(a)
        a = [-1] * n
        def dfs(p):
            if a[p] != -1:
                return a[p]
            a[p] = p
            for x in d[p]:
                y = dfs(x)
                if quiet[y] < quiet[a[p]]:
                    a[p] = y
            return a[p]
        for i in range(n):
            dfs(i)
        return a


        