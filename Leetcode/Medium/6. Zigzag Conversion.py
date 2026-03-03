# Time to write all of below including tests, explanation and time and aux
# and total space: 17 mins

# Problem: https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        direction = 1
        i = 0
        for ch in s:
            rows[i].append(ch)
            if i == 0:
                direction = 1
            elif i == numRows - 1:
                direction = -1
            i += direction
        return "".join("".join(row) for row in rows)

if __name__ == "__main__":
    sol = Solution()
    assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert sol.convert("PAYPALISHIRING", 1) == "PAYPALISHIRING"
    assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert sol.convert("A", 1) == "A"
    assert sol.convert("hi,There.", 3) == "hh.iTee,r"
    assert sol.convert("hi,There.", 2) == "h,hr.iTee"

# Explanation: the code stores the variable rows, and iterates through s
# while repeatedly going down and up rows and appending to the relevant 
# row
# Time: O(numRows + n), n = len(s)
# Space: excluding output: O(n)


