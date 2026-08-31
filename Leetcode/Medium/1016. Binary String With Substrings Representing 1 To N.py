

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # Time: O(n log n)
        # Space: O(log n)
        for x in range(1, n + 1):
            if bin(x)[2:] not in s:
                return False
        return True


