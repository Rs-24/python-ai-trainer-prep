# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/remove-outermost-parentheses/description/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space, excluding output: O(1)
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


