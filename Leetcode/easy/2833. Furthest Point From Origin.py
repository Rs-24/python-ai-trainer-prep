

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # Time: O(n)
        # Space: O(1)
        return abs(moves.count("L") - moves.count("R")) + moves.count("_")


