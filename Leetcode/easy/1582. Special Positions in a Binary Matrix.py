

class Solution:
    def numSpecial(self, mat: list[list]) -> int:
        # Time: O(m * n), m = len(mat), n = len(mat[0])
        # Space: O(m + n)
        m, n = len(mat), len(mat[0])
        s_r = [0] * m
        s_c = [0] * n
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    s_r[r] += 1
                    s_c[c] += 1
        count = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    if s_r[r] == s_c[c] == 1:
                        count += 1
        return count


