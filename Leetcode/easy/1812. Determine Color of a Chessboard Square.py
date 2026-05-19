

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # Time: O(1)
        # Space: O(1)
        t = ord(coordinates[0]) - ord("a") + 1 + int(coordinates[1])
        return t % 2 != 0


