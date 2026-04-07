# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/water-bottles/description/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Time: O(log n), n = numBottles
        # Space: O(1)
        total = 0
        empty = 0
        while numBottles > 0:
            total += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty %= numExchange
        return total


