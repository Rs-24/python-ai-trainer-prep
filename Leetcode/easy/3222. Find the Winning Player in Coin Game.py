

class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        # Time: O(1)
        # Space: O(1)
        return "Alice" if min(x, y // 4) % 2 != 0 else "Bob"


