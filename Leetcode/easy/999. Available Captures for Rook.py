# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/available-captures-for-rook/description/

from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Time: O(m * n), m = len(board), n = len(board[0])
        # Space: O(1)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "R":
                    total = 0
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for dr, dc in directions:
                        temp_r = r + dr
                        temp_c = c + dc
                        while 0 <= temp_r < len(board) and 0 <= temp_c < len(board[0]):
                            if board[temp_r][temp_c] in "Bp":
                                total += 1 if board[temp_r][temp_c] == "p" else 0
                                break
                            temp_r += dr
                            temp_c += dc
                    return total


