

class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        a = 0
        for x in range(1, n + 1):
            a += (not any(ch in "347" for ch in str(x)) and any(ch in "2569" for ch in str(x)))
        return a


