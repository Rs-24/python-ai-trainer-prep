

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        c = 0
        for t in preorder.split(","):
            c -= 1
            if c < 0:
                return False
            c += 2 * (t != "#")
        return c == 0


