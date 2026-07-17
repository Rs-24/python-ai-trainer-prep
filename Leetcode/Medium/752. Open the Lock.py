

from collections import deque

class Solution:
    def openLock(self, deadends: list, target: str) -> int:
        # Time: O(1)
        # Space: O(1)
        d = set(deadends)
        if "0000" in d:
            return -1
        q = deque([("0000", 0)])
        s = {"0000"}
        while q:
            x, t = q.popleft()
            if x == target:
                return t
            for i in range(4):
                y = int(x[i])
                for dy in (-1, 1):
                    z = (y + dy) % 10
                    n = x[:i] + str(z) + x[i + 1:]
                    if n not in d and n not in s:
                        s.add(n)
                        q.append((n, t + 1))
        return -1


