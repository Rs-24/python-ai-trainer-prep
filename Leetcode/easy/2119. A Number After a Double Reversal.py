# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/a-number-after-a-double-reversal/description/

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        return num == 0 or num % 10 != 0


