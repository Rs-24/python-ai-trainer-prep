# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/binary-gap/description/

class Solution:
    def binaryGap(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        best = 0
        current = None
        while n > 0:
            if n & 1 == 1:
                if current is not None:
                    best = max(best, current)
                current = 1
            else:
                if current is not None:
                    current += 1
            n >>= 1
        return best


