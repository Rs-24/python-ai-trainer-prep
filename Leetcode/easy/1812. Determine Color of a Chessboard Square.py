# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # Time: O(1)
        # Space: O(1)
        d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
        total = d[coordinates[0]] + int(coordinates[1])
        return total % 2 != 0


