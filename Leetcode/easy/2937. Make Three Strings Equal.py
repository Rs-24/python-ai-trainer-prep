

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        # Time: O(n)
        # Space: O(n)
        for i in range(min(len(s1), len(s2), len(s2))):
            if not (s1[i] == s2[i] == s3[i]) or i == len(s1) - 1 or i == len(s2) - 1 or i == len(s3) - 1:
                return -1 if i == 0 else len(s1) + len(s2) + len(s3) - 3 * i
        

