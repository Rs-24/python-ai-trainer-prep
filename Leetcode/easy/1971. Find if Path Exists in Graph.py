

from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: list[list], source: int, destination: int) -> bool:
        # Time: O(L + L * n), L = len(edges)
        # Space: O(L + L * n)
        neighbours = defaultdict(list)
        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)
        seen = {source}
        q = deque([source])
        while q:
            node = q.popleft()
            if node == destination:
                return True
            for n in neighbours[node]:
                if n not in seen:
                    seen.add(n)
                    q.append(n)
        return False


