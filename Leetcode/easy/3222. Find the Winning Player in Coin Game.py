# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-winning-player-in-coin-game/description/

class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        # Time: O(1)
        # Space: O(1)
        moves = min(x, y // 4)
        return "Bob" if moves % 2 == 0 else "Alice"


