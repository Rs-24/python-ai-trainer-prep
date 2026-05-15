

class Solution:
    def kWeakestRows(self, mat: list[list], k: int) -> list:
        # Time: O(m * n + m log m), m = len(mat), n = len(mat[0])
        # Space: O(m)
        r = []
        for i, row in enumerate(mat):
            r.append((sum(row), i))
        r.sort()
        out = []
        for i in range(k):
            out.append(r[i][1])
        return out


