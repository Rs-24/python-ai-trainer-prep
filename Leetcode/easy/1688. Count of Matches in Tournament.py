# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/count-of-matches-in-tournament/description/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        total = 0
        while n > 1:
            if n % 2 == 0:
                total += n // 2
                n //= 2
            else:
                total += (n - 1) // 2
                n = ((n - 1) // 2) + 1
        return total


