

class Solution:
    def isValid(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(n)
        stack = []
        d = {"(": ")", "{": "}", "[": "]"}
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if stack and d[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        return not stack


