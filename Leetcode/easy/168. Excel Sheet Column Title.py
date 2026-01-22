# Time to write all of below including tests, explanation and time and aux 
# space: 10 mins

# Problem: https://leetcode.com/problems/excel-sheet-column-title/description/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        while columnNumber > 26:
            out.append("A")
            columnNumber -= 26
        if columnNumber > 0:
            out.append(alphabet[columnNumber-1].upper())
        return "".join(out)

if __name__ == "__main__":
    sol = Solution()
    assert sol.convertToTitle(1) == "A"
    assert sol.convertToTitle(2) == "B"
    assert sol.convertToTitle(26) == "Z"
    assert sol.convertToTitle(27) == "AA"
    assert sol.convertToTitle(29) == "AC"

# Explanation: While columnNumber is > 26, "A" is appended to out, and once
# the loop ends the remaining number's corresponding letter is appended to 
# out. Then out is joined together and returned as a string
# Time: O(n), n = columnNumber
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 10 mins):
#   - I now realise my solution is incorrect. My rewrite is below:
#
# def convertToTitle(self, columnNumber: int) -> str:
#     # Time: O(n), n = number of letters in output
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(n)
#     out = []
#     alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
#     while columnNumber > 0:
#         out.append(alphabet[(columnNumber - 1) % 26])
#         columnNumber = (columnNumber - 1) // 26
#     return "".join(reversed(out))
#
#   - Additionally, my tests could have been improved. My new tests are below: 
#
# if __name__ == "__main__":
#     sol = Solution()
#     assert sol.convertToTitle(1) == "A"
#     assert sol.convertToTitle(2) == "B"
#     assert sol.convertToTitle(25) == "Y"
#     assert sol.convertToTitle(26) == "Z"
#     assert sol.convertToTitle(27) == "AA"
#     assert sol.convertToTitle(28) == "AB"
#     assert sol.convertToTitle(51) == "AY"
#     assert sol.convertToTitle(52) == "AZ"
#     assert sol.convertToTitle(53) == "BA"
#     assert sol.convertToTitle(701) == "ZY"










