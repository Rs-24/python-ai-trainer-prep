# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/find-if-path-exists-in-graph/description/

from typing import List
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Time: O(n + k), k = len(edges)
        # Space: O(n + k)
        neighbours = defaultdict(list)
        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)
        seen = set()
        q = deque([source])
        while q:
            cur = q.popleft()
            if cur == destination:
                return True
            seen.add(cur)
            for n in neighbours[cur]:
                if n not in seen:
                    q.append(n)
        return False


