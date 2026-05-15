

class Solution:
    def generateTheString(self, n: int) -> str:
        # Time: O(n)
        # Space: O(n)
        if n % 2 == 0:
            return "a" * (n - 1) + "b"
        else:
            return "a" * n


