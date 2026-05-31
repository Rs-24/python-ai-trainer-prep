

class Solution:
    def isFascinating(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        n = n * 10**6 + (2 * n) * 10**3 + 3 * n
        for i in range(9):
            if str(i + 1) not in str(n):
                return False
        return True


