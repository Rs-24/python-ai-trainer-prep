

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Time: O(log columnNumber)
        # Space: O(log columnNumber)
        out = []
        while columnNumber > 0:
            columnNumber -= 1
            out.append(chr(columnNumber % 26 + ord("A")))
            columnNumber //= 26
        return "".join(reversed(out))


