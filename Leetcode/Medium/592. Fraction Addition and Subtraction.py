

from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Time: O(n)
        # Space: O(1)
        n, d, i = 0, 1, 0
        while i < len(expression):
            t = 1
            if expression[i] in "+-":
                t = -1 if expression[i] == "-" else t
                i += 1
            a = 0
            while i < len(expression) and expression[i].isdigit():
                a = a * 10 + int(expression[i])
                i += 1
            i += 1
            b = 0
            while i < len(expression) and expression[i].isdigit():
                b = b * 10 + int(expression[i])
                i += 1
            a *= t
            n = n * b + a * d
            d *= b
            t = gcd(abs(n), d)
            n //= t
            d //= t
        return str(n) + "/" + str(d)


