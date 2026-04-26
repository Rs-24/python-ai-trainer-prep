# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/k-items-with-the-maximum-sum/description/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # Time: O(1)
        # Space: O(1)
        if k <= numOnes + numZeros:
            return min(k, numOnes)
        else:
            return numOnes - (k - numOnes - numZeros)


