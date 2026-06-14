

class Solution:
    def minimumFlips(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(log n)
        b = bin(n)[2:]
        c = 0
        i, j = 0, len(b) - 1
        while i < j:
            if b[i] != b[j]:
                c += 1
            i += 1
            j -= 1
        return c


