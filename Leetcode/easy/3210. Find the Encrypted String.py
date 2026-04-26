# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-encrypted-string/description/

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        # Time: O(n), n = len(s)
        # Aux space: O(1)
        n = len(s)
        out = []
        for i in range(n):
            out.append(s[(i + k) % n])
        return "".join(out)


