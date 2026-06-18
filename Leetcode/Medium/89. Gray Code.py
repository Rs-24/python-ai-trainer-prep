

class Solution:
    def grayCode(self, n: int) -> list:
        # Time: O(2 ** n)
        # Space: O(2 ** n)
        return [x ^ (x >> 1) for x in range(2 ** n)]


