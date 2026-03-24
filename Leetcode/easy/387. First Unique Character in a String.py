# Time to write all of below including tests, explanation and time and aux
# and total space: 8 mins

# Problem: https://leetcode.com/problems/first-unique-character-in-a-string/description/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        for i, ch in enumerate(s):
            if d[ch] == 1:
                return i        
        return -1

# Counter method:
from collections import Counter 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        c = Counter(s)
        for i, ch in enumerate(s):
            if c[ch] == 1:
                return i        
        return -1


