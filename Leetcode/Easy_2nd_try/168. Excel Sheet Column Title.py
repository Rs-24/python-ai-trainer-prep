# Time to write all of below including tests, explanation and time and aux 
# space: 39 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/excel-sheet-column-title/description/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = []
        while columnNumber > 0:
            columnNumber -= 1
            out.append(chr(ord("A") + (columnNumber % 26)))
            columnNumber //= 26
        return "".join(reversed(out))

if __name__ == "__main__":
    sol = Solution()
    assert sol.convertToTitle(1) == "A"
    assert sol.convertToTitle(2) == "B"
    assert sol.convertToTitle(25) == "Y"
    assert sol.convertToTitle(26) == "Z"
    assert sol.convertToTitle(27) == "AA"
    assert sol.convertToTitle(28) == "AB"
    assert sol.convertToTitle(52) == "AZ"
    assert sol.convertToTitle(53) == "BA"

# Explanation: the code repeatedly decrements columnNumber by 1 and appends to
# out the corresponding letter equivalent to the remainder of columnNumber
# after dividing by 26. It then uses the // operator on columnNumber by 26.
# Then once the loop ends it reverses out and returns it as a string
# Time: O(log_26 n), n = columnNumber
# Space: excluding output: O(1)

# Learning lessons (done after completing all of above in 39 mins):
#   - No major learning lessons



