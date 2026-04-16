# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/sum-of-digits-in-base-k/description/

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        total = 0
        while n > 0:
            total += n % k
            n //= k
        return total


