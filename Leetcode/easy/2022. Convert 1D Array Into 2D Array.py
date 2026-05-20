

class Solution:
    def construct2DArray(self, original: list, m: int, n: int) -> list[list]:
        # Time: O(m * n)
        # Space: O(m * n)
        if m * n != len(original):
            return []
        out = [[0] * n for _ in range(m)]
        for i, num in enumerate(original):
            out[i // n][i % n] = num
        return out


