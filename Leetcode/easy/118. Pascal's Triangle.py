

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Time: O(numRows^2)
        # Space: O(numRows^2)
        if numRows <= 2:
            return [[1] * i for i in range(1, numRows + 1)]
        out = [[1], [1, 1]]
        for r in range(3, numRows + 1):
            prev = out[-1]
            cur = []
            for i in range(len(prev) - 1):
                cur.append(prev[i] + prev[i + 1])
            cur = [1] + cur + [1]
            out.append(cur)
        return out


