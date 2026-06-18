

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Time: O(log n)
        # Space: O(log n)
        if numerator == 0:
            return "0"
        out = ["-"] if (numerator < 0) ^ (denominator < 0) else []
        n, d = abs(numerator), abs(denominator)
        out.append(str(n // d))
        r = n % d
        if r == 0:
            return "".join(out)
        out.append(".")
        s = {}
        while r:
            if r in s:
                i = s[r]
                out.insert(i, "(")
                out.append(")")
                break
            s[r] = len(out)
            r *= 10
            out.append(str(r // d))
            r %= d
        return "".join(out)


