

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Time: O(1)
        # Space: O(1)
        flips = 0
        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1
            if bit_c == 0:
                flips += bit_a + bit_b
            else:
                flips += (bit_a == 0 and bit_b == 0)
        return flips


