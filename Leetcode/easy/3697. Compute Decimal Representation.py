

class Solution:
    def decimalRepresentation(self, n: int) -> list:
        # Time: O(log n)
        # Space: O(log n)
        out = []
        p = 0
        while n > 0:
            if n % 10 != 0:
                out.append((n % 10) * (10 ** p))
            n //= 10
            p += 1
        return list(reversed(out))


