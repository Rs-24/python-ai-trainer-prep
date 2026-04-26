# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/sum-multiples/description/

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        total = 0
        for x in range(1, n + 1):
            if x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
                total += x
        return total


