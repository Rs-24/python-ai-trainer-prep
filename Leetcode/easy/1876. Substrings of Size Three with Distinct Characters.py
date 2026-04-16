# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        count = 0
        for i, ch in enumerate(s[:-2]):
            if ch != s[i + 1] and ch != s[i + 2] and s[i + 1] != s[i + 2]:
                count += 1
        return count 


