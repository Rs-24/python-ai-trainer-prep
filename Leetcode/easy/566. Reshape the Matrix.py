

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        # Time: O(r * c + m * n), m = len(mat), n = len(mat[0])
        # Space: O(r * c)
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        out = [[""] * c for _ in range(r)]
        for i in range(m):
            for j in range(n):
                d = (i * n + j)
                new_i, new_j = divmod(d, c)
                out[new_i][new_j] = mat[i][j]
        return out


