

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Time: O(m + n), m = len(s), n = len(goal)
        # Space: O(m)
        if len(s) != len(goal):
            return False
        return goal in (s + s)


