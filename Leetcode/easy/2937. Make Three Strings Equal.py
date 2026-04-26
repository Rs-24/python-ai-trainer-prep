# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/make-three-strings-equal/description/

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        # Time: O(n), n = min(len(s1), len(s2), len(s3))
        # Space: O(1)
        if not (s1[0] == s2[0] == s3[0]):
            return -1 
        i = 0
        while i < min(len(s1), len(s2), len(s3)):
            if not (s1[i] == s2[i] == s3[i]):
                break
            i += 1
        return len(s1) + len(s2) + len(s3) - 3 * i


