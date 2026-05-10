# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/description/

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # Time: O(1)
        # Space: O(1)
        def get_pos(s: str) -> str:
            pos = (ord(s[0]) - ord("a") + 1) + int(s[1])
            return "Black" if pos % 2 == 0 else "White"
        return get_pos(coordinate1) == get_pos(coordinate2)


