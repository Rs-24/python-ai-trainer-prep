# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-odd-binary-number/description/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        ones = s.count("1")
        return "1" * (ones - 1) + "0" * (len(s) - ones) + "1"


