

class Solution:
    def exist(self, board: list[list], word: str) -> bool:
        # Time: 0(m * n * m * n)
        # Space: O(m * n)
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if board[r][c] != word[0]:
                    continue
                s = [(r, c, 0, {(r, c)})]
                while s:
                    x, y, i, v = s.pop()
                    if i == len(word) - 1:
                        return True
                    for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if 0 <= x + a < m and 0 <= y + b < n and (x + a, y + b) not in v and board[x + a][y + b] == word[i + 1]:
                            s.append((x + a, y + b, i + 1, v | {(x + a, y + b)}))
        return False


