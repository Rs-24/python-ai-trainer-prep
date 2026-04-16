# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        seen_zero_after_segment = False
        for ch in s:
            if ch == "0":
                seen_zero_after_segment = True
            elif seen_zero_after_segment:
                return False
        return True


