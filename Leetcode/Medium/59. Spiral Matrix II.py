

class Solution:
    def generateMatrix(self, n: int) -> list[list]:
        # Time: O(n^2)
        # Space: O(n^2)
        out = [[0] * n for _ in range(n)]
        l, r, t, b = 0, n - 1, 0, n - 1
        x = 1
        while x <= n * n:
            for i in range(l, r + 1):
                out[t][i] = x
                x += 1
            t += 1
            for i in range(t, b + 1):
                out[i][r] = x
                x += 1
            r -= 1
            if t <= b:
                for i in range(r, l - 1, -1):
                    out[b][i] = x
                    x += 1
                b -= 1
            if l <= r:
                for i in range(b, t - 1, -1):
                    out[i][l] = x
                    x += 1
                l += 1
        return out


