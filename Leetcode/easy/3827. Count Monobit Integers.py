# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-monobit-integers/description/

class Solution:
    def countMonobit(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        count = 1
        x = 1
        while x <= n:
            count += 1
            x = (x << 1) | 1
        return count


