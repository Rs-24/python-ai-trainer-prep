# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/make-the-string-great/description/

class Solution:
    def makeGood(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        stack = []
        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


