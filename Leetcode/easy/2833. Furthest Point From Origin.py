# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/furthest-point-from-origin/description/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # Time: O(n), n = len(moves)
        # Space: O(1)
        return abs(moves.count("L") - moves.count("R")) + moves.count("_")


