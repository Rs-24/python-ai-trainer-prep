

class Solution:
    def minAreaRect(self, points: list) -> int:
        # Time: O(n^2)
        # Space: O(n)
        n = len(points)
        s = set(map(tuple, points))
        t = float("inf")
        for i in range(n):
            a, b = points[i]
            for j in range(i + 1, n):
                c, d = points[j]
                if a != c and b != d:
                    if (a, d) in s and (c, b) in s:
                        t = min(t, abs(a - c) * abs(b - d))
        return 0 if t == float("inf") else t


        