# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Time: O(n), n = len(s1) = len(s2)
        # Space: O(1)
        num_diff = []
        for i, ch in enumerate(s1):
            if ch != s2[i]:
                num_diff.append(i)
                if len(num_diff) > 2:
                    return False
        if len(num_diff) == 1:
            return False
        elif len(num_diff) == 0:
            return True
        i, j = num_diff
        return s1[i] == s2[j] and s1[j] == s2[i]


