

class Solution:
    def eventualSafeNodes(self, graph: list) -> list:
        # Time: O(n^2)
        # Space: O(n)
        n = len(graph)
        t = [0] * n
        def dfs(i):
            if t[i] == 1 or t[i] == 3:
                return False
            if t[i] == 2:
                return True
            t[i] = 1
            for j in graph[i]:
                if not dfs(j):
                    t[i] = 3
                    return False
            t[i] = 2
            return True
        return [i for i in range(n) if dfs(i)]


