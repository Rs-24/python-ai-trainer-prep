

class Solution:
    def spiralOrder(self, matrix: list[list]) -> list:
        # Time: O(n^2)
        # Space: O(n^2)
        out = []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while l <= r and t <= b:
            for i in range(l, r + 1):
                out.append(matrix[t][i])
            t += 1
            for i in range(t, b + 1):
                out.append(matrix[i][r])
            r -= 1
            if t <= b:
                for i in range(r, l - 1, -1):
                    out.append(matrix[b][i])
                b -= 1
            if l <= r:
                for i in range(b, t - 1, -1):
                    out.append(matrix[i][l])
                l += 1
        return out


