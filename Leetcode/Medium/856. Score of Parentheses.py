

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        t = [0]
        for ch in s:
            if ch == "(":
                t.append(0)
            else:
                x = t.pop()
                t[-1] += max(2 * x, 1)
        return t[0]


        