

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # Time: O(1)
        # Space: O(1)
        return (ord(coordinate1[0]) - ord("a") + 1 + int(coordinate1[1])) % 2 == (ord(coordinate2[0]) - ord("a") + 1 + int(coordinate2[1])) % 2


