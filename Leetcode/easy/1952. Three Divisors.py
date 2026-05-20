

class Solution:
    def isThree(self, n: int) -> bool:
        # Time: O(n)
        # Space: O(1)
        found = False
        for d in range(2, n):
            if n % d == 0:
                if not found:
                    found = True
                else:
                    return False
        return found


