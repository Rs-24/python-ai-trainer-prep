# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/description/

class Solution:
    def numberOfCuts(self, n: int) -> int:
        # Time: O(1)
        # Space: O(1)
        if n == 1:
            return 0
        elif n % 2 == 0:
            return n // 2
        return n


