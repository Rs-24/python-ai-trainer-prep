# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/minimum-moves-to-convert-string/description/

class Solution:
    def minimumMoves(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        moves = 0
        i = 0
        while i < len(s):
            if s[i] == "X":
                moves += 1
                i += 3
            else:
                i += 1
        return moves


