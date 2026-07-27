

from collections import Counter

class Solution:
    def largestOverlap(self, img1: list, img2: list) -> int:
        # Time: O(n^2)
        # Space: O(n^2)
        a, b = [], []
        n = len(img1)
        for r in range(n):
            for c in range(n):
                if img1[r][c]:
                    a.append((r, c))
                if img2[r][c]:
                    b.append((r, c))
        c = Counter()
        for x, y in a:
            for i, j in b:
                c[(i - x, j - y)] += 1
        return max(c.values(), default=0)


        