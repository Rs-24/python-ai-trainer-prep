# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/nim-game/description/

class Solution:
    def canWinNim(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        return n % 4 != 0

