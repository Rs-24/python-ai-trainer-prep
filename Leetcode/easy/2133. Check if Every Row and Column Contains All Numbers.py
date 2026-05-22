

class Solution:
    def checkValid(self, matrix: list[list]) -> bool:
        # Time: O(n^2)
        # Space: O(n)
        n = len(matrix)
        s = set(i for i in range(1, n + 1))
        for r in matrix:
            if set(r) != s:
                return False
        for c in range(n):
            seen = set()
            for r in range(n):
                seen.add(matrix[r][c])
            if seen != s:
                return False
        return True


