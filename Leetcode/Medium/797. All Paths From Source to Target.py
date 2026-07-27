

class Solution:
    def allPathsSourceTarget(self, graph: list) -> list:
        # Time: O(n)
        # Space: O(n)
        t = len(graph) - 1
        a = []
        def dfs(n, p):
            if n == t:
                a.append(p[:])
            else:
                for x in graph[n]:
                    p.append(x)
                    dfs(x, p)
                    p.pop()
        dfs(0, [0])
        return a


