

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list]) -> bool:
        # Time: O(1)
        # Space: O(1)
        dr, dc, db = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in dr[r] or board[r][c] in dc[c] or board[r][c] in db[(r // 3, c // 3)]:
                    return False
                dr[r].add(board[r][c])
                dc[c].add(board[r][c])
                db[((r // 3, c // 3))].add(board[r][c])
        return True


