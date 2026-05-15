

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        out = []
        depth = 0
        for ch in s:
            if ch == "(":
                depth += 1
                if depth > 1:
                    out.append(ch)
            else:
                depth -= 1
                if depth > 0:
                    out.append(ch)
        return "".join(out)


