

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list]:
        # Time: O(n * k)
        # Space: O(n * k)
        out = []
        s = [(1, [], n)]
        while s:
            x, p, r = s.pop()
            if len(p) == k and r == 0:
                out.append(p)
                continue
            if len(p) >= k or r < 0:
                continue
            for d in range(x, 10):
                if d > r:
                    break
                s.append((d + 1, p + [d], r - d))
        return out


