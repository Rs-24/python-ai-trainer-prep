

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: list) -> list:
        # Time: O(n)
        # Space: O(n)
        ans = [[0] * len(colsum) for _ in range(2)]
        for i, c in enumerate(colsum):
            if c == 2:
                ans[0][i] = 1
                ans[1][i] = 1
                upper -= 1
                lower -= 1
            elif c == 1:
                if upper > lower:
                    ans[0][i] = 1
                    upper -= 1
                else:
                    ans[1][i] = 1
                    lower -= 1
        if upper != 0 or lower != 0:
            return []
        return ans


