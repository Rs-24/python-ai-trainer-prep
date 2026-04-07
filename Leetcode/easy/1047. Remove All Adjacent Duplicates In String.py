# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space, excluding output: O(n)
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


