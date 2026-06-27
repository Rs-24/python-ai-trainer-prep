

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        c = 0
        while left != right:
            left >>= 1
            right >>= 1
            c += 1
        return left << c


