# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-distinct-numbers-on-board/description/

class Solution:
    def distinctIntegers(self, n: int) -> int:
        # Time: O(1)
        # Space: O(1)
        if n == 1:
            return 1
        return n - 1 


