# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/equal-score-substrings/description/

class Solution:
    def scoreBalance(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        l_sum = ord(s[0]) - ord("a") + 1
        r_sum = sum(ord(ch) - ord("a") + 1 for ch in s) - l_sum
        for i in range(1, len(s) - 1):
            l_sum += ord(s[i]) - ord("a") + 1
            r_sum -= ord(s[i]) - ord("a") + 1
            if l_sum == r_sum:
                return True
        return False


