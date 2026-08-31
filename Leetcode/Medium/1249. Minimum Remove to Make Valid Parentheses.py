

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        stack = []
        s = list(s)
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        for i in stack:
            s[i] = ""
        return "".join(s)


