

class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        # Time: O(m + n + L), L = len(indices)
        # Space: O(m + n)
        r, c = [0] * m, [0] * n
        for i, j in indices:
            r[i] ^= 1
            c[j] ^= 1
        odd_r, odd_c = sum(r), sum(c)
        return odd_r * (n - odd_c) + odd_c * (m - odd_r)


