

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Time: O(log numBottles)
        # Space: O(1)
        count = 0
        empty = 0
        full = numBottles
        while full > 0:
            count += full
            empty += full
            full = empty // numExchange
            empty %= numExchange
        return count


