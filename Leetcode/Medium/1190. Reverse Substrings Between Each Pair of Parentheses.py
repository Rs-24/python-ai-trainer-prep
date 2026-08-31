

class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Time: O(n^2)
        # Space: O(n)
        stack = []
        for ch in s:
            if ch == ")":
                t = []
                while stack[-1] != "(":
                    t.append(stack.pop())
                stack.pop()
                stack.extend(t)
            else:
                stack.append(ch)
        return "".join(stack)


