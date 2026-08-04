

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list:
        # Time: O(rows * cols)
        # Space: O(1)
        a = []
        if 0 <= rStart < rows and 0 <= cStart < cols:
            a.append([rStart, cStart])
        t = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 1
        while len(a) < rows * cols:
            for i in range(4):
                for _ in range(d):
                    rStart += t[i][0]
                    cStart += t[i][1]
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        a.append([rStart, cStart])
                if i % 2 == 1:
                    d += 1
        return a


        