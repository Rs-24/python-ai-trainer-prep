# Time to write all of below including tests, explanation and time and aux
# and total space: 21 mins

# Problem: https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if s == "":
            return True
        s_to_t = {}
        t_to_s = {}
        for s1, t1 in zip(s, t):
            if s1 in s_to_t and s_to_t[s1] != t1:
                    return False
            if t1 in t_to_s and t_to_s[t1] != s1:
                    return False
            s_to_t[s1] = t1
            t_to_s[t1] = s1
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.isIsomorphic("1", "2") == True
    assert sol.isIsomorphic("1", "1") == True
    assert sol.isIsomorphic("f1", "f2") == True
    assert sol.isIsomorphic("ff1", "fg2") == False
    assert sol.isIsomorphic("ff1", "gg3") == True

# Explanation: the code uses two dictionaries to map the characters to each
# other, and if any of the characters do not correspond, then False is
# returned
# Time: O(k), k = number of characters processed, worst case O(n),
# n = len(s) = len(t)
# Space: O(k), worst case O(n)

# Last seen index method:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Time: O(k), k = number of characters processed, worst case O(n),
        # n = len(s) = len(t)
        # Space: O(k), worst case O(n)
        last_s = {}
        last_t = {}
        for i, (a, b) in enumerate(zip(s, t)):           
            if last_s.get(a, -1) != last_t.get(b, -1):
                return False            
            last_s[a] = i
            last_t[b] = i
        return True

# Normalisation method:
from typing import List
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Time: O(n), n = len(s) = len(t)
        # Space: O(n)
        def encode(s: str) -> List[int]:
            d = {}
            out = []
            count = 0
            for ch in s:
                if ch in d:
                    out.append(d[ch])
                else:
                    d[ch] = count
                    out.append(count)
                    count += 1
            return out
        return encode(s) == encode(t)

# set equality method
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Time: O(n), n = len(s) = len(t)
        # Space, excluding output: worst case O(n) 
        combined = len(set(zip(s, t)))
        s_s = len(set(s))
        t_s = len(set(t))
        return combined == s_s == t_s


