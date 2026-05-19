

class Solution:
    def thousandSeparator(self, n: int) -> str:
        # Time: O(log n)
        # Space: O(log n)
        if n == 0:
            return "0"
        out = []
        digits = 0
        while n > 0:
            if digits > 0 and digits % 3 == 0:
                out.append(".")
            out.append(str(n % 10))
            n //= 10
            digits += 1
        return "".join(reversed(out))


