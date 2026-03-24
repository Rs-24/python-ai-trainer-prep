# Time to write all of below including tests, explanation and time and aux
# and total space: 8 mins

# Problem: https://leetcode.com/problems/find-the-difference/description/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Time: O(n + m), n = len(s), m = len(t)
        # Space: O(1)
        x = 0
        for ch in s:
            x ^= ord(ch)
        for ch in t:
            x ^= ord(ch)
        return chr(x)

# Counter method:
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Time: O(n + m), n = len(s), m = len(t)
        # Space: O(1)
        c_s = Counter(s)
        c_t = Counter(t)
        for ch in t:
            if c_t[ch] != c_s[ch]:
                return ch

# Simplified XOR method: 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Time: O(n + m), n = len(s), m = len(t)
        # Space: O(1) 
        x = 0
        for ch in s + t:
            x ^= ord(ch)
        return chr(x)


