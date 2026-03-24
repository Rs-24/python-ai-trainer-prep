# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/rotate-string/description/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(n)
        if len(s) != len(goal):
            return False
        return goal in (s + s)


