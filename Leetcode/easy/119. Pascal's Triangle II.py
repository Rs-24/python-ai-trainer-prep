

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # Time: O(rowIndex^2)
        # Space: O(rowIndex)
        if rowIndex < 2:
            return [1] * (rowIndex + 1)
        out = [1, 1]
        for r in range(2, rowIndex + 1):
            temp = []
            for i in range(len(out) - 1):
                temp.append(out[i] + out[i + 1])
            out = [1] + temp + [1]
        return out


