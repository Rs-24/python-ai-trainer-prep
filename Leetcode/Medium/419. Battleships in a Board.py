

class Solution:
    def countBattleships(self, board: list[list]) -> int:
        # Time: O(m * n)
        # Space: O(1)
        if not board:
            return 0
        m, n = len(board), len(board[0])
        s = 0
        for r in range(m):
            for c in range(n):
                s += not (board[r][c] == "." or (r > 0 and board[r - 1][c] == "X") or (c > 0 and board[r][c - 1] == "X"))
        return s


