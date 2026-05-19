

class Solution:
    def findRotation(self, mat: list[list], target: list[list]) -> bool:
        # Time: O(m * n), m = len(mat), n = len(mat[0])
        # Space: O(m * n)
        m, n = len(mat), len(mat[0])
        def rotate(x: list[list]) -> list[list]:
            out = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    out[j][n - 1 - i] = x[i][j]
            return out
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        return False


