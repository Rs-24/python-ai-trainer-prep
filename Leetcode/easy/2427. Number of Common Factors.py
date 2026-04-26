# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/number-of-common-factors/description/

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # Time: O(n), n = min(a, b)
        # Space: O(1)
        count = 0
        for x in range(1, min(a, b) + 1):
            if a % x == 0 and b % x == 0:
                count += 1
        return count


