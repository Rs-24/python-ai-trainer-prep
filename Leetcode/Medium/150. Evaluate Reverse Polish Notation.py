

class Solution:
    def evalRPN(self, tokens: list) -> int:
        # Time: O(n)
        # Space: O(n)
        s = []
        for t in tokens:
            if t in "+-*/":
                b = s.pop()
                a = s.pop()
                if t == "+":
                    s.append(a + b)
                elif t == "-":
                    s.append(a - b)
                elif t == "*":
                    s.append(a * b)
                elif t == "/":
                    s.append(int(a / b))
            else:
                s.append(int(t))
        return s[-1]


