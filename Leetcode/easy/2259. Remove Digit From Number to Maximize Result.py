

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # Time: O(n^2)
        # Space: O(n)
        best = ""
        for i, d in enumerate(number):
            if d == digit:
                best = max(best, number[:i] + number[i + 1:])
        return best


