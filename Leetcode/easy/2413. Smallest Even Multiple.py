# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/smallest-even-multiple/description/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return n if n % 2 == 0 else 2 * n


