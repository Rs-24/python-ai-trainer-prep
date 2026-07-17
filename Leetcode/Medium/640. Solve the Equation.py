

class Solution:
    def solveEquation(self, equation: str) -> str:
        # Time: O(n)
        # Space: O(1)
        def p(expr: str):
            coeff = const = i = 0
            s = 1
            while i < len(expr):
                if expr[i] == "+":
                    s = 1
                    i += 1
                elif expr[i] == "-":
                    s = -1
                    i += 1
                else:
                    t = 0
                    num = False
                    while i < len(expr) and expr[i].isdigit():
                        t = t * 10 + int(expr[i])
                        num = True
                        i += 1
                    if i < len(expr) and expr[i] == "x":
                        coeff += s * (t if num else 1)
                        i += 1
                    else:
                        const += s * t
            return coeff, const
        l, r = equation.split("=")
        l_coeff, l_const = p(l)
        r_coeff, r_const = p(r)
        coeff = l_coeff - r_coeff
        const = r_const - l_const
        if coeff == 0:
            if const == 0:
                return "Infinite solutions"
            return "No solution"
        return "x=" + str(const // coeff)


