# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/check-if-the-number-is-fascinating/description/

class Solution:
    def isFascinating(self, n: int) -> bool:
        # Time: O(d log d), d = number of digits in n
        # Space: O(d)
        final = str(n) + str(2 * n) + str(3 * n)
        if len(final) != 9:
            return False
        return sorted(final) == list("123456789")
        

