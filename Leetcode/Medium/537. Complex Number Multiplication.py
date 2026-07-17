

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Time: O(1)
        # Space: O(1)
        a, b = num1[:-1].split("+")
        a, b = int(a), int(b)
        c, d = num2[:-1].split("+")
        c, d = int(c), int(d)
        return str(a * c - b * d) + "+" + str(a * d + b * c) + "i"


