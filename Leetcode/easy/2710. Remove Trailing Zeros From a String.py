

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # Time: O(n)
        # Space: O(n)
        for i in range(len(num) - 1, -1, -1):
            if num[i] != "0":
                return num[:i + 1]
        return ""


