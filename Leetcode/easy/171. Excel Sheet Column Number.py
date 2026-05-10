

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # Time: O(n), n = len(columnTitle)
        # Space: O(1)
        res = 0
        for ch in columnTitle:
            res = res * 26 + ord(ch) - ord("A") + 1
        return res


