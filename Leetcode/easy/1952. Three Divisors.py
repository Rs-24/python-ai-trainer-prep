# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/three-divisors/description/

class Solution:
    def isThree(self, n: int) -> bool:
        # Time: O(n)
        # Space: O(1)
        found = False
        for x in range(2, n):
            if n % x == 0:
                if not found:
                    found = True
                else:
                    return False
        return found


