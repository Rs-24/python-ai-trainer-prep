

class Solution:
    def findCircleNum(self, isConnected: list[list]) -> int:
        # Time: O(n)
        # Space: O(n)
        n = len(isConnected)
        s = set()
        def dfs(t: int):
            s.add(t)
            for p in range(n):
                if isConnected[t][p] and p not in s:
                    dfs(p)
        a = 0
        for p in range(n):
            if p not in s:
                a += 1
                dfs(p)
        return a


