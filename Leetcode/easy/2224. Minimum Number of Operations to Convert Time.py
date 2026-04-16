# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/description/

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # Time: O(1)
        # Space: O(1)
        def to_mins(s: str) -> int:
            return int(s[:2]) * 60 + int(s[3:])      
        m1, m2 = to_mins(current), to_mins(correct)
        diff = m2 - m1
        total = 0
        options = [60, 15, 5, 1]
        for dt in options:
            total += diff // dt
            diff %= dt
        return total


