

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        # Time: O(n)
        # Space: O(n)
        return "".join([s[(i + k) % len(s)] for i in range(len(s))])


