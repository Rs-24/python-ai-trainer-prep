

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list:
        # Time: O(1)
        # Space: O(1)
        jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        small = cheeseSlices - jumbo
        if tomatoSlices % 2 or jumbo < 0 or small < 0 or 4 * jumbo + 2 * small != tomatoSlices:
            return []
        return [jumbo, small]


