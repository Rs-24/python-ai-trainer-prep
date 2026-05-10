# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/smallest-number-with-all-set-bits/description/

class Solution:
    def smallestNumber(self, n: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return (1 << n.bit_length()) - 1


