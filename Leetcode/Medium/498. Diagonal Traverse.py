

class Solution:
    def findDiagonalOrder(self, mat: list[list]) -> list:
        # Time: O(m * n)
        # Space: O(m * n)
        if not mat:
            return []
        m, n = len(mat), len(mat[0])
        r, c, d, a = 0, 0, 1, []
        for _ in range(m * n):
            a.append(mat[r][c])
            if d == 1:
                if c == n - 1:
                    r += 1
                    d = -1
                elif r == 0:
                    c += 1
                    d = -1
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                    d = 1
                elif c == 0:
                    r += 1
                    d = 1
                else:
                    r += 1
                    c -= 1
        return a


