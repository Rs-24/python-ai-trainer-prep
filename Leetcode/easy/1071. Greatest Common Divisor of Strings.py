# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Time: O(n + m), n = len(str1), m = len(str2)
        # Space: O(n + m)
        if str1 + str2 != str2 + str1:
            return ""
        length = gcd(len(str1), len(str2))
        return str1[:length]


