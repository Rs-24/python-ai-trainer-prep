

class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        # Time: O(n), n = len(position)
        # Space: O(1)
        even = odd = 0
        for p in position:
            if p % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)


