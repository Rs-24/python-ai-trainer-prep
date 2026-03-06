# Time to write all of below including tests, explanation and time and aux
# and total space: 10 mins

# Problem: https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(26) = O(1)
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1
        return all(c == 0  for c in count)

# Dictionary method:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(n + m), n = len(s), m = len(t)
        # Space: O(n)
        if len(s) != len(t):
            return False    
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        for ch in t:
            if ch not in d:
                return False
            d[ch] -= 1
            if d[ch] < 0:
                return False
        return True

# One-liner solution
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(n + m), n = len(s), m = len(t)
        # Space: O(n + m)
        return Counter(s) == Counter(t)


