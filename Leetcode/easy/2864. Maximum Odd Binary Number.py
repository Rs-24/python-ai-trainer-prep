

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Time: O(log n)
        # Space: O(1)
        n = s.count("1")
        return "1" * (n - 1) + "0" * (len(s) - n) + "1"


