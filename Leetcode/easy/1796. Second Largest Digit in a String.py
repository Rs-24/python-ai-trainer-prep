# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/second-largest-digit-in-a-string/description/

class Solution:
    def secondHighest(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        digits = set()
        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))
        if len(digits) < 2:
            return -1
        digits.remove(max(digits))
        return max(digits)


