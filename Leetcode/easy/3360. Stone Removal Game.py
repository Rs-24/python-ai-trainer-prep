# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/stone-removal-game/description/

class Solution:
    def canAliceWin(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        cur_move = 10
        moves = 0
        while n >= cur_move:
            n -= cur_move
            cur_move -= 1
            moves += 1
        return moves % 2 != 0


