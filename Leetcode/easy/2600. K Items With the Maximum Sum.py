

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # Time: O(1)
        # Space: O(1)
        if k <= numOnes + numZeros:
            return min(k, numOnes)
        return numOnes - (k - numZeros - numOnes)


