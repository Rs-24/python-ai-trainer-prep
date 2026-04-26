# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/

class Solution:
    def minLength(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(n)
        stack = []
        for ch in s:
            if stack and ((stack[-1] == "A" and ch == "B") or (stack[-1] == "C" and ch == "D")):
                stack.pop()
                continue
            stack.append(ch)
        return len(stack)


