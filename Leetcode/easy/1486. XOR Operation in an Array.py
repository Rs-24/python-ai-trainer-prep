

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # Time: O(n)
        # Space: O(1)
        ans = start
        for i in range(1, n):
            ans ^= (start + 2 * i)
        return ans


