

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        if n == 0:
            return 1
        ans = 0
        while n > 0:
            ans = (ans << 1) | ((n & 1) ^ 1)
            n >>= 1
        return ans


