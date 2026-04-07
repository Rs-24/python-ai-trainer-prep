# Time to write all of below including tests, explanation and time and aux
# and total space: 8 mins

# Problem: https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/

from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Time: O(1)
        # Space: O(1)
        board = [[""] * 3 for _ in range(3)]
        x = 1
        for r, c in moves:
            board[r][c] = "X" if x else "O"
            x ^= 1
        for r in range(len(board)):
            if board[r][0] != "" and len(set(board[r])) == 1:
                return "A" if board[r][0] == "X" else "B"
        for c in range(len(board[0])):
            temp = [board[r][c] for r in range(3)]
            if temp[0] != "" and len(set(temp)) == 1:
                return "A" if temp[0] == "X" else "B"
        temp = [board[i][i] for i in range(3)]
        if temp[0] != "" and len(set(temp)) == 1:
            return "A" if temp[0] == "X" else "B"
        temp = [board[2 - i][i] for i in range(3)]
        if temp[0] != "" and len(set(temp)) == 1:
            return "A" if temp[0] == "X" else "B"
        if any(cell == "" for row in board for cell in row):
            return "Pending"
        else:
            return "Draw"
        

