# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/description/

class Solution:
    def minimumChairs(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        highest = 0
        cur = 0
        for ch in s:
            cur += 1 if ch == "E" else -1
            highest = max(highest, cur)
        return highest


