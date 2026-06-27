

class Solution:
    def calculate(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        a = []
        x = 0
        op = "+"
        for i, ch in enumerate(s):
            if ch.isdigit():
                x = x * 10 + int(ch)
            if ch in "+-/*" or i == len(s) - 1:
                if op == "+":
                    a.append(x)
                elif op == "-":
                    a.append(-x)
                elif op == "*":
                    a.append(a.pop() * x)
                else:
                    a.append(int(a.pop() / x))
                op = ch
                x = 0
        return sum(a)


