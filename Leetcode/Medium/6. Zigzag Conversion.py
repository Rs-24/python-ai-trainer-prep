# Time to write all of below including tests, explanation and time and aux
# and total space: 1h 9 mins

# Problem: https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        pattern = [[] for _ in range(numRows)]
        i = 0
        row = 0
        down = True
        while i < len(s):
            if down:
                pattern[row].append(s[i])
                if row == numRows - 1:
                    down = False
                    row -= 1
                else:
                    row += 1
            else:
                pattern[row].append(s[i])
                if row == 0:
                    down = True
                    row += 1
                else:
                    row -= 1
            i += 1
        out = []
        for row in pattern:
            for element in row:
                out.append(element)
        return "".join(out)

if __name__ == "__main__":
    sol = Solution()
    assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert sol.convert("PAYPALISHIRING", 1) == "PAYPALISHIRING"
    assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert sol.convert("A", 1) == "A"
    assert sol.convert("hi,There.", 3) == "hh.iTee,r"
    assert sol.convert("hi,There.", 2) == "h,hr.iTee"
    
# Explanation: the program iterates through s using the boolean variable down
# to fill the pattern variable up in the correct way. Then pattern is
# compressed down to a single string variable which is outputted
# Time: O(n), n = len(s)
# Aux space, excluding output and input: O(n)
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 1h 9 mins):
#   - No major learning lessons






