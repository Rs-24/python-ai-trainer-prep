# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/

from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        # Time: O(n), n = len(num)
        # Space: O(1)
        c = Counter(num)
        for i, digit in enumerate(num):
            if c[str(i)] != int(digit):
                return False
        return True


