

class Solution:
    def combine(self, n: int, k: int) -> list[list]:
        # Time: O(n^2)
        # Space: O(n^2)
        out = []
        s = [(1, [])]
        while s:
            i, p = s.pop()
            if len(p) == k:
                out.append(p)
                continue
            for x in range(i, n + 1):
                s.append((x + 1, p + [x]))
        return out


