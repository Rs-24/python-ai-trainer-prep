

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        # Time: O(n)
        # Space: O(n)
        out = []
        while a > 0 or b > 0:
            if len(out) >= 2 and out[-1] == out[-2]:
                if out[-1] == "a":
                    out.append("b")
                    b -= 1
                else:
                    out.append("a")
                    a -= 1
            else:
                if a >= b and a > 0:
                    out.append("a")
                    a -= 1
                else:
                    out.append("b")
                    b -= 1
        return "".join(out)


        