# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-special-substring-of-length-k/description/

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            if j - i == k:
                return True
            i = j
        return False


