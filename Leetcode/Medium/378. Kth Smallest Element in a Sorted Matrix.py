

class Solution:
    def kthSmallest(self, matrix: list[list], k: int) -> int:
        # Time: O(n log n)
        # Space O(1)
        n = len(matrix)
        def c(x: int) -> int:
            r, c = n - 1, 0
            a = 0
            while r >= 0 and c < n:
                if matrix[r][c] <= x:
                    a += r + 1
                    c += 1
                else:
                    r -= 1
            return a
        l, r = matrix[0][0], matrix[n - 1][n - 1]
        while l < r:
            m = (l + r) // 2
            if c(m) < k:
                l = m + 1
            else:
                r = m
        return l


